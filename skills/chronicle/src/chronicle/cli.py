"""`chron` — the human and agent interface to the ledger.

Two families of command, and the split matters:

  WRITE   open · arm · decision · landed · close · note · correct
          The five moments a machine cannot infer. Everything else is captured for you.

  READ    resume · show · history · diff · restore · day · search · why · files · doctor
          The payoff. `resume` in particular has to be CHEAP, because a read-back that
          costs context is a read-back agents skip — which is exactly how v1 died.

Stdlib only, deliberately: `chron` is invoked on remote boxes with whatever interpreter
is on PATH, and a reader that needs a virtualenv is a reader that is not there when the
box is on fire.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import capture as cap  # noqa: E402
import index as idx  # noqa: E402

TRIGGERS = {
    "OPEN": "session start, after reading back — what state you believe you are in",
    "ARM": "BEFORE any destructive/bulk/irreversible operation — carries a restore path",
    "LANDED": "immediately after a deploy, publish, or external write",
    "DECISION": "a fork was chosen, or a state ruled INTENTIONAL vs BUG",
    "CLOSE": "session end — always, including on failure, interruption, or rate limit",
    "EXPERIMENT": "something was TRIED — hypothesis, setup, what varied, what the numbers were",
    "ABANDONED": "an approach was given up on — say why, so nobody retries it blindly",
    "NOTE": "anything else (use sparingly; one of the five is usually the honest label)",
}

CLASSES = {
    "R0": "fully reversible (git-tracked, no external side effect)",
    "R1": "reversible only via a named artifact (snapshot, rollback tag, backup file)",
    "R2": "irreversible (destroys data, or mutates third-party state with no undo)",
}


# ── presentation ─────────────────────────────────────────────────────────────

def _tty() -> bool:
    return sys.stdout.isatty() and not os.environ.get("NO_COLOR")


def c(text: str, code: str) -> str:
    return f"\033[{code}m{text}\033[0m" if _tty() else text


def bold(s): return c(s, "1")
def dim(s): return c(s, "2")
def red(s): return c(s, "31")
def green(s): return c(s, "32")
def yellow(s): return c(s, "33")
def blue(s): return c(s, "34")
def cyan(s): return c(s, "36")


def rule(title: str = "") -> str:
    width = min(shutil.get_terminal_size((80, 20)).columns, 100)
    if not title:
        return dim("─" * width)
    return dim("─── ") + bold(title) + " " + dim("─" * max(0, width - len(title) - 5))


def _ago(ts: str) -> str:
    try:
        then = datetime.fromisoformat(ts.replace("Z", "+00:00"))
    except Exception:
        return ts
    delta = datetime.now(timezone.utc) - then
    secs = int(delta.total_seconds())
    if secs < 90:
        return f"{secs}s ago"
    if secs < 5400:
        return f"{secs // 60}m ago"
    if secs < 172800:
        return f"{secs // 3600}h ago"
    return f"{secs // 86400}d ago"


# ── shared helpers ───────────────────────────────────────────────────────────

def _conn():
    conn = idx.connect()
    idx.refresh(conn)
    return conn


def _project(args) -> str | None:
    if getattr(args, "all", False):
        return None
    if getattr(args, "project", None):
        return args.project
    return cap.project_name(os.getcwd())


def _session() -> str:
    """Key state under the SAME identity the hooks use.

    Claude Code does not export its session id into the agent's shell, so the CLI cannot
    read it from the environment. The hooks publish it instead (capture.mark_current_
    session) and we read it back here. Getting this wrong is not cosmetic: it means
    `chron note` never clears the nudge counters, so the agent is told "nothing has been
    narrated yet" one second after narrating — and learns to ignore the nudge.
    """
    explicit = os.environ.get("CLAUDE_SESSION_ID") or os.environ.get("CHRONICLE_SESSION")
    if explicit:
        return explicit
    return cap.current_session() or "cli"


def _chronicle_md(cwd: str) -> Path | None:
    root = cap.repo_root(cwd)
    return Path(root) / "CHRONICLE.md" if root else None


MD_HEADER = """# CHRONICLE

Curated narrative for this project. The complete trace — every file, command, and
prompt, with full content — lives in the chronicle ledger; `chron resume` reads it back.

**Append only.** Corrections reference the entry they supersede; nothing is ever edited.

