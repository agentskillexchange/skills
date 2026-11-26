"""The invariants that make capture safe to leave switched on forever.

Every test here corresponds to a promise made in the spec. They are written to FAIL if
the promise breaks, not to demonstrate that the happy path works — the happy path is
covered by capture.py's own selftest. These are the ones that bite in production:
concurrency, crash-safety, latency, secret leakage, and never breaking the caller.
"""
from __future__ import annotations

import json
import os
import signal
import subprocess
import sys
import textwrap
import time
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
CAPTURE = REPO / "src" / "chronicle" / "capture.py"

sys.path.insert(0, str(CAPTURE.parent))
import capture as cap  # noqa: E402


def test_hook_actor_prefers_payload_then_explicit_harness_environment(monkeypatch):
    monkeypatch.setenv("CHRONICLE_HARNESS", "codex")
    assert cap._actor_from_hook({})["harness"] == "codex"
    assert cap._actor_from_hook({"harness": "claude-code"})["harness"] == "claude-code"


def test_hook_actor_keeps_legacy_claude_default(monkeypatch):
    monkeypatch.delenv("CHRONICLE_HARNESS", raising=False)
    assert cap._actor_from_hook({})["harness"] == "claude-code"


@pytest.fixture()
def home(tmp_path, monkeypatch):
    """Isolate CHRONICLE_HOME so tests never touch the real ledger."""
    h = tmp_path / "chron-home"
    h.mkdir()
    monkeypatch.setattr(cap, "CHRON_HOME", str(h))
    monkeypatch.setenv("CHRONICLE_HOME", str(h))
    monkeypatch.setenv("CHRONICLE_MACHINE", "testbox")
    return h


@pytest.fixture()
def repo(tmp_path):
    """A minimal git repo — enough for repo_root/git_head, without running git."""
    r = tmp_path / "proj"
    (r / ".git" / "refs" / "heads").mkdir(parents=True)
    (r / ".git" / "HEAD").write_text("ref: refs/heads/main\n")
    (r / ".git" / "refs" / "heads" / "main").write_text("deadbeefcafe1234\n")
    return r


def _lane_lines(path: Path):
    return [json.loads(l) for l in path.read_text().splitlines() if l.strip()]


# ── invariant 1: never breaks the caller ─────────────────────────────────────

@pytest.mark.parametrize("stdin_payload", [
    "",                       # empty
    "not json at all",        # garbage
    "null",                   # valid json, wrong type
    "[]",                     # valid json, wrong type
    '{"hook_event_name": "PostToolUse"}',            # missing everything
    '{"hook_event_name":"PostToolUse","tool_name":"Write","tool_input":null}',
    '{"hook_event_name":"PostToolUse","tool_name":"Write","tool_input":{"file_path":null}}',
    '{"hook_event_name":"\\u0000weird","cwd":"/nonexistent/deeply/nested"}',
])
def test_hook_always_exits_zero(stdin_payload, tmp_path):
    """A non-zero exit from a hook is a user-visible failure caused by nothing the user
    did. There is no input for which this may happen.

    NOTE the cwd= argument. Isolating CHRONICLE_HOME is not enough: the LANE path is
    derived from the working directory, so a payload with no `cwd` falls back to
    os.getcwd() — and an earlier version of this test therefore wrote 12 synthetic events
    into this repo's own real ledger. Isolate every path the code can reach, not just the
    one you were thinking about.
    """
    sandbox = tmp_path / "sandbox"
    sandbox.mkdir()
    # Snapshot first: a pre-existing stray lane (from before this isolation fix) must not
    # make every future run fail for something it did not do.
    lanes_dir = REPO / ".chronicle" / "lanes"
    before_leak = set(lanes_dir.glob("testbox.*")) if lanes_dir.exists() else set()
    env = dict(os.environ, CHRONICLE_HOME=str(tmp_path / "h"), CHRONICLE_MACHINE="testbox")
    proc = subprocess.run(
        [sys.executable, str(CAPTURE), "hook"],
        input=stdin_payload, text=True, capture_output=True, env=env,
        cwd=str(sandbox), timeout=30)
    assert proc.returncode == 0, proc.stderr
    # Anything printed must be valid JSON — the harness parses it.
    if proc.stdout.strip():
        json.loads(proc.stdout)
    # And nothing may have escaped the sandbox into a real ledger.
    assert set((REPO / ".chronicle" / "lanes").glob("testbox.*")) == before_leak, \
        "this test wrote events into the real ledger"


