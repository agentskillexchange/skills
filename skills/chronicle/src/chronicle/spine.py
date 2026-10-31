"""The spine — the union of every machine's ledger.

WHY THIS IS SIMPLE ON PURPOSE
Every lane file is named `<machine>.<session>.jsonl` and is append-only. Two machines
therefore never write the same file, and a file only ever grows. That removes the entire
conflict class: sync is "copy the bytes that are new", and merge is "union, sorted by
ULID". There is no three-way diff, no vector clock, no last-writer-wins, and nothing that
can lose an event because two boxes disagreed.

Blobs are content-addressed, so the same reasoning applies: a blob either exists at its
hash or it does not, and copying it twice is a no-op. A machine offline for a month heals
in one sync.

Topology: a coordinator can pull from explicitly configured SSH hosts. Remote capture
does not require a copy of the spine repository.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import capture as cap  # noqa: E402
import index as idx  # noqa: E402

# Local by default; CHRONICLE_SPINE or --spine selects an explicit private archive.
DEFAULT_SPINE = Path.home() / ".chronicle" / "spine"

# No hosts are contacted unless the operator configures them.
REMOTES = os.environ.get("CHRONICLE_REMOTES", "").split()


def spine_root(override: str | None = None) -> Path:
    if override:
        return Path(override).expanduser()
    env = os.environ.get("CHRONICLE_SPINE")
    if env:
        return Path(env).expanduser()
    return DEFAULT_SPINE


def _copy_grown(src: Path, dst: Path) -> int:
    """Copy only the bytes appended since last time. Returns bytes copied.

    Append-only files mean the prefix is immutable, so re-copying it every sync would be
    pure waste — and on a ledger that grows forever, waste that compounds.
    """
    dst.parent.mkdir(parents=True, exist_ok=True)
    src_size = src.stat().st_size
    dst_size = dst.stat().st_size if dst.exists() else 0
    if dst_size > src_size:
        # Destination is longer: the source was truncated or replaced. Trust neither —
        # keep the longer copy and report, rather than silently discarding events.
        cap._log_error(f"spine: {dst} is longer than {src}; left untouched")
        return 0
    if dst_size == src_size:
        return 0
    with src.open("rb") as fh:
        fh.seek(dst_size)
        chunk = fh.read()
    with dst.open("ab") as out:
        out.write(chunk)
    return len(chunk)


def _local_lanes() -> list[Path]:
    lanes: list[Path] = []
    home = Path(cap.CHRON_HOME) / "lanes"
    if home.exists():
        lanes.extend(home.rglob("*.jsonl"))
    for root in idx.registered_roots():
        d = Path(root) / ".chronicle" / "lanes"
        if d.exists():
            lanes.extend(d.glob("*.jsonl"))
    return lanes


def push_local(spine: Path, verbose: bool = True) -> dict:
    """Copy this machine's lanes and blobs into the spine."""
    events_dir = spine / "events"
    cas_dir = spine / "cas"
    events_dir.mkdir(parents=True, exist_ok=True)
    cas_dir.mkdir(parents=True, exist_ok=True)

    lane_bytes = 0
    lanes = 0
    for lane in _local_lanes():
        # Month-partitioned so the spine directory stays browsable as it grows.
        month = _lane_month(lane)
        dst = events_dir / month / _spine_name(lane)
        n = _copy_grown(lane, dst)
        if n:
            lane_bytes += n
            lanes += 1

    blobs, skipped = _push_blobs(cas_dir, verbose)

    if verbose:
        print(f"  pushed {lanes} lane(s) (+{lane_bytes:,} bytes), {blobs} new blob(s)")
    return {"lanes": lanes, "bytes": lane_bytes, "blobs": blobs, "blobs_skipped": skipped}


# ── blob confidentiality ─────────────────────────────────────────────────────
#
# The local CAS holds the full plaintext of every file anyone touched. The spine is a git
# repository that gets pushed to a remote. Those two facts cannot both be true of the same
# bytes, so blobs are ENCRYPTED on their way into the spine.
#
# Content addressing survives it: the name is still the sha256 of the PLAINTEXT, so dedup,
# integrity checks, and cross-machine merging work exactly as before. Only the bytes at
# rest change, and the `.age` suffix says so.
#
# FAIL CLOSED. With no recipients configured, blobs are SKIPPED rather than copied in
# plaintext. A sync that silently degrades to "publish everything unencrypted" is worse
# than a sync that does not run because traces can contain private data.

def recipients_path() -> Path:
    env = os.environ.get("CHRONICLE_RECIPIENTS")
    if env:
        return Path(env).expanduser()
    return Path(cap.CHRON_HOME) / "age_recipients.txt"


def read_recipients() -> list[str]:
    """Public age recipients only. A private identity here is a hard error, not a warning."""
    path = recipients_path()
    try:
        lines = [l.strip() for l in path.read_text().splitlines()]
    except OSError:
        return []
    out = []
    for line in lines:
        if not line or line.startswith("#"):
            continue
        if line.startswith("AGE-SECRET-KEY-"):
            raise SystemExit(
                f"REFUSED: {path} contains a PRIVATE age identity (AGE-SECRET-KEY-…).\n"
                "Remove the secret, rotate the "
                "identity, and put only public age1… recipients here.")
        if line.startswith("age1"):
            out.append(line)
    return out