---
"""


def _append_md(cwd: str, entry_id: str, trigger: str, title: str, fields: dict) -> None:
    """Mirror a narrative entry into the repo's committed CHRONICLE.md.

    The lane is authoritative; this file exists so a collaborator (or a future you with
    no tooling installed) can read the story with nothing but a text editor.
    """
    path = _chronicle_md(cwd)
    if path is None:
        return
    lines = []
    if not path.exists():
        lines.append(MD_HEADER)
    lines.append(f"\n## [{entry_id}] {trigger} — {title}\n")
    order = ["intent", "state", "hypothesis", "setup", "varied", "result", "conclusion",
             "outcome", "what", "why", "class", "restore", "verified",
             "ext", "not_done", "open", "resolves"]
    labels = {"intent": "Intent", "state": "State reading", "what": "What", "why": "Why",
              "hypothesis": "Hypothesis", "setup": "Setup", "varied": "Varied",
              "result": "Result", "conclusion": "Conclusion", "outcome": "Outcome",
              "class": "Reversibility", "restore": "Restore", "verified": "Verified",
              "ext": "External", "not_done": "NOT done", "open": "OPEN",
              "resolves": "Resolves"}
    for key in order:
        val = fields.get(key)
        if not val:
            continue
        if key == "class":
            lines.append(f"- **Reversibility:** {val} — {CLASSES.get(val, '')}")
        elif key == "restore":
            lines.append(f"- **Restore:** `{val}`")
        elif isinstance(val, list):
            for item in val:
                lines.append(f"- **{labels[key]}:** {item}")
        else:
            lines.append(f"- **{labels[key]}:** {val}")
    if fields.get("inferred"):
        # Loud, in the file itself. Someone reading CHRONICLE.md in a text editor with no
        # tooling must not mistake a model's reconstruction for a witnessed account.
        lines.append("")
        lines.append("> ⚠ **INFERRED — NOT WITNESSED. MAY BE WRONG.** Reconstructed after "
                     "the fact by a model reading the trace. Do not treat as fact or act "
                     "on it without checking the anchored events. Where this conflicts "
                     "with a first-hand entry, the first-hand entry wins.")
    lines.append("")
    try:
        with path.open("a", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")
    except OSError:
        pass


def _entry_id() -> str:
    """Human-quotable id, kept in v1's shape so old references still resolve."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ") + "-" + cap.ulid()[-4:]


# ── write verbs ──────────────────────────────────────────────────────────────

def cmd_write(args) -> int:
    trigger = args._trigger
    cwd = os.getcwd()
    idx.register_root(cwd)

    if trigger == "ARM" and not args.restore:
        print(red("REFUSED: an ARM entry must carry --restore (how to get back)."))
        print("If the operation is genuinely irreversible, say so explicitly:")
        print("  --class R2 --restore 'IRREVERSIBLE: <what is lost and why accepted>'")
        return 2
    if getattr(args, "klass", None) in ("R1", "R2") and not args.restore:
        print(red(f"REFUSED: --class {args.klass} requires --restore naming the artifact "
                  "or stating IRREVERSIBLE."))
        return 2

    entry_id = _entry_id()
    fields = {
        "intent": getattr(args, "intent", None),
        "state": getattr(args, "state", None),
        "what": getattr(args, "what", None),
        "why": getattr(args, "why", None),
        "class": getattr(args, "klass", None),
        "restore": getattr(args, "restore", None),
        "verified": getattr(args, "verified", None) or [],
        "ext": getattr(args, "ext", None) or [],
        "not_done": getattr(args, "not_done", None),
        "open": getattr(args, "open", None) or [],
        "resolves": getattr(args, "resolves", None) or [],
        "hypothesis": getattr(args, "hypothesis", None),
        "setup": getattr(args, "setup", None),
        "varied": getattr(args, "varied", None),
        "result": getattr(args, "result", None),
        "conclusion": getattr(args, "conclusion", None),
        "outcome": getattr(args, "outcome", None),
    }
    fields = {k: v for k, v in fields.items() if v}

    # Credential guard, inherited from v1: the record must never be the leak.
    blob = json.dumps(fields, ensure_ascii=False) + " " + args.title
    masked = cap.redact_text(blob)
    if masked != blob and not getattr(args, "allow_secretish", False):
        print(red("REFUSED: this entry looks like it carries a credential."))
        print("Reference the config by path instead (e.g. 'see .env: SHOPIFY_TOKEN').")
        print("Override with --allow-secretish only if you are certain it is not one.")
        return 2

    ev = {
        "kind": "narrative",
        "trigger": trigger,
        "entry": entry_id,
        "summary": args.title,
        "actor": {"kind": "agent" if os.environ.get("CLAUDE_SESSION_ID") else "human",
                  "harness": os.environ.get("CHRONICLE_HARNESS", "cli"),
                  "session": _session(),
                  "model": os.environ.get("CHRONICLE_MODEL", "")},
        "cwd": cwd,
    }
    ev.update(fields)
    git = cap.git_head(cwd)
    if git:
        ev["git"] = {k: v for k, v in git.items() if k != "root"}
    if getattr(args, "stdin", False) and not sys.stdin.isatty():
        body = sys.stdin.read().strip()
        if body:
            ev["body"] = body

    eid = cap.emit(ev, cwd, _session())
    _append_md(cwd, entry_id, trigger, args.title, fields)

    # An ARM is what the gate looks for. Registered separately from the lane so the gate
    # can answer "is this covered?" in microseconds inside a PreToolUse hook, without
    # scanning a ledger that grows forever.
    if trigger == "ARM":
        import time as _time
        cap.record_arm({
            "at": _time.time(), "entry": entry_id, "session": _session(),
            "title": args.title, "restore": args.restore,
            "class": getattr(args, "klass", None), "cwd": cwd,
        })

    # A narrative entry resets the nudge counters — the agent just did the thing the
    # nudge exists to provoke.
    st = cap.state_load(_session())
    for key in ("events", "file_writes", "output_bytes"):
        st[key] = 0
    st["last_narrative"] = cap.now_iso()
    st["last_trigger"] = trigger
    cap.state_save(_session(), st)

    colour = {"ARM": red, "LANDED": green, "DECISION": cyan, "OPEN": blue,
              "CLOSE": yellow, "EXPERIMENT": cyan, "ABANDONED": yellow}.get(trigger, dim)
    print(f"{colour(trigger):>8}  {bold(entry_id)}  {args.title}")
    if trigger == "ARM":
        print(dim(f"          restore: {args.restore}"))
    print(dim(f"          event {eid}"))
    return 0


