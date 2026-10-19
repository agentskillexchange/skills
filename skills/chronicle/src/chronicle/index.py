"""Derived index over the lanes.

The lanes are the truth; this file is a cache that can be deleted at any time and
rebuilt from them. Nothing here may ever be the only copy of anything.

Indexing is INCREMENTAL by byte offset: a lane is an append-only file, so the bytes
before the last recorded offset can never change. Re-reading a 200 MB ledger on every
`chron resume` would make the read-back expensive, and an expensive read-back is one
that agents skip — which is the failure v1 died of, one layer up.
"""
from __future__ import annotations

import json
import os
import sqlite3
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator

sys.path.insert(0, str(Path(__file__).parent))
import capture as cap  # noqa: E402  (single-file, stdlib-only capture core)

SCHEMA = """
CREATE TABLE IF NOT EXISTS events (
    id        TEXT PRIMARY KEY,
    ts        TEXT NOT NULL,
    machine   TEXT,
    project   TEXT,
    cwd       TEXT,
    kind      TEXT,
    trigger   TEXT,
    summary   TEXT,
    actor     TEXT,
    harness   TEXT,
    session   TEXT,
    model     TEXT,
    git_sha   TEXT,
    git_branch TEXT,
    inferred  INTEGER DEFAULT 0,
    raw       TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS ix_events_ts      ON events(ts);
CREATE INDEX IF NOT EXISTS ix_events_project ON events(project, ts);
CREATE INDEX IF NOT EXISTS ix_events_kind    ON events(kind, ts);
CREATE INDEX IF NOT EXISTS ix_events_session ON events(session, ts);

CREATE TABLE IF NOT EXISTS files (
    event_id TEXT NOT NULL,
    ts       TEXT NOT NULL,
    path     TEXT NOT NULL,
    before   TEXT,
    after    TEXT,
    project  TEXT,
    redacted INTEGER DEFAULT 0
);
CREATE INDEX IF NOT EXISTS ix_files_path ON files(path, ts);
CREATE INDEX IF NOT EXISTS ix_files_ts   ON files(ts);

CREATE TABLE IF NOT EXISTS lanes (
    path   TEXT PRIMARY KEY,
    offset INTEGER NOT NULL,
    mtime  REAL
);
"""


@dataclass
class Event:
    id: str
    ts: str
    machine: str
    project: str
    kind: str
    summary: str
    raw: dict

    @property
    def trigger(self) -> str:
        return self.raw.get("trigger") or ""

    @property
    def inferred(self) -> bool:
        return bool(self.raw.get("inferred"))

    @property
    def actor_kind(self) -> str:
        return (self.raw.get("actor") or {}).get("kind") or "?"

    @property
    def session(self) -> str:
        return (self.raw.get("actor") or {}).get("session") or ""


def index_path() -> Path:
    return Path(cap.CHRON_HOME) / "index.sqlite"


def connect(path: Path | None = None) -> sqlite3.Connection:
    p = path or index_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(p))
    conn.row_factory = sqlite3.Row
    # WAL lets a canvas read while a hook-driven refresh writes.
    conn.execute("PRAGMA journal_mode=WAL")
    conn.executescript(SCHEMA)
    return conn


# ── lane discovery ───────────────────────────────────────────────────────────

def discover_lanes(roots: Iterable[str] | None = None) -> list[Path]:
    """Every lane this machine can see: home lanes, spine lanes, and repo lanes.

    Repo lanes are found by scanning the registered project roots rather than the whole
    filesystem — an unbounded scan of $HOME is the kind of thing that makes a tool feel
    slow and unpredictable.
    """
    found: list[Path] = []
    home = Path(cap.CHRON_HOME)
    for base in (home / "lanes", home / "spine" / "events"):
        if base.exists():
            found.extend(sorted(base.rglob("*.jsonl")))

    for root in roots or registered_roots():
        rp = Path(root).expanduser()
        lanes = rp / ".chronicle" / "lanes"
        if lanes.exists():
            found.extend(sorted(lanes.glob("*.jsonl")))
    q = home / "quarantine.jsonl"
    if q.exists():
        found.append(q)
    return found


def registered_roots() -> list[str]:
    """Project roots chronicle knows about. Registration happens automatically the first
    time a lane is written inside a repo, so this is a cache of observed reality rather
    than something a human has to maintain."""
    reg = Path(cap.CHRON_HOME) / "roots.json"
    try:
        return json.loads(reg.read_text())
    except Exception:
        return []


def register_root(path: str) -> None:
    root = cap.repo_root(path)
    if not root:
        return
    reg = Path(cap.CHRON_HOME) / "roots.json"
    roots = registered_roots()
    if root not in roots:
        roots.append(root)
        reg.parent.mkdir(parents=True, exist_ok=True)
        tmp = reg.with_suffix(".tmp")
        tmp.write_text(json.dumps(sorted(roots), indent=1))
        os.replace(tmp, reg)


# ── refresh ──────────────────────────────────────────────────────────────────

