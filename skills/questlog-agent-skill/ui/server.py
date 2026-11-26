#!/usr/bin/env python3
"""Local Questlog cockpit and Markdown ledger. No external actions or adapters enabled."""

import json
import os
import re
import subprocess
import threading
import hashlib
import fcntl
import tempfile
from datetime import date, datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

REPO = Path(os.environ.get("QUESTLOG_ROOT", "./.questlog")).expanduser().resolve()
LEDGER = REPO / "LEDGER.md"
BRIEF_LOGS = REPO / ".brief-logs"
INDEX = (Path(__file__).resolve().parent / "index.html").read_bytes()
BAR = (Path(__file__).resolve().parent / "bar.html").read_bytes()
QUICKADD = (Path(__file__).resolve().parent / "quickadd.html").read_bytes()

# Action execution is deliberately excluded from the public runtime.
QUEUE = REPO / "queue"
Q_PENDING = QUEUE / "pending"
Q_DONE = QUEUE / "done"
CAPTURE_LOCK = threading.Lock()
REQUEST = threading.local()

def enqueue_action(slug, text, **kwargs):
    """Save a local instruction only. No runner is supplied or launched."""
    import uuid
    if not isinstance(text, str) or not text.strip():
        return None, "non-empty text required"
    aid = uuid.uuid4().hex
    Q_PENDING.mkdir(parents=True, exist_ok=True, mode=0o700)
    record = {"id": aid, "slug": re.sub(r"[^a-z0-9._-]", "", str(slug or "general"))[:64],
              "text": " ".join(text.split())[:1000], "status": "pending",
              "created": datetime.now().isoformat(timespec="seconds")}
    _atomic_write(Q_PENDING / (aid + ".json"), json.dumps(record))
    return aid, None

def read_queue(limit_done=12):
    pending = []
    for path in sorted(Q_PENDING.glob("*.json")):
        try:
            record = json.loads(path.read_text())
            if isinstance(record, dict):
                pending.append(record)
        except (OSError, ValueError):
            pass
    return {"pending": pending, "done": []}

WS_RE = re.compile(r"^## ([a-z0-9][a-z0-9._-]*)\s+\[(work|research|life|forge|client)\]\s+\[(hot|warm|paused|blocked|ember)\]\s*$")
DUE_RE = re.compile(r"^DUE: (\d{4}-\d{2}-\d{2}) (.+?)\s+\[(hard|soft)\]\s*$")
WAIT_RE = re.compile(r"^WAITING: (.+?) — (.+?) — since (\d{4}-\d{2}-\d{2}) — chase (\d+)d\s*$")