def cmd_correct(args) -> int:
    cwd = os.getcwd()
    conn = _conn()
    hit = conn.execute(
        "SELECT id FROM events WHERE raw LIKE ? LIMIT 1", (f'%"entry": "{args.target}"%',)
    ).fetchone()
    if not hit:
        print(red(f"no entry with id {args.target!r} in the record"))
        print(dim("(ids look like 2026-08-06T02:10Z-A3F9; `chron resume` lists them)"))
        return 1
    entry_id = _entry_id()
    ev = {
        "kind": "narrative", "trigger": "CORRECTION", "entry": entry_id,
        "corrects": args.target, "summary": args.what_was_wrong,
        "truth": args.truth, "evidence": args.evidence,
        "actor": {"kind": "human", "harness": "cli", "session": _session()},
        "cwd": cwd,
    }
    ev = {k: v for k, v in ev.items() if v is not None}
    eid = cap.emit(ev, cwd, _session())
    _append_md(cwd, entry_id, "CORRECTION", f"supersedes [{args.target}]",
               {"what": args.what_was_wrong, "why": args.truth,
                "verified": [args.evidence] if args.evidence else []})
    print(f"{red('CORRECTION'):>8}  {bold(entry_id)}  supersedes {args.target}")
    print(dim(f"          event {eid}"))
    return 0


# ── read verbs ───────────────────────────────────────────────────────────────