def refresh(conn: sqlite3.Connection, roots: Iterable[str] | None = None) -> int:
    """Pull new bytes from every lane into the index. Returns events added.

    A malformed line is skipped and counted, never fatal: one torn line (the crash-safety
    case) must not make the whole ledger unreadable.
    """
    added = 0
    skipped = 0
    for lane in discover_lanes(roots):
        try:
            stat = lane.stat()
        except OSError:
            continue
        row = conn.execute("SELECT offset FROM lanes WHERE path=?", (str(lane),)).fetchone()
        start = row["offset"] if row else 0
        if stat.st_size < start:
            start = 0          # lane was truncated or replaced: reread it whole
        if stat.st_size == start:
            continue
        try:
            with lane.open("rb") as fh:
                fh.seek(start)
                chunk = fh.read()
        except OSError:
            continue

        # Only consume up to the last complete line; a partial tail stays unread until
        # its writer finishes it.
        cut = chunk.rfind(b"\n")
        if cut < 0:
            continue
        consumed = start + cut + 1
        for line in chunk[: cut + 1].splitlines():
            if not line.strip():
                continue
            try:
                ev = json.loads(line.decode("utf-8", "replace"))
            except Exception:
                skipped += 1
                continue
            if _insert(conn, ev):
                added += 1
        conn.execute(
            "INSERT INTO lanes(path, offset, mtime) VALUES(?,?,?) "
            "ON CONFLICT(path) DO UPDATE SET offset=excluded.offset, mtime=excluded.mtime",
            (str(lane), consumed, stat.st_mtime))
    conn.commit()
    if skipped:
        cap._log_error("index: skipped %d unparseable line(s)" % skipped)
    return added


def _insert(conn: sqlite3.Connection, ev: dict) -> bool:
    eid = ev.get("id")
    if not eid:
        return False
    actor = ev.get("actor") or {}
    git = ev.get("git") or {}
    try:
        conn.execute(
            "INSERT OR IGNORE INTO events"
            "(id,ts,machine,project,cwd,kind,trigger,summary,actor,harness,session,model,"
            " git_sha,git_branch,inferred,raw) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (eid, ev.get("ts", ""), ev.get("machine", ""), ev.get("project", ""),
             ev.get("cwd", ""), ev.get("kind", ""), ev.get("trigger", ""),
             ev.get("summary", ""), actor.get("kind", ""), actor.get("harness", ""),
             actor.get("session", ""), actor.get("model", ""),
             git.get("sha", ""), git.get("branch", ""),
             1 if ev.get("inferred") else 0,
             json.dumps(ev, ensure_ascii=False, sort_keys=True)))
    except sqlite3.Error:
        return False
    if conn.total_changes == 0:
        return False
    for f in ev.get("files") or []:
        if not isinstance(f, dict) or not f.get("path"):
            continue
        conn.execute(
            "INSERT INTO files(event_id,ts,path,before,after,project,redacted) "
            "VALUES(?,?,?,?,?,?,?)",
            (eid, ev.get("ts", ""), f["path"], f.get("before", ""), f.get("after", ""),
             ev.get("project", ""), 1 if f.get("redacted") else 0))
    return True


# ── queries ──────────────────────────────────────────────────────────────────

def _ev(row: sqlite3.Row) -> Event:
    raw = json.loads(row["raw"])
    return Event(row["id"], row["ts"], row["machine"] or "", row["project"] or "",
                 row["kind"] or "", row["summary"] or "", raw)


def recent(conn, limit: int = 40, project: str | None = None,
           kinds: Iterable[str] | None = None) -> list[Event]:
    sql = "SELECT * FROM events WHERE 1=1"
    args: list = []
    if project:
        sql += " AND project=?"
        args.append(project)
    if kinds:
        marks = ",".join("?" * len(list(kinds)))
        sql += f" AND kind IN ({marks})"
        args.extend(kinds)
    sql += " ORDER BY ts DESC, id DESC LIMIT ?"
    args.append(limit)
    return [_ev(r) for r in conn.execute(sql, args)]


def narrative(conn, project: str | None = None, limit: int = 20,
              since: str | None = None) -> list[Event]:
    sql = "SELECT * FROM events WHERE kind='narrative'"
    args: list = []
    if project:
        sql += " AND project=?"
        args.append(project)
    if since:
        sql += " AND ts>=?"
        args.append(since)
    sql += " ORDER BY ts DESC LIMIT ?"
    args.append(limit)
    return [_ev(r) for r in conn.execute(sql, args)]


def open_questions(conn, project: str | None = None) -> list[tuple[str, str, str]]:
    """Unresolved OPEN questions: (event_id, ts, question).

    A question is resolved by a later narrative entry naming it in `resolves`. Everything
    else stays on the handover, forever, which is the point — an open question that ages
    out silently is a trap left for the next agent.
    """
    rows = narrative(conn, project, limit=10_000)
    resolved: set[str] = set()
    for ev in rows:
        for r in ev.raw.get("resolves") or []:
            resolved.add(r)
    out = []
    for ev in sorted(rows, key=lambda e: e.ts):
        for q in ev.raw.get("open") or []:
            key = f"{ev.id}:{q}"
            if key not in resolved and q not in resolved:
                out.append((ev.id, ev.ts, q))
    return out