def test_unwritable_lane_falls_back_to_quarantine(home, repo, monkeypatch):
    """A read-only repo must not cost us the event."""
    lanes = repo / ".chronicle" / "lanes"
    lanes.mkdir(parents=True)
    lanes.chmod(0o500)  # no write
    try:
        cap.emit({"kind": "note", "summary": "trapped"}, str(repo), "s1")
        q = home / "quarantine.jsonl"
        assert q.exists(), "event was lost instead of quarantined"
        assert "trapped" in q.read_text()
    finally:
        lanes.chmod(0o700)


def test_capture_never_networks():
    """Static guarantee: the capture file must not import any network module.

    Checked by parsing imports rather than by monkeypatching, because the promise is
    about the file's contents, not about one execution path through it.
    """
    import ast
    tree = ast.parse(CAPTURE.read_text())
    banned = {"socket", "http", "urllib", "requests", "httpx", "ftplib", "smtplib",
              "telnetlib", "asyncio", "ssl", "xmlrpc"}
    found = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for a in node.names:
                found.add(a.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom) and node.module:
            found.add(node.module.split(".")[0])
    offenders = (found & banned) - {"socket"}   # socket is used for gethostname only
    assert not offenders, f"capture.py imports network modules: {offenders}"
    # And socket may only be used for the hostname.
    src = CAPTURE.read_text()
    for bad in ("socket.socket", "socket.create_connection", "socket.AF_INET"):
        assert bad not in src, f"capture.py uses {bad}"


def test_timeout_is_bounded(home, repo, monkeypatch):
    """A capture that hangs holds up the user's tool call. The guard must cut it off."""
    monkeypatch.setattr(cap, "TIMEOUT_S", 0.3)

    def hang():
        time.sleep(5)

    start = time.time()
    cap.run_guarded(hang)
    assert time.time() - start < 2.0, "run_guarded did not enforce its timeout"


# ── invariant 2: concurrency ─────────────────────────────────────────────────

def test_concurrent_writers_never_interleave(tmp_path, monkeypatch):
    """Eight processes appending large records to ONE lane: every line must parse.

    This is the test that justifies flock. With plain O_APPEND and records over
    PIPE_BUF, writes tear and lines become unparseable JSON.
    """
    home = tmp_path / "h"
    repo = tmp_path / "proj"
    (repo / ".git").mkdir(parents=True)
    (repo / ".git" / "HEAD").write_text("ref: refs/heads/main\n")
    # The children run with CHRONICLE_MACHINE=testbox; the parent must resolve the lane
    # name under the same identity or it goes looking for a file nobody wrote.
    monkeypatch.setenv("CHRONICLE_MACHINE", "testbox")

    script = textwrap.dedent(f"""
        import sys, os
        sys.path.insert(0, {str(CAPTURE.parent)!r})
        os.environ["CHRONICLE_HOME"] = {str(home)!r}
        os.environ["CHRONICLE_MACHINE"] = "testbox"
        import capture as cap
        cap.CHRON_HOME = {str(home)!r}
        big = "x" * 20000          # far above PIPE_BUF, so torn writes are possible
        for i in range(40):
            cap.emit({{"kind": "note", "summary": big, "worker": sys.argv[1], "i": i}},
                     {str(repo)!r}, "shared-session")
    """)
    sfile = tmp_path / "w.py"
    sfile.write_text(script)

    procs = [subprocess.Popen([sys.executable, str(sfile), str(i)]) for i in range(8)]
    for p in procs:
        assert p.wait(timeout=120) == 0

    lane = Path(cap.lane_path(str(repo), "shared-session"))
    lines = [l for l in lane.read_text().splitlines() if l.strip()]
    assert len(lines) == 8 * 40, f"lost events: {len(lines)} of 320"
    parsed = [json.loads(l) for l in lines]          # raises on a torn line
    assert len({p["id"] for p in parsed}) == 320, "duplicate ids"


# ── invariant 3: crash safety ────────────────────────────────────────────────