def cmd_resume(args) -> int:
    """The read-back. Optimised for what a fresh session does not already know."""
    conn = _conn()
    project = _project(args)
    session = _session()

    total = conn.execute("SELECT COUNT(*) n FROM events").fetchone()["n"]
    if not total:
        print(yellow("The ledger is empty."))
        print("Capture may not be installed here. Run: " + bold("chron install-hooks"))
        return 1

    scope = project or "all projects"
    print(f"{bold('CHRONICLE')}  {cyan(scope)}  {dim(f'{total:,} events indexed')}")

    delta = idx.since_last_session(conn, project, session)
    if delta["events"]:
        print()
        print(rule("since you were last here"))
        who = ", ".join(delta["sessions"][:4]) or "?"
        print(f"  {bold(str(delta['events']))} events "
              f"from {len(delta['sessions'])} other session(s) "
              f"on {', '.join(delta['machines']) or '?'}")
        if delta["commits"]:
            print(f"  {bold(str(len(delta['commits'])))} commit(s):")
            for msg in delta["commits"][:6]:
                print(f"    {dim('·')} {msg[:88]}")
        if delta["files"]:
            print(f"  {bold(str(len(delta['files'])))} file(s) touched; most recent:")
            for path in delta["files"][-8:]:
                print(f"    {dim('·')} {_short(path)}")

    labels = idx.state_labels(conn, project)
    if labels:
        print()
        print(rule("declared state — INTENTIONAL vs BUG"))
        for _eid, ts, label in labels[:6]:
            print(f"  {green('▸')} {label}")
            print(f"    {dim(_ago(ts))}")

    arm = idx.last_arm(conn, project)
    if arm:
        stood_down = any(e.raw.get("resolves") and arm.raw.get("entry") in e.raw["resolves"]
                         for e in idx.narrative(conn, project, limit=200))
        print()
        print(rule("most recent ARM (destructive operation)"))
        mark = green("stood down") if stood_down else red("NOT stood down")
        print(f"  {arm.summary}  {dim('·')} {mark} {dim('·')} {dim(_ago(arm.ts))}")
        if arm.raw.get("restore"):
            print(f"    restore: {cyan(arm.raw['restore'])}")

    questions = idx.open_questions(conn, project)
    if questions:
        print()
        print(rule(f"{len(questions)} unresolved OPEN question(s) — the handover"))
        for _eid, ts, q in questions[:10]:
            print(f"  {yellow('?')} {q}  {dim(_ago(ts))}")

    entries = idx.narrative(conn, project, limit=args.n)
    if entries:
        print()
        if any(e.inferred for e in entries):
            # Stated once, prominently, before any inferred entry is read — not as a
            # per-line suffix a reader's eye learns to skip.
            print(red("  ⚠ entries marked ~inferred were written by a model reading the "
                      "trace after the fact."))
            print(red("    They were NOT witnessed and MAY BE WRONG. Check their anchored "
                      "events before acting;"))
            print(red("    where they conflict with a first-hand entry, the first-hand "
                      "entry wins."))
            print()
        print(rule(f"last {len(entries)} narrative entries"))
        corrected = {e.raw.get("corrects") for e in entries if e.raw.get("corrects")}
        for ev in entries:
            trig = ev.trigger or "NOTE"
            colour = {"ARM": red, "LANDED": green, "DECISION": cyan,
                      "OPEN": blue, "CLOSE": yellow, "CORRECTION": red}.get(trig, dim)
            flags = ""
            if ev.raw.get("entry") in corrected:
                flags += red("  ⚠ CORRECTED")
            if ev.inferred:
                flags += dim("  ~inferred")
            print(f"  {colour(trig.ljust(10))} {ev.summary}{flags}")
            print(f"    {dim(ev.raw.get('entry', ev.id))}  {dim(_ago(ts_of(ev)))}")
            for key, label in (("intent", "intent"), ("state", "state"),
                               ("not_done", "NOT done")):
                if ev.raw.get(key):
                    print(f"    {dim(label + ':')} {ev.raw[key]}")
    else:
        print()
        print(yellow("No narrative entries yet — the trace is being captured, but nobody "
                     "has said why."))
        print("Start with: " + bold('chron open "<what you are picking up>" '
                                    '--state "<what is intentional here>"'))

    print()
    print(dim("verify with `chron doctor` · reconstruct with `chron show <path> --at <ts>`"))
    return 0


def ts_of(ev) -> str:
    return ev.ts


def _short(path: str, width: int = 78) -> str:
    if len(path) <= width:
        return path
    return "…" + path[-(width - 1):]


def cmd_show(args) -> int:
    conn = _conn()
    at = _resolve_at(args.at)
    found = idx.version_at(conn, args.path, at)
    if not found:
        print(red(f"no recorded version of {args.path} at or before {at}"))
        vers = idx.file_versions(conn, args.path)
        if vers:
            print(dim(f"(earliest record is {vers[0]['ts']})"))
        return 1
    digest, row = found
    if not digest:
        print(red("that version was recorded but its content was not stored "
                  "(redacted, oversize, or binary)"))
        return 1
    try:
        data = cap.cas_get(digest)
    except KeyError:
        print(red(f"content {digest} is not in this machine's store"))
        print(dim("run `chron sync` to pull blobs from the spine"))
        return 1
    sys.stdout.write(data.decode("utf-8", "replace"))
    if sys.stderr.isatty():
        print(f"\n{dim('── ' + row['path'] + ' as of ' + row['ts'] + ' · ' + digest[:19])}",
              file=sys.stderr)
    return 0


def cmd_history(args) -> int:
    conn = _conn()
    rows = idx.file_versions(conn, args.path)
    if not rows:
        print(red(f"no record of {args.path}"))
        return 1
    print(f"{bold(args.path)}  {dim(f'{len(rows)} recorded touches')}")
    print()
    prev = None
    for r in rows:
        digest = r["after"] or r["before"] or ""
        changed = "" if digest == prev else green(" ●")
        prev = digest
        actor = r["actor"] or "?"
        mark = dim(digest[7:15]) if digest else red("not stored")
        print(f"  {r['ts']}  {mark}{changed}  {dim(actor)}  {r['summary'][:56]}")
    print()
    print(dim("chron show <path> --at <ts>   ·   chron diff <path> --from <ts> --to <ts>"))
    return 0