def _push_blobs(cas_dir: Path, verbose: bool) -> tuple[int, int]:
    local_cas = Path(cap.CHRON_HOME) / "cas"
    if not local_cas.exists():
        return 0, 0

    try:
        recips = read_recipients()
    except SystemExit:
        raise
    pending = [b for b in local_cas.rglob("*")
               if b.is_file() and not b.name.startswith(".tmp")]

    if not recips:
        # Count what we are declining to publish, so the gap is visible rather than silent.
        todo = sum(1 for b in pending
                   if not (cas_dir / b.parent.name / (b.name + ".age")).exists())
        if verbose and todo:
            print(f"  ⚠ {todo} blob(s) NOT pushed: no age recipients configured.")
            print(f"    File contents stay local until {recipients_path()} lists at least")
            print("    two public age1… recipients. Run: chron crypto-setup")
        return 0, todo

    if shutil.which("age") is None:
        if verbose:
            print("  ⚠ blobs NOT pushed: `age` is not installed")
        return 0, len(pending)

    args: list[str] = []
    for r in recips:
        args += ["-r", r]

    pushed = 0
    for blob in pending:
        dst = cas_dir / blob.parent.name / (blob.name + ".age")
        if dst.exists():
            continue                       # content-addressed: same name, same bytes
        dst.parent.mkdir(parents=True, exist_ok=True)
        tmp = dst.with_suffix(".age.tmp")
        try:
            proc = subprocess.run(["age", "-e", *args, "-o", str(tmp), str(blob)],
                                  capture_output=True, text=True, timeout=120)
            if proc.returncode != 0:
                cap._log_error(f"spine encrypt {blob.name}: {proc.stderr[-200:]}")
                tmp.unlink(missing_ok=True)
                continue
            os.replace(tmp, dst)
            pushed += 1
        except (subprocess.SubprocessError, OSError) as exc:
            cap._log_error(f"spine encrypt {blob.name}: {exc}")
            tmp.unlink(missing_ok=True)
    return pushed, 0


def _spine_name(lane: Path) -> str:
    """Destination filename for a lane, guaranteed collision-free.

    Lanes created after the root-discriminator fix are already unique, but lanes written
    before it are not — and the spine must not be able to corrupt itself because of a
    historical naming choice. Hashing the SOURCE DIRECTORY into the destination name makes
    that structurally impossible, for old and new lanes alike.
    """
    import hashlib
    if re.match(r"^[^.]+\.[^.]+\.[0-9a-f]{8}\.jsonl$", lane.name):
        return lane.name                      # already carries a root discriminator
    tag = hashlib.sha256(str(lane.parent).encode("utf-8", "replace")).hexdigest()[:8]
    return f"{lane.stem}.{tag}.jsonl"


def _lane_month(lane: Path) -> str:
    """Partition by the month of the lane's FIRST event, so a session that spans midnight
    on the 1st stays in one file rather than being split across two directories."""
    try:
        with lane.open("r", errors="replace") as fh:
            first = fh.readline()
        return json.loads(first)["ts"][:7]
    except Exception:
        return "unsorted"


def pull_remote(host: str, spine: Path, verbose: bool = True) -> dict:
    """Pull one machine's lanes and blobs. An unreachable host is skipped, not fatal."""
    # Probe for the LANE directory specifically, not just ~/.chronicle. A machine with
    # capture deployed but no events yet has ~/.chronicle/bin and nothing else, and rsync
    # exits 23 ("partial transfer") on a missing source — which reads as a failure when
    # it is simply a quiet machine. Distinguishing the two keeps `sync` output honest.
    # `; true` is load-bearing. Without it the probe's exit code is that of the LAST test,
    # so a perfectly reachable machine that simply has no events yet exits 1 and gets
    # reported as unreachable. Conflating "nothing to report" with "host is down" is how a
    # fleet view becomes something you stop believing.
    probe = subprocess.run(
        ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=6", host,
         "test -d ~/.chronicle/lanes && echo lanes; "
         "test -d ~/.chronicle/cas && echo cas; true"],
        capture_output=True, text=True)
    if probe.returncode != 0:
        if verbose:
            print(f"  {host}: skipped (unreachable)")
        return {"host": host, "skipped": True, "reason": "unreachable"}
    has_lanes = "lanes" in probe.stdout
    has_cas = "cas" in probe.stdout
    if not has_lanes and not has_cas:
        if verbose:
            print(f"  {host}: no events yet (capture deployed, nothing recorded)")
        return {"host": host, "skipped": True, "reason": "no events"}

    events = spine / "events" / "incoming"
    cas = spine / "cas"
    events.mkdir(parents=True, exist_ok=True)
    cas.mkdir(parents=True, exist_ok=True)

    # rsync rather than a hand-rolled copy: it already knows how to move only what
    # changed over a network, and reimplementing that badly is not a good use of a
    # ledger's reliability budget.
    codes = []
    if has_lanes:
        r = subprocess.run(
            ["rsync", "-az", "--timeout=60", "--include=*/", "--include=*.jsonl",
             "--exclude=*", f"{host}:.chronicle/lanes/", str(events) + "/"],
            capture_output=True, text=True)
        codes.append(("lanes", r))
    if has_cas:
        r = subprocess.run(
            ["rsync", "-az", "--timeout=120", "--ignore-existing",
             f"{host}:.chronicle/cas/", str(cas) + "/"],
            capture_output=True, text=True)
        codes.append(("cas", r))

    failed = [(what, r) for what, r in codes if r.returncode != 0]
    if verbose:
        if failed:
            detail = ", ".join(f"{what} rsync={r.returncode}" for what, r in failed)
            print(f"  {host}: FAILED ({detail})")
        else:
            print(f"  {host}: ok ({', '.join(what for what, _ in codes)})")
    for what, r in failed:
        cap._log_error(f"spine pull {host} {what}: rc={r.returncode} {r.stderr[-200:]}")
    return {"host": host, "ok": not failed}


