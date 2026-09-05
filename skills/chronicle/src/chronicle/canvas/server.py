"""The canvas — narrative on the left, the evidence that backs it on the right.

THE ANTI-FICTION MECHANISM
The narrative layer is generative, and generative artifacts drift. Binding every sentence
to the event ids that support it means an unanchored claim renders VISIBLY unanchored —
you can see, at a glance, which parts of the story have receipts and which do not. A
beautiful record that cannot be clicked back to bytes is a story, not a record.

Served locally. No CDN, no external fonts, no build step: one process, one page, works
offline on a plane and on a box with no network egress.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import capture as cap  # noqa: E402
import index as idx  # noqa: E402

HERE = Path(__file__).parent


# ── data access ──────────────────────────────────────────────────────────────

def _conn():
    conn = idx.connect()
    idx.refresh(conn)
    return conn


def api_timeline(project: str | None, day: str | None, limit: int = 400) -> dict:
    conn = _conn()
    sql = "SELECT * FROM events WHERE 1=1"
    args: list = []
    if project and project != "all":
        sql += " AND project=?"
        args.append(project)
    if day:
        sql += " AND ts>=? AND ts<=?"
        args += [day + "T00:00", day + "T23:59:59.999Z"]
    sql += " ORDER BY ts DESC LIMIT ?"
    args.append(limit)
    events = [idx._ev(r) for r in conn.execute(sql, args)]

    narrative = [e for e in events if e.kind == "narrative"]
    trace = [e for e in events if e.kind != "narrative"]

    return {
        "narrative": [_narr(e) for e in narrative],
        "trace": [_trace(e) for e in reversed(trace)],
        "projects": [r["project"] for r in conn.execute(
            "SELECT project, COUNT(*) n FROM events WHERE project<>'' "
            "GROUP BY project ORDER BY n DESC LIMIT 40")],
        "days": [r["d"] for r in conn.execute(
            "SELECT DISTINCT substr(ts,1,10) d FROM events ORDER BY d DESC LIMIT 60")],
        "stats": _stats(conn),
    }


def _stats(conn) -> dict:
    total = conn.execute("SELECT COUNT(*) n FROM events").fetchone()["n"]
    files = conn.execute("SELECT COUNT(DISTINCT path) n FROM files").fetchone()["n"]
    machines = [r["machine"] for r in conn.execute(
        "SELECT DISTINCT machine FROM events WHERE machine<>''")]
    human = conn.execute("SELECT COUNT(*) n FROM events WHERE actor='human'").fetchone()["n"]
    return {"events": total, "files": files, "machines": sorted(machines),
            "human": human, "agent": total - human}


def _narr(e: idx.Event) -> dict:
    raw = e.raw
    return {
        "id": e.id, "entry": raw.get("entry", e.id), "ts": e.ts,
        "trigger": raw.get("trigger", "NOTE"), "summary": e.summary,
        "inferred": bool(raw.get("inferred")),
        "intent": raw.get("intent"), "state": raw.get("state"),
        "why": raw.get("why"), "restore": raw.get("restore"),
        "klass": raw.get("class"), "not_done": raw.get("not_done"),
        "open": raw.get("open") or [], "ext": raw.get("ext") or [],
        "verified": raw.get("verified") or [],
        "corrects": raw.get("corrects"), "resolves": raw.get("resolves") or [],
        "beats": raw.get("beats") or [],
        "caveat": raw.get("caveat"),
        "hypothesis": raw.get("hypothesis"), "setup": raw.get("setup"),
        "varied": raw.get("varied"), "result": raw.get("result"),
        "conclusion": raw.get("conclusion"), "outcome": raw.get("outcome"),
        "why_abandoned": raw.get("why_abandoned"), "confidence": raw.get("confidence"),
        "anchors": raw.get("anchors") or [],
        "project": e.project, "machine": e.machine,
    }


def _trace(e: idx.Event) -> dict:
    raw = e.raw
    files = [{"path": f.get("path", ""), "before": f.get("before", ""),
              "after": f.get("after", ""), "redacted": bool(f.get("redacted"))}
             for f in (raw.get("files") or [])]
    cmd = raw.get("cmd") or {}
    return {
        "id": e.id, "ts": e.ts, "kind": e.kind, "summary": e.summary,
        "project": e.project, "machine": e.machine,
        "actor": (raw.get("actor") or {}).get("kind", "?"),
        "harness": (raw.get("actor") or {}).get("harness", ""),
        "files": files, "exit": cmd.get("exit"),
        "gate": raw.get("gate"),
        "output": raw.get("output") or raw.get("output_head") or "",
        "output_sha": raw.get("output_sha"),
        "text": raw.get("text") or raw.get("text_head") or "",
    }


def api_blob(digest: str) -> tuple[str, bool]:
    try:
        data = cap.cas_get(digest)
    except Exception:
        return "", False
    return data.decode("utf-8", "replace"), True


def api_diff(path: str, before: str, after: str) -> str:
    import difflib
    try:
        a = cap.cas_get(before).decode("utf-8", "replace").splitlines(keepends=True) \
            if before else []
        b = cap.cas_get(after).decode("utf-8", "replace").splitlines(keepends=True) \
            if after else []
    except Exception as exc:
        return f"(content not on this machine: {exc}; run `chron sync`)"
    return "".join(difflib.unified_diff(a, b, fromfile=path + " @before",
                                        tofile=path + " @after")) or "(no textual change)"


# ── server ───────────────────────────────────────────────────────────────────

def build_app():
    """FastAPI if present, else a stdlib http.server. The canvas must not be the reason
    the tool needs a virtualenv on a box you are debugging at 3am."""
    try:
        from fastapi import FastAPI
        from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse
    except ImportError:
        return None

    app = FastAPI(title="chronicle canvas")

    @app.get("/", response_class=HTMLResponse)
    def root():
        return (HERE / "index.html").read_text()

    @app.get("/api/timeline")
    def timeline(project: str = "all", day: str = "", limit: int = 400):
        return JSONResponse(api_timeline(project or None, day or None, limit))

    @app.get("/api/blob", response_class=PlainTextResponse)
    def blob(digest: str):
        text, ok = api_blob(digest)
        return text if ok else "(blob not on this machine — run `chron sync`)"

    @app.get("/api/diff", response_class=PlainTextResponse)
    def diff(path: str = "", before: str = "", after: str = ""):
        return api_diff(path, before, after)

    return app


def _stdlib_server(host: str, port: int):
    """Zero-dependency fallback so `chron canvas` always works."""
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs, urlparse

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def _send(self, body: bytes, ctype: str):
            self.send_response(200)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            u = urlparse(self.path)
            q = {k: v[0] for k, v in parse_qs(u.query).items()}
            try:
                if u.path == "/":
                    self._send((HERE / "index.html").read_bytes(), "text/html; charset=utf-8")
                elif u.path == "/api/timeline":
                    data = api_timeline(q.get("project") or None, q.get("day") or None,
                                        int(q.get("limit", 400)))
                    self._send(json.dumps(data).encode(), "application/json")
                elif u.path == "/api/blob":
                    text, ok = api_blob(q.get("digest", ""))
                    body = text if ok else "(blob not on this machine — run `chron sync`)"
                    self._send(body.encode(), "text/plain; charset=utf-8")
                elif u.path == "/api/diff":
                    body = api_diff(q.get("path", ""), q.get("before", ""), q.get("after", ""))
                    self._send(body.encode(), "text/plain; charset=utf-8")
                else:
                    self.send_error(404)
            except Exception as exc:
                self.send_error(500, str(exc))

    return HTTPServer((host, port), Handler)


def cmd_canvas(args) -> int:
    host = getattr(args, "host", "127.0.0.1")
    port = getattr(args, "port", 8899)
    url = f"http://{host}:{port}"

    if getattr(args, "open_browser", False):
        import threading
        import webbrowser
        threading.Timer(1.0, lambda: webbrowser.open(url)).start()

    app = build_app()
    if app is not None:
        try:
            import uvicorn
            print(f"chronicle canvas → {url}   (fastapi)")
            uvicorn.run(app, host=host, port=port, log_level="warning")
            return 0
        except ImportError:
            pass
    print(f"chronicle canvas → {url}   (stdlib server)")
    _stdlib_server(host, port).serve_forever()
    return 0