def cmd_diff(args) -> int:
    import difflib
    conn = _conn()
    a = idx.version_at(conn, args.path, _resolve_at(args.frm))
    b = idx.version_at(conn, args.path, _resolve_at(args.to))
    if not a or not b:
        print(red("one or both versions are not in the record"))
        return 1
    try:
        left = cap.cas_get(a[0]).decode("utf-8", "replace").splitlines(keepends=True)
        right = cap.cas_get(b[0]).decode("utf-8", "replace").splitlines(keepends=True)
    except KeyError as exc:
        print(red(f"content {exc} not in this machine's store; run `chron sync`"))
        return 1
    for line in difflib.unified_diff(left, right,
                                     fromfile=f"{args.path}@{a[1]['ts']}",
                                     tofile=f"{args.path}@{b[1]['ts']}"):
        if line.startswith("+") and not line.startswith("+++"):
            sys.stdout.write(green(line.rstrip()) + "\n")
        elif line.startswith("-") and not line.startswith("---"):
            sys.stdout.write(red(line.rstrip()) + "\n")
        else:
            sys.stdout.write(line if line.endswith("\n") else line + "\n")
    return 0


def cmd_restore(args) -> int:
    conn = _conn()
    found = idx.version_at(conn, args.path, _resolve_at(args.at))
    if not found:
        print(red("no such version in the record"))
        return 1
    digest, row = found
    try:
        data = cap.cas_get(digest)
    except KeyError:
        print(red("content not in this machine's store; run `chron sync`"))
        return 1
    dest = Path(args.to or args.path)
    if dest.exists() and not args.force:
        print(red(f"{dest} exists. Pass --force to overwrite, or --to <other path>."))
        return 2
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    print(f"{green('restored')} {dest}  {dim('from ' + row['ts'] + ' · ' + digest[:19])}")
    return 0


def cmd_day(args) -> int:
    conn = _conn()
    summary = idx.day_summary(conn, args.date)
    if not summary["events"]:
        print(yellow(f"nothing recorded on {args.date}"))
        return 1
    print(f"{bold(args.date)}  {summary['events']:,} events  "
          f"{dim(summary['first'][11:16] + ' → ' + summary['last'][11:16] + ' UTC')}")
    print()
    print(rule("by project"))
    for proj, n in sorted(summary["by_project"].items(), key=lambda kv: -kv[1]):
        print(f"  {str(n).rjust(6)}  {proj}")
    print()
    print(rule("by kind"))
    for kind, n in sorted(summary["by_kind"].items(), key=lambda kv: -kv[1]):
        print(f"  {str(n).rjust(6)}  {kind}")
    if summary["narrative"]:
        print()
        print(rule("narrative"))
        for ev in summary["narrative"]:
            print(f"  {(ev.trigger or 'NOTE').ljust(10)} {ev.summary}")
    print()
    print(rule(f"{len(summary['files'])} files touched"))
    for path, proj in summary["files"][:40]:
        print(f"  {dim((proj or '?').ljust(16))} {_short(path, 60)}")
    if len(summary["files"]) > 40:
        print(dim(f"  … and {len(summary['files']) - 40} more"))
    return 0


def cmd_search(args) -> int:
    conn = _conn()
    hits = idx.search(conn, args.term, limit=args.n)
    if not hits:
        print(yellow(f"no match for {args.term!r}"))
        return 1
    for ev in hits:
        trig = ev.trigger or ev.kind
        print(f"  {dim(ev.ts[:16])}  {cyan(trig.ljust(12))} {ev.summary[:70]}")
        print(f"    {dim(ev.project)}  {dim(ev.id)}")
    print()
    print(f"{len(hits)} match(es)")
    return 0


def cmd_why(args) -> int:
    """Why does this file look like this — the narrative that mentions it."""
    conn = _conn()
    hits = idx.touching(conn, args.path)
    if not hits:
        print(yellow(f"no narrative entry references {args.path}"))
        print(dim("the raw trace still has it: chron history " + args.path))
        return 1
    for ev in hits:
        print(f"  {(ev.trigger or 'NOTE').ljust(10)} {ev.summary}"
              + (dim("  ~inferred") if ev.inferred else ""))
        for key in ("intent", "state", "why", "restore"):
            if ev.raw.get(key):
                print(f"    {dim(key + ':')} {ev.raw[key]}")
        print(f"    {dim(ev.raw.get('entry', ev.id))} {dim(_ago(ev.ts))}")
        print()
    return 0