def test_sigkill_midwrite_leaves_prior_lines_intact(tmp_path, monkeypatch):
    """SIGKILL during capture may truncate the LAST line. It may not damage earlier ones."""
    home = tmp_path / "h"
    repo = tmp_path / "proj"
    (repo / ".git").mkdir(parents=True)
    (repo / ".git" / "HEAD").write_text("ref: refs/heads/main\n")
    # The children run with CHRONICLE_MACHINE=testbox; the parent must resolve the lane
    # name under the same identity or it goes looking for a file nobody wrote.
    monkeypatch.setenv("CHRONICLE_MACHINE", "testbox")

    script = textwrap.dedent(f"""
        import sys, os, time
        sys.path.insert(0, {str(CAPTURE.parent)!r})
        os.environ["CHRONICLE_HOME"] = {str(home)!r}
        os.environ["CHRONICLE_MACHINE"] = "testbox"
        import capture as cap
        cap.CHRON_HOME = {str(home)!r}
        i = 0
        while True:
            cap.emit({{"kind": "note", "summary": "y" * 5000, "i": i}}, {str(repo)!r}, "crash")
            i += 1
    """)
    sfile = tmp_path / "spin.py"
    sfile.write_text(script)
    proc = subprocess.Popen([sys.executable, str(sfile)])
    time.sleep(2.0)
    proc.send_signal(signal.SIGKILL)
    proc.wait(timeout=30)

    lane = Path(cap.lane_path(str(repo), "crash"))
    lines = [l for l in lane.read_text().splitlines() if l.strip()]
    assert len(lines) > 3, "test did not produce enough events to be meaningful"
    for idx, line in enumerate(lines[:-1]):          # all but possibly the last
        json.loads(line)                             # must parse


# ── invariant 4: secrets never enter the store ───────────────────────────────

def test_secret_files_never_reach_the_cas(home, repo):
    """Fixture repo full of credentials → zero secret bytes anywhere in the store."""
    secrets = {
        ".env": "SHOPIFY_TOKEN=shpat_" + "a" * 32,
        ".env.production": "DB_PASSWORD=hunter2-very-secret",
        "id_rsa": "-----BEGIN OPENSSH PRIVATE KEY-----\nMIIEpQIBAAKCA-SECRETKEY\n",
        "service-account.json": '{"private_key": "-----BEGIN PRIVATE KEY-----SECRETKEY"}',
        "creds.pem": "-----BEGIN CERTIFICATE-----SECRETKEY",
    }
    for name, body in secrets.items():
        (repo / name).write_text(body)

    for name in secrets:
        desc = cap.snapshot_file(str(repo / name))
        assert desc.get("redacted") is True, f"{name} was not treated as a secret"
        assert "sha" not in desc, f"{name} content entered the CAS"

    # Nothing anywhere in the store may contain the marker.
    for root, _dirs, files in os.walk(home):
        for f in files:
            blob = Path(root) / f
            data = blob.read_bytes()
            assert b"SECRETKEY" not in data, f"secret leaked into {blob}"
            assert b"hunter2" not in data, f"secret leaked into {blob}"
            assert b"shpat_aaaa" not in data, f"secret leaked into {blob}"


def test_secret_bearing_command_is_masked_not_dropped(home, repo):
    """The command still happened. Record it — with the credential masked."""
    payload = {
        "hook_event_name": "PostToolUse", "tool_name": "Bash", "session_id": "s",
        "cwd": str(repo),
        "tool_input": {"command": "curl -H 'Authorization: Bearer ghp_" + "b" * 30 + "' https://api"},
        "tool_response": {"stdout": "ok", "exit_code": 0},
    }
    cap.handle_hook(payload)
    lane = Path(cap.lane_path(str(repo), "s"))
    events = _lane_lines(lane)
    assert len(events) == 1, "the event was dropped instead of masked"
    text = json.dumps(events[0], ensure_ascii=False)
    assert "ghp_bbbb" not in text, "credential survived into the record"
    assert cap.MASK in text, "credential was removed without leaving a mask"
    assert "curl" in text, "the fact that curl ran was lost"


def test_normal_source_file_is_stored_fully(home, repo):
    """The denylist must not be so broad that ordinary work stops being captured."""
    src = repo / "main.py"
    body = "def f():\n    return 'hello world'\n" * 50
    src.write_text(body)
    desc = cap.snapshot_file(str(src))
    assert desc.get("redacted") is not True
    assert cap.cas_get(desc["sha"]).decode() == body


# ── invariant 5: content addressing ──────────────────────────────────────────