def parse_ledger(text):
    state = {"updated": None, "season": None, "now": None, "inbox": [], "workstreams": []}
    section = None
    ws = None
    for line in text.splitlines():
        m = re.match(r"^# LEDGER — updated (.+)$", line)
        if m:
            state["updated"] = m.group(1).strip()
            continue
        if line.startswith("SEASON:"):
            state["season"] = line[7:].strip()
            continue
        if re.match(r"^## NOW\s*$", line):
            section, ws = "now", None
            continue
        if re.match(r"^## INBOX\s*$", line):
            section, ws = "inbox", None
            continue
        m = WS_RE.match(line)
        if m:
            ws = {"slug": m.group(1), "domain": m.group(2), "state": m.group(3),
                  "goal": None, "next": None, "dues": [], "waitings": [], "notes": [], "tasks": []}
            state["workstreams"].append(ws)
            section = "ws"
            continue
        if line.startswith("## "):  # unknown H2 — ignore contents
            section, ws = None, None
            continue

        if section == "now" and line.strip() and state["now"] is None:
            state["now"] = line.strip()
        elif section == "inbox" and line.startswith("- "):
            state["inbox"].append(line[2:].strip())
        elif section == "ws" and ws is not None:
            if line.startswith("GOAL:"):
                ws["goal"] = line[5:].strip()
            elif line.startswith("NEXT:"):
                ws["next"] = line[5:].strip()
            elif line.startswith("NOTE:"):
                ws["notes"].append(line[5:].strip())
            elif re.match(r"^(\s*)- \[( |x)\] ", line):
                tm = re.match(r"^(\s*)- \[( |x)\] (.+)$", line)
                ws["tasks"].append({"text": tm.group(3).strip(), "done": tm.group(2) == "x",
                                    "depth": len(tm.group(1)) // 2})
            else:
                m = DUE_RE.match(line)
                if m:
                    ws["dues"].append({"date": m.group(1), "what": m.group(2), "kind": m.group(3)})
                    continue
                m = WAIT_RE.match(line)
                if m:
                    since = m.group(3)
                    chase = int(m.group(4))
                    days = (date.today() - date.fromisoformat(since)).days
                    ws["waitings"].append({"who": m.group(1), "what": m.group(2), "since": since,
                                           "chase_days": chase, "days_waiting": days,
                                           "overdue_by": max(0, days - chase)})
    return state


def pulse_health():
    return {"configured": False, "crontab": [], "logs": {}}


def git(*args):
    """Explicit local journal only; never remote operations or arbitrary hooks."""
    environment = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    environment.update(GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1", GIT_OPTIONAL_LOCKS="0")
    return subprocess.run(["git", "-c", "core.hooksPath=/dev/null", "-c", "core.fsmonitor=false",
                           "-c", "commit.gpgSign=false", "-c", "maintenance.auto=false",
                           "-C", str(REPO), *args],
                          capture_output=True, text=True, timeout=15, env=environment)


def journal_enabled():
    return (REPO / ".questlog-git").is_file() and (REPO / ".git").is_dir()


def commit_ledger(message):
    """Only LEDGER.md is staged and committed. Other staged files are untouched."""
    if not journal_enabled():
        return None
    try:
        staged = git("add", "--", "LEDGER.md")
        if staged.returncode:
            return "ledger saved but Git staging failed; inspect local state"
        unchanged = git("diff", "--cached", "--quiet", "--", "LEDGER.md")
        if unchanged.returncode == 0:
            return None
        result = git("-c", "user.name=" + os.environ.get("QUESTLOG_GIT_NAME", "Questlog local ledger"),
                     "-c", "user.email=" + os.environ.get("QUESTLOG_GIT_EMAIL", "questlog@localhost"),
                     "commit", "--only", "-m", message, "--", "LEDGER.md")
        if result.returncode:
            return "ledger saved but Git commit failed; inspect local state"
    except (OSError, subprocess.TimeoutExpired):
        return "ledger saved but Git is unavailable; inspect local state"
    return None


def initialize_git():
    """Opt-in local history; called only by the explicit init --git command."""
    initialize()
    with CAPTURE_LOCK, open(REPO / ".ledger.lock", "a+") as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        result = git("init", "--quiet", ".")
        if result.returncode:
            return "Git initialization failed"
        _atomic_write(REPO / ".questlog-git", "enabled\n")
        return commit_ledger("questlog: initialize empty ledger")


def parse_when(q):
    """Local's when: token — strip time words from the query so they don't
    pollute the text match. Returns (since_iso, until_iso, rest_of_query)."""
    parts = (q or "").split()
    idx = next((i for i, w in enumerate(parts) if w.lower().startswith("when:")), None)
    if idx is None:
        return None, None, q
    val = parts[idx][5:].lower()
    rest = " ".join(parts[:idx] + parts[idx + 1:])
    now = datetime.now()
    day = lambda d: d.strftime("%Y-%m-%dT00:00:00")
    eod = lambda d: d.strftime("%Y-%m-%dT23:59:59")
    from datetime import timedelta
    if val == "today":
        return day(now), None, rest
    if val in ("yesterday", "yday"):
        y = now - timedelta(days=1)
        return day(y), eod(y), rest
    if val in ("week", "this-week", "thisweek", "7d", "last7", "7days"):
        return day(now - timedelta(days=7)), None, rest
    if val in ("month", "this-month", "thismonth", "30d", "last30", "30days"):
        return day(now - timedelta(days=30)), None, rest
    if ".." in val:
        a, _, b = val.partition("..")
        try:
            datetime.fromisoformat(a); datetime.fromisoformat(b)
            return a + "T00:00:00", b + "T23:59:59", rest
        except ValueError:
            return None, None, rest
    try:
        datetime.fromisoformat(val)
        return val + "T00:00:00", val + "T23:59:59", rest
    except ValueError:
        return None, None, rest


_recency_cache = {}


def ws_recency():
    if not journal_enabled():
        return {}
    result = git("log", "--format=%ct %s", "-400", "--", "LEDGER.md")
    out = {}
    if result.returncode == 0:
        for line in result.stdout.splitlines():
            stamp, _, subject = line.partition(" ")
            if stamp.isdigit():
                for word in re.findall(r"[a-z0-9][a-z0-9._-]{2,}", subject.lower()):
                    out.setdefault(word, int(stamp))
    return out


STATE_URGENCY = {"hot": 3.0, "blocked": 2.2, "warm": 1.6, "paused": 0.6, "ember": 0.3}


def ws_urgency(w, now_line=""):
    """Urgency score: state weight + overdue waitings + due-soon + NOW membership."""
    u = STATE_URGENCY.get(w["state"], 1.0)
    for x in w.get("waitings", []):
        if x.get("overdue_by", 0) > 0:
            u += 2.0 + min(x["overdue_by"], 7) * 0.2
    for d in w.get("dues", []):
        try:
            days = (date.fromisoformat(d["date"]) - date.today()).days
        except ValueError:
            continue
        if days <= 3:
            u += (3.0 if d.get("kind") == "hard" else 2.0) + max(0, 3 - days) * 0.5
    if w["slug"].lower() in (now_line or "").lower():
        u += 2.5
    return round(u, 2)


def full_state():
    text = LEDGER.read_text(encoding="utf-8")
    state = parse_ledger(text)
    state["journal"] = []
    state["git_head"] = None
    state["head"] = hashlib.sha256(text.encode()).hexdigest()
    state["dirty"] = False
    state["unpushed"] = None
    if journal_enabled():
        log = git("log", "--oneline", "-14", "--", "LEDGER.md")
        state["journal"] = log.stdout.strip().splitlines() if log.returncode == 0 else []
        head = git("rev-parse", "--verify", "HEAD")
        state["git_head"] = head.stdout.strip() if head.returncode == 0 else None
        dirty = git("status", "--porcelain", "--", "LEDGER.md")
        state["dirty"] = bool(dirty.stdout.strip())
    state["pulses"] = pulse_health()
    state["today"] = date.today().isoformat()
    state["prefs"] = read_prefs()
    rec = ws_recency()
    for w in state["workstreams"]:
        w["recent_ts"] = rec.get(w["slug"].lower(), 0)
        w["urgency"] = ws_urgency(w, state.get("now") or "")
    return state


VALID_TAGS = {"done", "focus", "defer", "replied", "chased", "note"}


# --- M0: durable, torn-write-proof, lost-update-proof ledger writes ---

def _atomic_write(path, text, mode=0o600):
    fd, tmp = tempfile.mkstemp(prefix=".questlog-", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            os.fchmod(stream.fileno(), mode)
            stream.write(text)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def ensure_perms():
    REPO.mkdir(parents=True, exist_ok=True, mode=0o700)
    os.chmod(REPO, 0o700)


def initialize():
    ensure_perms()
    # Exclusive creation never overwrites an existing ledger.
    try:
        fd = os.open(LEDGER, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError:
        return
    with os.fdopen(fd, "w", encoding="utf-8") as stream:
        stream.write("# LEDGER — updated " + date.today().isoformat() + "\n\n## NOW\n\n## INBOX\n")


def cas_commit(apply_fn, msg, retries=5):
    """Serialize writers across processes and reject stale HTTP revisions.

    External editors must use this helper too; arbitrary disk edits cannot be locked.
    A revision conflict never writes stale content. Optional Git commits remain local.
    """
    with CAPTURE_LOCK, open(REPO / ".ledger.lock", "a+") as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        content = LEDGER.read_text(encoding="utf-8")
        base = getattr(REQUEST, "base", None)
        if base is not None and base != hashlib.sha256(content.encode()).hexdigest():
            return "revision conflict; reload and retry"
        new, err = apply_fn(content)
        if err:
            return err
        _atomic_write(LEDGER, new)
        return commit_ledger(msg)


def do_capture(text, tag=None):
    """Append a single-line inbox note using the locked ledger writer."""
    text = " ".join(text.split())[:300]
    if not text:
        return "empty capture"
    if tag:
        if tag not in VALID_TAGS:
            return "bad tag"
        text = f"[web:{tag}] {text}"
    stamp = datetime.now().strftime("%m-%d %H:%M")
    bullet = f"- {text}  (web {stamp})"

    def apply(content):
        if "\n## INBOX\n" not in content:
            return content, "no ## INBOX section in ledger"
        return content.replace("\n## INBOX\n", f"\n## INBOX\n{bullet}\n", 1), None

    return cas_commit(apply, "questlog: capture inbox (web)")


# --- UI preferences: custom card order + pins (UI-only, not ledger grammar) ---
PREFS = REPO / "prefs.json"


def read_prefs():
    try:
        p = json.loads(PREFS.read_text(encoding="utf-8"))
        return {"order": list(p.get("order", []))[:300], "pinned": list(p.get("pinned", []))[:80]}
    except Exception:
        return {"order": [], "pinned": []}


def write_prefs(p):
    _atomic_write(PREFS, json.dumps({"order": list(p.get("order", []))[:300],
                                     "pinned": list(p.get("pinned", []))[:80]}))


# --- structured ledger mutations from the UI (drag-to-reclassify) ---
STATE_SET = {"hot", "warm", "paused", "blocked", "ember"}


def _set_now(content, text):
    lines, out, i = content.split("\n"), [], 0
    while i < len(lines):
        out.append(lines[i])
        if lines[i].strip() == "## NOW":
            i += 1
            out.append(text)
            while i < len(lines) and lines[i].strip() != "" and not lines[i].startswith("## "):
                i += 1
            continue
        i += 1
    return "\n".join(out)


def do_mutate(slug, op, value):
    """Drag-driven structured edits: reclassify a workstream's [state], or set NOW.
    Uses the CAS commit path (re-applies on concurrent conflict, no lost updates)."""
    slug = (slug or "").strip()
    if op == "state":
        if value not in STATE_SET:
            return "bad state"
        pat = re.compile(
            rf"^(## {re.escape(slug)}\s+\[(?:work|research|life|forge|client)\])\s+\[(?:hot|warm|paused|blocked|ember)\]\s*$",
            re.M)

        def apply(content):
            c, n = pat.subn(lambda m: f"{m.group(1)} [{value}]", content)
            return (c, None) if n else (content, "workstream not found")

        return cas_commit(apply, f"questlog: web set {slug} → {value}")
    if op == "now":
        text = " ".join(str(value).split())[:200]
        if not text:
            return "empty now"

        def apply(content):
            return _set_now(content, text), None

        return cas_commit(apply, f"questlog: web set NOW → {slug}")

    if op in ("taskToggle", "taskAdd"):
        text = " ".join(str((value or {}).get("text", "")).split())[:200] if isinstance(value, dict) else " ".join(str(value).split())[:200]
        if not text:
            return "empty task"
        hdr = re.compile(rf"^## {re.escape(slug)}\s+\[", re.M)

        def section_span(content):
            m = hdr.search(content)
            if not m:
                return None
            start = m.start()
            nxt = re.search(r"^## ", content[m.end():], re.M)
            end = m.end() + (nxt.start() if nxt else len(content) - m.end())
            return start, end

        if op == "taskToggle":
            def apply(content):
                span = section_span(content)
                if not span:
                    return content, "workstream not found"
                a, b = span
                sec = content[a:b]
                esc = re.escape(text)
                m = re.search(rf"^(\s*)- \[( |x)\] {esc}\s*$", sec, re.M)
                if not m:
                    return content, "subtask not found"
                flipped = " " if m.group(2) == "x" else "x"
                sec = sec[:m.start()] + f"{m.group(1)}- [{flipped}] {text}" + sec[m.end():]
                return content[:a] + sec + content[b:], None
            return cas_commit(apply, f"questlog: web toggle subtask in {slug}")

        def apply(content):
            span = section_span(content)
            if not span:
                return content, "workstream not found"
            a, b = span
            sec = content[a:b].rstrip("\n")
            tail = content[b:]
            return content[:a] + sec + f"\n- [ ] {text}\n" + ("\n" if not tail.startswith("\n") else "") + tail.lstrip("\n"), None
        return cas_commit(apply, f"questlog: web add subtask to {slug}")
    return "bad op"


DOMAINS = {"work", "research", "life", "forge", "client"}


def _slugify(title):
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:40]
    return s or "task"


def do_new(title, domain="life"):
    """Add a new workstream card from a typed title (the simple 'add task' path)."""
    title = " ".join(str(title).split())[:160]
    if not title:
        return "empty title"
    if domain not in DOMAINS:
        domain = "life"
    base = _slugify(title)

    def apply(content):
        existing = set(re.findall(r"^## ([a-z0-9._-]+)\s+\[", content, re.M))
        slug, n = base, 2
        while slug in existing:
            slug, n = f"{base}-{n}", n + 1
        block = f"\n## {slug}  [{domain}] [warm]\nGOAL: {title}\nNEXT: {title}\n"
        return content.rstrip() + "\n" + block, None

    return cas_commit(apply, f"questlog: web add task {base}")


def _ws_docs(state):
    return {w["slug"]: " ".join([w["slug"], w.get("goal") or "", w.get("next") or "", " ".join(w.get("notes") or [])]) for w in state["workstreams"]}


def do_search(q, mode="exact", level=None, sort="relevant"):
    state = full_state()
    docs = _ws_docs(state)
    hits = [w for w in state["workstreams"] if str(q).lower() in docs[w["slug"]].lower()]
    if sort == "urgent":
        hits.sort(key=lambda w: -w["urgency"])
    return {"slugs": [w["slug"] for w in hits], "mode": "exact", "level": None,
            "note": "Local literal search; no embedding adapter configured."}


def do_tagmap(level=None):
    return {"tags": {}, "level": None}


class Handler(BaseHTTPRequestHandler):
    server_version = "questlog-ui/1.0"

    def _send(self, code, body, ctype="application/json; charset=utf-8"):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "DENY")
        self.end_headers()
        self.wfile.write(body)

    def _host_ok(self):
        """Reject browser DNS rebinding on reads and mutations."""
        host = self.headers.get("Host")
        if not host:
            return False
        port = self.server.server_address[1]
        return host in (f"127.0.0.1:{port}", f"localhost:{port}", "127.0.0.1", "localhost")

    def do_GET(self):
        if not self._host_ok():
            self._send(403, b'{"error":"unrecognised Host header"}')
            return
        path = self.path.split("?")[0]
        if path == "/":
            self._send(200, INDEX, "text/html; charset=utf-8")
        elif path == "/bar":
            self._send(200, BAR, "text/html; charset=utf-8")
        elif path == "/quickadd":
            self._send(200, QUICKADD, "text/html; charset=utf-8")
        elif path == "/api/state":
            try:
                self._send(200, json.dumps(full_state()).encode())
            except Exception as e:
                self._send(500, json.dumps({"error": str(e)}).encode())
        elif path == "/api/queue":
            try:
                self._send(200, json.dumps(read_queue()).encode())
            except Exception as e:
                self._send(500, json.dumps({"error": str(e)}).encode())
        elif path == "/api/tags":
            try:
                from urllib.parse import parse_qs, urlparse
                level = (parse_qs(urlparse(self.path).query).get("level", ["small"])[0])
                self._send(200, json.dumps(do_tagmap(level)).encode())
            except Exception as e:
                self._send(500, json.dumps({"error": str(e)}).encode())
        else:
            self._send(404, b'{"error":"not found"}')

    def do_POST(self):
        if not self._host_ok():
            self._send(403, b'{"error":"unrecognised Host header"}')
            return
        path = self.path.split("?")[0]
        if path not in ("/api/capture", "/api/action", "/api/mutate", "/api/prefs", "/api/search", "/api/new"):
            self._send(404, b'{"error":"not found"}')
            return
        # Origin plus non-simple content type protects browser mutation requests.
        origin = self.headers.get("Origin")
        if origin:
            port = self.server.server_address[1]
            if origin not in (f"http://127.0.0.1:{port}", f"http://localhost:{port}"):
                self._send(403, b'{"error":"cross-origin POST refused"}')
                return
        ctype = (self.headers.get("Content-Type") or "").split(";")[0].strip().lower()
        if ctype != "application/json":
            self._send(415, b'{"error":"Content-Type must be application/json"}')
            return
        try:
            n = int(self.headers.get("Content-Length", 0))
            if not 0 < n <= 65536:
                self._send(413, b'{"error":"body too large or empty"}')
                return
            payload = json.loads(self.rfile.read(n) or b"{}")
            if not isinstance(payload, dict):
                raise ValueError("object required")
        except (ValueError, json.JSONDecodeError):
            self._send(400, b'{"error":"bad json"}')
            return
        for key in ("slug", "op", "title", "domain", "tag", "q", "text", "mode", "sort", "level"):
            if key in payload and payload[key] is not None and not isinstance(payload[key], str):
                self._send(400, b'{"error":"text field has invalid type"}')
                return
        if path == "/api/mutate" and payload.get("op") == "state" and not isinstance(payload.get("value"), str):
            self._send(400, b'{"error":"state must be text"}')
            return
        REQUEST.base = self.headers.get("If-Match", "").strip('"')
        if path in ("/api/capture", "/api/mutate", "/api/new") and not REQUEST.base:
            self._send(428, b'{"error":"If-Match revision required"}')
            return
        if path == "/api/action":
            aid, err = enqueue_action(payload.get("slug"), payload.get("text", ""))
            if err:
                self._send(400, json.dumps({"error": err}).encode())
            else:
                self._send(200, json.dumps({"ok": True, "id": aid}).encode())
            return
        if path == "/api/mutate":
            err = do_mutate(payload.get("slug"), payload.get("op"), payload.get("value"))
            self._send((409 if err and err.startswith("revision conflict") else 400) if err else 200,
                       json.dumps({"error": err} if err else {"ok": True}).encode())
            return
        if path == "/api/new":
            err = do_new(payload.get("title", ""), payload.get("domain", "life"))
            self._send((409 if err and err.startswith("revision conflict") else 400) if err else 200,
                       json.dumps({"error": err} if err else {"ok": True}).encode())
            return
        if path == "/api/prefs":
            try:
                write_prefs(payload)
                self._send(200, b'{"ok":true}')
            except Exception as e:
                self._send(500, json.dumps({"error": str(e)}).encode())
            return
        if path == "/api/search":
            try:
                res = do_search(payload.get("q", ""), payload.get("mode", "smart"),
                                payload.get("level", "small"), payload.get("sort", "relevant"))
                self._send(200, json.dumps(res).encode())
            except Exception as e:
                self._send(500, json.dumps({"error": str(e)}).encode())
            return
        err = do_capture(str(payload.get("text", "")), payload.get("tag") or None)
        if err:
            self._send(409 if err.startswith("revision conflict") else 400, json.dumps({"error": err}).encode())
        else:
            self._send(200, b'{"ok":true}')

    def log_message(self, fmt, *args):
        pass


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8321)
    HOST = "127.0.0.1"
    args = ap.parse_args()
    initialize()
    srv = ThreadingHTTPServer((HOST, args.port), Handler)
    print(f"questlog ui on http://{HOST}:{args.port}")
    srv.serve_forever()


if __name__ == "__main__":
    main()