def cmd_files(args) -> int:
    conn = _conn()
    rows = conn.execute(
        "SELECT path, COUNT(*) n, MAX(ts) last, project FROM files "
        "GROUP BY path ORDER BY last DESC LIMIT ?", (args.n,))
    for r in rows:
        print(f"  {dim(r['last'][:16])}  {str(r['n']).rjust(4)}×  "
              f"{dim((r['project'] or '?').ljust(14))} {_short(r['path'], 60)}")
    return 0


def cmd_doctor(args) -> int:
    """Is the record trustworthy right now? Answers loudly rather than reassuringly."""
    problems: list[str] = []
    notes: list[str] = []

    home = Path(cap.CHRON_HOME)
    print(f"{bold('chronicle doctor')}  {dim(str(home))}")
    print()

    hooks = _installed_hooks()
    if hooks:
        notes.append(f"capture hooks installed for: {', '.join(hooks)}")
    else:
        problems.append("NO capture hooks installed — nothing is being recorded "
                        "(fix: chron install-hooks)")

    if cap.capture_disabled():
        problems.append("capture is SUSPENDED (chron on, to resume)")

    conn = _conn()
    total = conn.execute("SELECT COUNT(*) n FROM events").fetchone()["n"]
    notes.append(f"{total:,} events indexed across "
                 f"{len(idx.discover_lanes())} lane(s)")

    row = conn.execute("SELECT MAX(ts) t FROM events").fetchone()
    if row and row["t"]:
        notes.append(f"most recent event {_ago(row['t'])}")
        try:
            last = datetime.fromisoformat(row["t"].replace("Z", "+00:00"))
            if datetime.now(timezone.utc) - last > timedelta(hours=12):
                problems.append("no events for over 12 hours — capture may be broken")
        except Exception:
            pass

    # Blob integrity on a sample. Verifying every blob would make `doctor` too slow to
    # run habitually, and a check nobody runs is worth nothing.
    sample = [r["after"] for r in conn.execute(
        "SELECT after FROM files WHERE after<>'' ORDER BY ts DESC LIMIT 200")]
    bad, missing = [], []
    for digest in sample:
        try:
            if not cap.cas_verify(digest):
                bad.append(digest)
        except Exception:
            missing.append(digest)
    if bad:
        problems.append(f"{len(bad)} blob(s) FAILED hash verification — the store has "
                        "been altered")
    if missing:
        notes.append(f"{len(missing)}/{len(sample)} sampled blobs not on this machine "
                     "(normal before `chron sync`)")
    if sample and not bad and not missing:
        notes.append(f"all {len(sample)} sampled blobs verify against their hashes")

    errlog = home / "errors.log"
    if errlog.exists():
        lines = errlog.read_text(errors="replace").strip().splitlines()
        if lines:
            recent_errs = lines[-3:]
            problems.append(f"{len(lines)} capture error(s) logged; most recent: "
                            + recent_errs[-1][:100])

    quarantine = home / "quarantine.jsonl"
    if quarantine.exists() and quarantine.stat().st_size:
        problems.append("events are in quarantine — a lane was unwritable "
                        f"({quarantine})")

    for note in notes:
        print(f"  {green('ok')}   {note}")
    for prob in problems:
        print(f"  {red('!!')}   {prob}")
    print()
    if problems:
        print(red(f"{len(problems)} problem(s)"))
        return 3
    print(green("the record is healthy"))
    return 0


def cmd_stats(args) -> int:
    conn = _conn()
    home = Path(cap.CHRON_HOME)
    cas = home / "cas"
    nblobs = sum(1 for _ in cas.rglob("*")) if cas.exists() else 0
    size = sum(p.stat().st_size for p in cas.rglob("*") if p.is_file()) if cas.exists() else 0
    rows = conn.execute("SELECT kind, COUNT(*) n FROM events GROUP BY kind ORDER BY n DESC")
    print(f"{bold('ledger')}")
    for r in rows:
        print(f"  {str(r['n']).rjust(8)}  {r['kind']}")
    uniq = conn.execute("SELECT COUNT(DISTINCT path) n FROM files").fetchone()["n"]
    print()
    print(f"  {str(uniq).rjust(8)}  distinct files")
    print(f"  {str(nblobs).rjust(8)}  blobs  {dim(f'{size / 1e6:.1f} MB on disk')}")
    return 0


def cmd_off(args) -> int:
    Path(cap.CHRON_HOME).mkdir(parents=True, exist_ok=True)
    (Path(cap.CHRON_HOME) / "OFF").write_text(cap.now_iso())
    cap.emit({"kind": "note", "summary": "capture SUSPENDED via `chron off`",
              "actor": {"kind": "human", "harness": "cli", "session": "cli"}},
             os.getcwd(), "cli")
    print(yellow("capture suspended.") + " Resume with " + bold("chron on"))
    return 0