def test_dedup_stores_one_blob(home):
    data = b"identical content" * 500
    d1 = cap.cas_put(data)
    d2 = cap.cas_put(data)
    assert d1 == d2
    shard = home / "cas" / d1.split(":")[1][:2]
    blobs = [p for p in shard.iterdir() if not p.name.startswith(".tmp")]
    assert len(blobs) == 1, f"dedup failed: {blobs}"


def test_gzip_and_zstd_blobs_share_a_hash_and_both_read(home, monkeypatch):
    """A blob written on one host (gzip, py3.9) and on another (zstd, py3.14) must be the
    same object. This is what lets the two machines' stores merge by union."""
    import gzip
    zstd = pytest.importorskip("compression.zstd", reason="legacy zstd decoding requires Python 3.14+")
    data = b"cross-machine content" * 200
    digest = cap.cas_put(data)                       # native codec
    hexd = digest.split(":")[1]
    shard = home / "cas" / hexd[:2]

    # Simulate the other machine's codec landing beside it.
    existing = next(p for p in shard.iterdir() if not p.name.startswith(".tmp"))
    other_ext = "gz" if existing.suffix == ".zst" else "zst"
    if other_ext == "gz":
        payload = gzip.compress(data)
    else:
        payload = zstd.compress(data)
    (shard / f"{hexd}.{other_ext}").write_bytes(payload)

    assert cap.cas_get(digest) == data
    existing.unlink()                                # only the foreign codec remains
    assert cap.cas_get(digest) == data, "foreign-codec blob was unreadable"
    assert cap.cas_verify(digest)


def test_new_captures_use_portable_gzip(home):
    digest = cap.cas_put(b"portable across supported Python versions")
    hexd = digest.split(":")[1]
    assert (home / "cas" / hexd[:2] / (hexd + ".gz")).is_file()


def test_unavailable_zstd_does_not_hide_readable_gzip(home, monkeypatch):
    import builtins
    import gzip
    data = b"portable fallback"
    digest = cap.cas_put(data)
    hexd = digest.split(":")[1]
    shard = home / "cas" / hexd[:2]
    (shard / (hexd + ".gz")).write_bytes(gzip.compress(data))
    (shard / (hexd + ".zst")).write_bytes(b"unsupported legacy encoding")
    original_import = builtins.__import__

    def without_compression(name, *args, **kwargs):
        if name == "compression":
            raise ImportError("unavailable on this interpreter")
        return original_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", without_compression)
    assert cap.cas_get(digest) == data


def test_tampered_blob_fails_verification(home):
    digest = cap.cas_put(b"trust me")
    hexd = digest.split(":")[1]
    shard = home / "cas" / hexd[:2]
    blob = next(p for p in shard.iterdir() if not p.name.startswith(".tmp"))
    blob.write_bytes(b"garbage that is not the original")
    assert cap.cas_verify(digest) is False, "tampering went undetected"


# ── invariant 6: latency ─────────────────────────────────────────────────────

def test_capture_latency_is_small(home, repo):
    """Capture is on the critical path of every tool call. A slow capture is a capture
    that gets switched off, which is the only true failure mode."""
    src = repo / "code.py"
    src.write_text("x = 1\n" * 500)
    payload = {"hook_event_name": "PostToolUse", "tool_name": "Write",
               "session_id": "perf", "cwd": str(repo),
               "tool_input": {"file_path": str(src)},
               "tool_response": {"stdout": "ok"}}
    cap.handle_hook(payload)                          # warm caches

    timings = []
    for i in range(60):
        src.write_text(f"x = {i}\n" * 500)            # defeat dedup: real work each time
        t0 = time.perf_counter()
        cap.handle_hook(payload)
        timings.append((time.perf_counter() - t0) * 1000)
    timings.sort()
    p99 = timings[int(len(timings) * 0.99) - 1]
    assert p99 < 50, f"p99 capture latency {p99:.1f} ms exceeds 50 ms budget"


# ── behaviour: before/after pairing ──────────────────────────────────────────

def test_edit_records_before_and_after(home, repo):
    """The point of the whole system: an edit has a real predecessor, even for a file
    git has never seen."""
    target = repo / "never_committed.txt"
    target.write_text("original content\n")
    session = "pair"
    pre = {"hook_event_name": "PreToolUse", "tool_name": "Edit", "session_id": session,
           "cwd": str(repo), "tool_input": {"file_path": str(target)}}
    cap.handle_hook(pre)
    target.write_text("replaced content\n")
    post = dict(pre, hook_event_name="PostToolUse", tool_response={"stdout": "ok"})
    cap.handle_hook(post)

    events = _lane_lines(Path(cap.lane_path(str(repo), session)))
    edits = [e for e in events if e["kind"] == "file.edit"]
    assert len(edits) == 1
    f = edits[0]["files"][0]
    assert f["before"] and f["after"] and f["before"] != f["after"]
    assert cap.cas_get(f["before"]).decode() == "original content\n"
    assert cap.cas_get(f["after"]).decode() == "replaced content\n"