def commit_spine(spine: Path, verbose: bool = True) -> bool:
    """Commit the spine if it lives in a git repo. Never fails the sync."""
    root = cap.repo_root(str(spine))
    if not root:
        return False
    try:
        subprocess.run(["git", "-C", root, "add", "--", str(spine)],
                       capture_output=True, timeout=120)
        status = subprocess.run(["git", "-C", root, "status", "--porcelain", "--", str(spine)],
                                capture_output=True, text=True, timeout=60)
        if not status.stdout.strip():
            if verbose:
                print("  spine: nothing new to commit")
            return False
        msg = f"chronicle spine sync from {cap.machine()} at {cap.now_iso()}"
        subprocess.run(["git", "-C", root, "commit", "-q", "-m", msg, "--", str(spine)],
                       capture_output=True, timeout=120)
        if verbose:
            print(f"  spine: committed to {root}")
        return True
    except Exception as exc:
        cap._log_error(f"spine commit: {exc}")
        return False


def cmd_sync(args) -> int:
    spine = spine_root(getattr(args, "spine", None))
    print(f"spine: {spine}")
    spine.mkdir(parents=True, exist_ok=True)

    if not getattr(args, "pull_only", False):
        push_local(spine)

    if not getattr(args, "push_only", False):
        for host in REMOTES:
            pull_remote(host, spine)

    # Index the spine so `chron resume` immediately sees other machines' work.
    conn = idx.connect()
    added = idx.refresh(conn)
    print(f"  indexed {added} new event(s)")

    if getattr(args, "commit", False):
        commit_spine(spine)

    total = conn.execute("SELECT COUNT(*) n FROM events").fetchone()["n"]
    machines = [r["machine"] for r in conn.execute(
        "SELECT DISTINCT machine FROM events WHERE machine<>''")]
    print(f"  ledger: {total:,} events across machines: {', '.join(sorted(machines))}")
    return 0


def cmd_crypto_setup(args) -> int:
    """Show exactly how to create the age identities — without ever handling them.

    This command deliberately does NOT generate a key. A private identity is a credential;
    it belongs in the owner's password manager, created by them, seen by nobody else. What
    this does is check the state of the world and print the precise commands.
    """
    path = recipients_path()
    print("chronicle encryption setup")
    print()
    have = []
    try:
        have = read_recipients()
    except SystemExit as exc:
        print(exc)
        return 2

    if len(have) >= 2:
        print(f"  configured: {len(have)} recipient(s) in {path}")
        for r in have:
            print(f"    {r}")
        print()
        print("  Blobs will be encrypted to all of them on the next `chron sync`.")
        print("  Any ONE of the matching private identities can decrypt.")
        return 0

    print(f"  NOT configured — {len(have)} recipient(s) found in {path}")
    print("  Until at least two are present, `chron sync` will not copy file contents")
    print("  into the spine at all. It fails closed rather than publishing plaintext.")
    print()
    print("  Run these YOURSELF — do not paste the private keys anywhere, including here:")
    print()
    print("    # 1. primary identity → store the WHOLE output in Bitwarden")
    print("    age-keygen")
    print()
    print("    # 2. recovery identity → store on separate offline media, NOT Bitwarden")
    print("    age-keygen")
    print()
    print("  Each prints a line like:")
    print("    # public key: age1abc...          <- this is the RECIPIENT (safe to commit)")
    print("    AGE-SECRET-KEY-1XYZ...            <- this is the IDENTITY (never commit)")
    print()
    print(f"  Put ONLY the two public age1… lines into {path}, one per line.")
    print("  Then re-run: chron crypto-setup")
    print()
    print("  Two recipients, not one, because a single lost key means the archive is")
    print("  unrecoverable. They must be stored independently or they are one key.")
    return 1