def cmd_on(args) -> int:
    sentinel = Path(cap.CHRON_HOME) / "OFF"
    if sentinel.exists():
        sentinel.unlink()
    cap.emit({"kind": "note", "summary": "capture RESUMED via `chron on`",
              "actor": {"kind": "human", "harness": "cli", "session": "cli"}},
             os.getcwd(), "cli")
    print(green("capture resumed."))
    return 0


def _installed_hooks() -> list[str]:
    out = []
    settings = Path.home() / ".claude" / "settings.json"
    try:
        data = json.loads(settings.read_text())
        blob = json.dumps(data.get("hooks", {}))
        if "chronicle" in blob:
            out.append("claude-code")
    except Exception:
        pass
    zshrc = Path.home() / ".zshrc"
    try:
        if "chronicle" in zshrc.read_text():
            out.append("shell")
    except Exception:
        pass
    return out


def _resolve_at(value: str | None) -> str:
    """Accept an ISO instant, a date, 'now', or a relative like '2h'/'3d'."""
    if not value or value == "now":
        return cap.now_iso()
    v = value.strip()
    if v and v[-1] in "smhd" and v[:-1].replace(".", "").isdigit():
        mult = {"s": 1, "m": 60, "h": 3600, "d": 86400}[v[-1]]
        when = datetime.now(timezone.utc) - timedelta(seconds=float(v[:-1]) * mult)
        return when.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    if len(v) == 10:                      # a bare date means end of that day
        return v + "T23:59:59.999Z"
    if not v.endswith("Z"):
        v += "Z"
    return v


# ── parser ───────────────────────────────────────────────────────────────────