def test_capture_off_sentinel_suspends_everything(home, repo):
    (home / "OFF").write_text("")
    payload = {"hook_event_name": "PostToolUse", "tool_name": "Bash", "session_id": "off",
               "cwd": str(repo), "tool_input": {"command": "echo private"},
               "tool_response": {"stdout": "private"}}
    cap.handle_hook(payload)
    lane = Path(cap.lane_path(str(repo), "off"))
    assert not lane.exists(), "capture ran while suspended"


def test_ulids_sort_chronologically_across_time(home):
    a = cap.ulid()
    time.sleep(0.01)
    b = cap.ulid()
    assert a < b, "ULIDs are not time-sortable; spine merge-by-sort would be wrong"


def test_events_are_json_line_delimited_and_stable(home, repo):
    """The spine merges by `sort -u` on raw lines. That requires deterministic key order."""
    cap.emit({"kind": "note", "summary": "b", "zebra": 1, "alpha": 2}, str(repo), "s")
    line = Path(cap.lane_path(str(repo), "s")).read_text().splitlines()[0]
    assert line.index('"alpha"') < line.index('"zebra"'), "keys are not sorted"
    assert "\n" not in line.strip()


def test_lane_names_are_unique_per_root(home, tmp_path):
    """Regression: lane identity is (machine, session, ROOT), not (machine, session).

    One session writes a lane in every repo it visits, plus a home lane when it steps
    outside one. With only machine+session in the filename, those collided on the same
    destination name in the spine and were appended into each other — 7 KB of home-lane
    events concatenated onto a 198 KB repo lane. The "merge is union, no conflict class"
    property depends on lane names being globally unique.
    """
    repo_a = tmp_path / "a"
    (repo_a / ".git").mkdir(parents=True)
    (repo_a / ".git" / "HEAD").write_text("ref: refs/heads/main\n")
    repo_b = tmp_path / "b"
    (repo_b / ".git").mkdir(parents=True)
    (repo_b / ".git" / "HEAD").write_text("ref: refs/heads/main\n")
    outside = tmp_path / "nowhere"
    outside.mkdir()

    session = "same-session"
    names = {Path(cap.lane_path(str(p), session)).name
             for p in (repo_a, repo_b, outside)}
    assert len(names) == 3, f"lane names collided across roots: {names}"

    # And the same root must always produce the SAME name, or a session would fragment
    # into a new lane on every single event.
    assert cap.lane_path(str(repo_a), session) == cap.lane_path(str(repo_a), session)
    assert cap.lane_path(str(repo_a / "deep" / "nested"), session) == \
        cap.lane_path(str(repo_a), session), "subdirectories must share the repo's lane"


def test_chronicle_dir_ignores_itself(home, repo):
    """Capture writes a lane into EVERY repo anyone works in. Without a self-ignoring
    directory, each one grows a permanent `?? .chronicle/` in git status, and eventually
    someone commits the raw trace into a client-facing repo.

    Self-ignoring rather than editing the repo's own .gitignore: that file belongs to the
    project, and a tool the project never opted into should not be modifying it.
    """
    cap.emit({"kind": "note", "summary": "x"}, str(repo), "s")
    marker = repo / ".chronicle" / ".gitignore"
    assert marker.exists(), ".chronicle/ does not ignore itself"
    assert marker.read_text().rstrip().endswith("*")

    # And it must not have touched the repo's own .gitignore.
    assert not (repo / ".gitignore").exists(), "capture edited the project's .gitignore"


def test_self_ignore_does_not_clobber_an_existing_file(home, repo):
    """If someone deliberately customised .chronicle/.gitignore, keep it."""
    d = repo / ".chronicle"
    d.mkdir(parents=True)
    (d / ".gitignore").write_text("# hand-written\n*\n!keep-me\n")
    cap.emit({"kind": "note", "summary": "x"}, str(repo), "s")
    assert "!keep-me" in (d / ".gitignore").read_text()