def last_arm(conn, project: str | None = None) -> Event | None:
    rows = [e for e in narrative(conn, project, limit=500) if e.trigger == "ARM"]
    return rows[0] if rows else None


def state_labels(conn, project: str | None = None) -> list[tuple[str, str, str]]:
    """Explicit INTENTIONAL-vs-BUG rulings. The highest-value field in the record."""
    out = []
    for ev in narrative(conn, project, limit=500):
        st = ev.raw.get("state")
        if st:
            out.append((ev.id, ev.ts, st))
    return out


def file_versions(conn, path: str) -> list[sqlite3.Row]:
    """Every recorded version of a path, oldest first."""
    like = f"%{path}" if not path.startswith("/") else path
    return list(conn.execute(
        "SELECT f.*, e.kind, e.summary, e.machine, e.actor, e.session "
        "FROM files f JOIN events e ON e.id=f.event_id "
        "WHERE f.path=? OR f.path LIKE ? ORDER BY f.ts ASC", (path, like)))


def version_at(conn, path: str, at: str) -> tuple[str, sqlite3.Row] | None:
    """The content hash of `path` as of instant `at`.

    Prefers the `after` hash of the last event at or before `at`. If that event only
    recorded a `before` (a write we saw start but not finish), that is still the last
    known truth and is returned rather than pretending we know nothing.
    """
    rows = file_versions(conn, path)
    best = None
    for r in rows:
        if r["ts"] <= at:
            best = r
        else:
            break
    if best is None:
        # Asked for a moment before our first record: the earliest `before` is what the
        # file looked like then, if we captured one.
        if rows and rows[0]["before"]:
            return rows[0]["before"], rows[0]
        return None
    digest = best["after"] or best["before"]
    if not digest:
        return None
    return digest, best


def search(conn, term: str, limit: int = 60) -> list[Event]:
    like = f"%{term}%"
    rows = conn.execute(
        "SELECT * FROM events WHERE summary LIKE ? OR raw LIKE ? "
        "ORDER BY ts DESC LIMIT ?", (like, like, limit))
    return [_ev(r) for r in rows]


def touching(conn, path: str) -> list[Event]:
    """Narrative entries whose text or files reference this path — `chron why`."""
    base = os.path.basename(path)
    rows = conn.execute(
        "SELECT DISTINCT e.* FROM events e LEFT JOIN files f ON f.event_id=e.id "
        "WHERE e.kind='narrative' AND (e.raw LIKE ? OR f.path LIKE ?) "
        "ORDER BY e.ts DESC LIMIT 40", (f"%{base}%", f"%{base}%"))
    return [_ev(r) for r in rows]


def day_summary(conn, date: str) -> dict:
    """Everything that happened on a UTC date, across all projects."""
    lo, hi = date + "T00:00", date + "T23:59:59.999Z"
    rows = list(conn.execute(
        "SELECT * FROM events WHERE ts>=? AND ts<=? ORDER BY ts ASC", (lo, hi)))
    files = list(conn.execute(
        "SELECT DISTINCT path, project FROM files WHERE ts>=? AND ts<=?", (lo, hi)))
    by_project: dict[str, int] = {}
    by_kind: dict[str, int] = {}
    for r in rows:
        by_project[r["project"] or "?"] = by_project.get(r["project"] or "?", 0) + 1
        by_kind[r["kind"] or "?"] = by_kind.get(r["kind"] or "?", 0) + 1
    return {
        "date": date,
        "events": len(rows),
        "files": [(f["path"], f["project"]) for f in files],
        "by_project": by_project,
        "by_kind": by_kind,
        "narrative": [_ev(r) for r in rows if r["kind"] == "narrative"],
        "first": rows[0]["ts"] if rows else None,
        "last": rows[-1]["ts"] if rows else None,
    }


def since_last_session(conn, project: str | None, session: str) -> dict:
    """What changed while this session was away.

    Deliberately scoped to *other* actors: the value of a read-back is learning what you
    did not already know, not being shown your own last hour.
    """
    row = conn.execute(
        "SELECT MAX(ts) AS ts FROM events WHERE session=? AND kind='session.end'",
        (session,)).fetchone()
    anchor = row["ts"] if row and row["ts"] else None
    if not anchor:
        row = conn.execute(
            "SELECT MAX(ts) AS ts FROM events WHERE kind='narrative'").fetchone()
        anchor = row["ts"] if row and row["ts"] else "0000"
    sql = "SELECT * FROM events WHERE ts>? AND session<>?"
    args: list = [anchor, session]
    if project:
        sql += " AND project=?"
        args.append(project)
    rows = list(conn.execute(sql + " ORDER BY ts ASC", args))
    return {
        "anchor": anchor,
        "events": len(rows),
        "sessions": sorted({r["session"] for r in rows if r["session"]}),
        "machines": sorted({r["machine"] for r in rows if r["machine"]}),
        "files": sorted({r["path"] for r in conn.execute(
            "SELECT DISTINCT path FROM files WHERE ts>?", (anchor,))}),
        "commits": [r["summary"] for r in rows if r["kind"] == "git.commit"],
    }