def _add_write_args(p, trigger: str):
    p.add_argument("title")
    p.add_argument("--intent", help="what you MEANT to do")
    p.add_argument("--state", help="anti-ambiguity: 'EN in base fields is INTENTIONAL staging, not a bug'")
    p.add_argument("--what", help="what actually changed")
    p.add_argument("--why", help="why it changed")
    p.add_argument("--ext", action="append", metavar="K=V",
                   help="external state git cannot version (url, image tag, resource id). repeatable")
    p.add_argument("--class", dest="klass", choices=sorted(CLASSES), help="reversibility class")
    p.add_argument("--restore", help="the command or artifact that gets you back")
    p.add_argument("--verified", action="append", help="what you checked and how. repeatable")
    p.add_argument("--not-done", dest="not_done", help="what you deliberately did NOT do")
    p.add_argument("--open", action="append", help="open question left behind. repeatable")
    p.add_argument("--resolves", action="append", help="entry id or question this closes. repeatable")
    p.add_argument("--hypothesis", help="EXPERIMENT: what you expected it to show")
    p.add_argument("--setup", help="EXPERIMENT: exactly what was run — command, config, data, scale")
    p.add_argument("--varied", help="EXPERIMENT: what changed since the previous attempt")
    p.add_argument("--result", help="EXPERIMENT: what actually happened — real measured numbers")
    p.add_argument("--conclusion", help="EXPERIMENT: what was learned")
    p.add_argument("--outcome", choices=["kept", "abandoned", "inconclusive", "superseded"],
                   help="EXPERIMENT: what became of it")
    p.add_argument("--stdin", action="store_true", help="read a free-form body from stdin")
    p.add_argument("--allow-secretish", action="store_true")
    p.set_defaults(fn=cmd_write, _trigger=trigger)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="chron",
        description="The continuous work ledger. Capture is automatic; this is for intent.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="write verbs:\n" + "\n".join(f"  {k.lower():10s} {v}" for k, v in TRIGGERS.items()))
    sub = p.add_subparsers(dest="cmd", required=True)

    for trigger in ("OPEN", "ARM", "DECISION", "LANDED", "CLOSE", "NOTE",
                    "EXPERIMENT", "ABANDONED"):
        sp = sub.add_parser(trigger.lower(), help=TRIGGERS[trigger])
        _add_write_args(sp, trigger)

    cp = sub.add_parser("correct", help="append a correction to a past entry")
    cp.add_argument("target")
    cp.add_argument("what_was_wrong")
    cp.add_argument("--truth")
    cp.add_argument("--evidence")
    cp.set_defaults(fn=cmd_correct)

    rp = sub.add_parser("resume", help="read yourself back into true state (START HERE)")
    rp.add_argument("-n", type=int, default=6, help="narrative entries to show")
    rp.add_argument("--project")
    rp.add_argument("--all", action="store_true", help="across all projects")
    rp.set_defaults(fn=cmd_resume)

    sp = sub.add_parser("show", help="a file's exact content at a past moment")
    sp.add_argument("path")
    sp.add_argument("--at", default="now", help="ISO instant, date, or relative like 2h/3d")
    sp.set_defaults(fn=cmd_show)

    hp = sub.add_parser("history", help="every recorded version of a file")
    hp.add_argument("path")
    hp.set_defaults(fn=cmd_history)

    dp = sub.add_parser("diff", help="diff a file between two moments")
    dp.add_argument("path")
    dp.add_argument("--from", dest="frm", required=True)
    dp.add_argument("--to", required=True)
    dp.set_defaults(fn=cmd_diff)

    rsp = sub.add_parser("restore", help="materialise a past version to disk")
    rsp.add_argument("path")
    rsp.add_argument("--at", default="now")
    rsp.add_argument("--to")
    rsp.add_argument("--force", action="store_true")
    rsp.set_defaults(fn=cmd_restore)

    dyp = sub.add_parser("day", help="everything that happened on a date")
    dyp.add_argument("date", help="YYYY-MM-DD")
    dyp.set_defaults(fn=cmd_day)

    sep = sub.add_parser("search", help="search the whole record")
    sep.add_argument("term")
    sep.add_argument("-n", type=int, default=40)
    sep.set_defaults(fn=cmd_search)

    wp = sub.add_parser("why", help="narrative entries that explain a file")
    wp.add_argument("path")
    wp.set_defaults(fn=cmd_why)

    fp = sub.add_parser("files", help="recently touched files")
    fp.add_argument("-n", type=int, default=40)
    fp.set_defaults(fn=cmd_files)

    sub.add_parser("doctor", help="is the record trustworthy right now?").set_defaults(fn=cmd_doctor)
    sub.add_parser("stats", help="ledger size and composition").set_defaults(fn=cmd_stats)
    sub.add_parser("off", help="suspend capture (records that it was suspended)").set_defaults(fn=cmd_off)
    sub.add_parser("on", help="resume capture").set_defaults(fn=cmd_on)

    ip = sub.add_parser("install-hooks", help="wire capture into this machine")
    ip.add_argument("--machine", help="install on a remote host over ssh")
    ip.add_argument("--shell", action="store_true", help="also install the zsh hook")
    ip.add_argument("--git", action="store_true", help="also install git hooks in registered repos")
    ip.add_argument("--trust-codex", action="store_true", dest="trust_codex",
                    help="deprecated: refuses; approve hooks interactively in your host")
    ip.add_argument("--codex", action="store_true",
                    help="stage experimental Codex hooks; host approval and verification required")
    ip.add_argument("--claude", action="store_true",
                    help="with --machine: merge chronicle hooks into the remote settings.json")
    ip.add_argument("--dry-run", action="store_true")
    ip.set_defaults(fn=_lazy("install", "cmd_install_hooks"))

    syp = sub.add_parser("sync", help="exchange lanes and blobs with the spine")
    syp.add_argument("--spine", help="override spine path")
    syp.add_argument("--pull-only", action="store_true")
    syp.add_argument("--push-only", action="store_true")
    syp.add_argument("--commit", action="store_true",
                     help="commit the spine to its git repo after syncing")
    syp.set_defaults(fn=_lazy("spine", "cmd_sync"))

    sub.add_parser("crypto-setup",
                   help="check/print how to configure age recipients for the spine"
                   ).set_defaults(fn=_lazy("spine", "cmd_crypto_setup"))

    np = sub.add_parser("narrate", help="run the background narrator over recent work")
    np.add_argument("--session", help="narrate one session (default: the most recent)")
    np.add_argument("--since", help="narrate everything since an instant")
    np.add_argument("--dry-run", action="store_true")
    np.set_defaults(fn=_lazy("narrate", "cmd_narrate"))

    cvp = sub.add_parser("canvas", help="serve the canvas")
    cvp.add_argument("--port", type=int, default=8899)
    cvp.add_argument("--host", default="127.0.0.1")
    cvp.add_argument("--open", action="store_true", dest="open_browser")
    cvp.set_defaults(fn=_lazy("canvas.server", "cmd_canvas"))

    return p


def _lazy(module: str, func: str):
    """Import optional subsystems only when their verb is used.

    `chron resume` must not pay for FastAPI being installed, and must still work on a box
    where it is not.
    """
    def run(args):
        import importlib
        try:
            mod = importlib.import_module(f"chronicle.{module}")
        except ImportError:
            sys.path.insert(0, str(Path(__file__).parent.parent))
            try:
                mod = importlib.import_module(f"chronicle.{module}")
            except ImportError as exc:
                print(red(f"this command needs the {module} subsystem: {exc}"))
                return 4
        return getattr(mod, func)(args)
    return run


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return args.fn(args) or 0
    except BrokenPipeError:
        return 0
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    sys.exit(main())
