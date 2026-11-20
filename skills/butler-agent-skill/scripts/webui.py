#!/usr/bin/env python3
"""Local Butler dashboard. Mutations require same-origin JSON; no provider actions."""
import os
import math
import datetime as dt
import json
import re
import subprocess
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import butler  # shared ledger helpers

HERE = Path(__file__).parent
PORT = int(os.environ.get("BUTLER_PORT", "8322"))
FLEET_MD = butler.ROOT / "FLEET.md"
CACHE_TTL = 15 * 60
UNBOUND_MIN = 300_000  # weighted tokens below which an unbound session is noise

_cache = {"ts": 0.0, "projects": {}, "machine": None}
_lock = threading.Lock()
_mutation_lock = threading.Lock()
_topics = {}


def finite_number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return False
    try:
        return math.isfinite(value)
    except OverflowError:
        return False


def json_float(value):
    number = float(value)
    if not math.isfinite(number):
        raise ValueError("non-finite JSON number")
    return number


def reject_json_constant(value):
    raise ValueError("nonstandard JSON constant")


def acct_pair():
    cfg = butler.config()
    name = butler.active_account() or next(iter(cfg["accounts"]), "unconfigured")
    return name, cfg["accounts"].get(name, {})


def recompute():
    with _lock:
        name, acct = acct_pair()
        ws = butler.week_start(acct)
        projs = {}
        for slug, p in butler.all_projects().items():
            u = butler.scan_usage(p.get("roots", []), ws, p.get("sessions"))
            projs[slug] = {"weighted": u["weighted"],
                           "by_model": {k: round(v) for k, v in u["by_model"].items()},
                           "by_day": {k: round(v) for k, v in u["by_day"].items()},
                           "by_session": {k: round(v) for k, v in u["by_session"].items()}}
        m = butler.scan_usage([r for p in butler.all_projects().values() for r in p.get("roots", [])], ws, timeline=butler.account_timeline())
        _cache.update({"ts": time.time(), "projects": projs,
                       "machine": {"weighted": m["weighted"], "sessions": m["sessions"],
                                   "input": m["input"], "output": m["output"],
                                   "cache_read": m["cache_read"],
                                   "cache_creation": m["cache_creation"],
                                   "by_day": {k: round(v) for k, v in m["by_day"].items()},
                                   "by_account": {k: round(v) for k, v in m["by_account"].items()},
                                   "by_session": {k: round(v) for k, v in m["by_session"].items()}}})


def session_topic(sid):
    if not butler.config().get("show_session_topics", False):
        return ""
    """First real user message of a session — cached, cheap-ish."""
    if sid in _topics:
        return _topics[sid]
    topic = ""
    try:
        for f in butler.CLAUDE_PROJECTS.glob(f"*/{sid}*.jsonl"):
            with open(f) as fh:
                for i, line in enumerate(fh):
                    if i > 300:
                        break
                    try:
                        obj = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if obj.get("type") == "user":
                        c = (obj.get("message") or {}).get("content")
                        t = c if isinstance(c, str) else next(
                            (x.get("text", "") for x in c
                             if isinstance(x, dict) and x.get("type") == "text"), "") if isinstance(c, list) else ""
                        t = " ".join((t or "").split())
                        if t and not t.startswith(("Caveat", "<", "[")):
                            topic = t[:90]
                            break
            break
    except OSError:
        pass
    _topics[sid] = topic
    return topic


def gate_info(name):
    """Active hard stop for this account, if any."""
    for ev in reversed(butler.read_jsonl(butler.ROOT / "events.jsonl")[-200:]):
        if ev.get("type") == "rate_limit" and ev.get("account") in (name, None):
            resume = ev.get("resume_at", "")
            try:
                if dt.datetime.fromisoformat(resume.replace("Z", "+00:00")) > dt.datetime.now(dt.timezone.utc):
                    return resume
            except ValueError:
                pass
            break
    return None


def gpu_windows(slug, lim):
    n = dt.datetime.now(dt.timezone.utc)
    out = {}
    for window, days in (("day", 1), ("week", 7), ("month", 30)):
        snap = butler._gpu_snapshot(slug, n - dt.timedelta(days=days))
        out[window] = {
            "used": round(snap["committed_gpu_hours"], 2),  # v2 API compatibility
            "completed": round(snap["completed_gpu_hours"], 2),
            "reserved": round(snap["reserved_gpu_hours"], 2),
            "committed": round(snap["committed_gpu_hours"], 2),
            "budget": lim.get(window),
        }
    return out


def fleet():
    if not butler.config().get("inspect_local_processes", False):
        return []
    names = {}
    if FLEET_MD.exists():
        for m in re.finditer(r"\|\s*(ttys\d+)\s*\|\s*\*?\*?([^|*]+?)\*?\*?\s*\|\s*([^|]+?)\s*\|",
                             FLEET_MD.read_text()):
            names[m.group(1)] = (m.group(2).strip(), m.group(3).strip())
    rows = []
    out = subprocess.run(["ps", "-axo", "pid=,tty=,etime=,command="],
                         capture_output=True, text=True).stdout
    for line in out.splitlines():
        parts = line.split(None, 3)
        if len(parts) < 4 or not parts[3].startswith("claude"):
            continue
        nm, mission = names.get(parts[1], ("?", "unbound — see FLEET.md"))
        rows.append({"pid": parts[0], "tty": parts[1], "up": parts[2],
                     "name": nm, "mission": mission})
    rows.sort(key=lambda r: r["tty"])
    return rows


def last_days(n=7):
    today = dt.date.today()
    return [(today - dt.timedelta(days=i)).isoformat() for i in range(n - 1, -1, -1)]


def remotes():
    out = {}
    for f in (butler.ROOT / "remote").glob("*.json"):
        s = butler.load_json(f, None)
        if s:
            out[s.get("machine", f.stem)] = s
    return out


def state():
    if time.time() - _cache["ts"] > CACHE_TTL:
        recompute()
    name, acct = acct_pair()
    ws = butler.week_start(acct)
    weekly = acct.get("weekly_weighted_budget", 0)
    hard_until = gate_info(name)
    all_p = butler.all_projects()

    rem = remotes()
    projects = []
    bound_prefixes = []
    for slug, p in sorted(all_p.items()):
        bound_prefixes += [s for s in p.get("sessions", []) if ":" not in s]
        u = _cache["projects"].get(slug, {})
        remote_spent = 0
        machines_used = set()
        for b in p.get("sessions", []):
            if ":" in b:
                mname, sid = b.split(":", 1)
                snap = rem.get(mname)
                if snap:
                    for rsid, w in snap["data"].get("by_session", {}).items():
                        if rsid.startswith(sid) or sid in rsid:
                            remote_spent += w
                            machines_used.add(mname)
        spent = u.get("weighted", 0) + remote_spent
        budget = weekly * p.get("budget_pct_weekly", 0) / 100.0
        pct = round(100 * spent / budget, 1) if budget else None
        lim = p.get("gpu_hours") or {}
        has_gpu = any(v is not None for v in lim.values())
        log = butler.read_jsonl(butler.project_path(slug) / "sessions.jsonl")[-3:][::-1]
        verdict = "hard" if hard_until else ("soft" if (pct or 0) >= 100 else "go")
        projects.append({
            "slug": slug, "alloc": p.get("budget_pct_weekly"), "status": p.get("status"),
            "accounts": p.get("accounts", []), "sessions": p.get("sessions", []),
            "spent": round(spent), "remote_spent": round(remote_spent),
            "machines": sorted(machines_used), "budget": round(budget), "pct": pct, "gate": verdict,
            "by_model": u.get("by_model", {}), "by_day": u.get("by_day", {}),
            "by_session": u.get("by_session", {}),
            "gpu": gpu_windows(slug, lim) if has_gpu else None,
            "log": [{"ts": l.get("ts", "")[:16], "summary": l.get("summary", "")} for l in log],
        })
    projects.sort(key=lambda r: -(r["pct"] or 0))

    mu = _cache["machine"] or {}
    spent = mu.get("weighted", 0)
    elapsed = max(1.0, (dt.datetime.now(dt.timezone.utc) - ws).total_seconds())
    frac = min(1.0, elapsed / (7 * 86400))
    rate = spent / elapsed
    dry_at = None
    if rate > 0 and spent < weekly:
        dry = ws + dt.timedelta(seconds=weekly / rate)
        if dry < ws + dt.timedelta(days=7):
            dry_at = dry.strftime("%a %H:%M")

    # burn chart: top 5 projects by week spend + Other, per day
    days = last_days(7)
    top = sorted(projects, key=lambda r: -r["spent"])[:5]
    top = sorted([p for p in top if p["spent"] > 0], key=lambda r: r["slug"])  # stable slot order
    series = [{"name": p["slug"], "values": [p["by_day"].get(d, 0) for d in days]} for p in top]
    mday = mu.get("by_day", {})
    other = []
    for i, d in enumerate(days):
        s = sum(sr["values"][i] for sr in series)
        other.append(max(0, mday.get(d, 0) - s))
    chart = {"days": days, "series": series, "other": other,
             "daily_par": round(weekly / 7) if weekly else 0}

    # unbound sessions: in machine total but bound to no project
    unbound = []
    for sid, w in sorted(mu.get("by_session", {}).items(), key=lambda kv: -kv[1]):
        if w < UNBOUND_MIN:
            break
        if any(sid.startswith(pref) or pref in sid for pref in bound_prefixes):
            continue
        unbound.append({"sid": sid[:8], "spent": round(w), "topic": session_topic(sid)})
        if len(unbound) >= 12:
            break

    # per-subscription spend: local timeline attribution + remote machines by their account
    local_by_acct = mu.get("by_account", {})
    acct_spend = {a: local_by_acct.get(a, 0) for a in butler.config()["accounts"]}
    machines_view = []
    for mname, mc in butler.config().get("machines", {}).items():
        if mc.get("local"):
            machines_view.append({"name": mname, "kind": "local", "ok": True,
                                  "weighted": round(spent), "sessions": mu.get("sessions", 0),
                                  "age_min": round((time.time() - _cache["ts"]) / 60) if _cache["ts"] else None})
            continue
        snap = rem.get(mname)
        if snap:
            acct_spend[snap.get("account") or "unconfigured"] =                 acct_spend.get(snap.get("account") or "unconfigured", 0) + snap["data"]["weighted"]
            age = (dt.datetime.now(dt.timezone.utc)
                   - dt.datetime.fromisoformat(snap["fetched_at"])).total_seconds() / 60
            machines_view.append({"name": mname, "kind": "remote", "ok": True,
                                  "enabled": mc.get("enabled", False),
                                  "weighted": round(snap["data"]["weighted"]),
                                  "sessions": snap["data"]["sessions"], "age_min": round(age)})
        else:
            machines_view.append({"name": mname, "kind": "remote", "ok": False,
                                  "enabled": mc.get("enabled", False),
                                  "weighted": None, "sessions": None, "age_min": None})
    weekly_by_acct = {a: c.get("weekly_weighted_budget", 0)
                      for a, c in butler.config()["accounts"].items()}
    ru = butler.real_utilization()
    return {
        "real": ru,
        "usage_available": bool(os.environ.get("BUTLER_CLAUDE_PROJECTS")) and butler.CLAUDE_PROJECTS.is_dir(),
        "fleet_enabled": bool(butler.config().get("inspect_local_processes", False)),
        "accounts_spend": {a: {"spent": round(v), "budget": weekly_by_acct.get(a, 0),
                               "pct": round(100 * v / weekly_by_acct[a], 1) if weekly_by_acct.get(a) else None}
                           for a, v in acct_spend.items()},
        "machines": machines_view,
        "account": name, "accounts": list(butler.config()["accounts"]),
        "accounts_cfg": {k: {"weekly_m": round(v.get("weekly_weighted_budget", 0) / 1e6)}
                         for k, v in butler.config()["accounts"].items()},
        "lock": butler.load_json(butler.ROOT / "account.lock", {}),
        "week_start": ws.isoformat(), "today": time.strftime("%Y-%m-%d"),
        "hard_until": hard_until,
        "machine": {**{k: v for k, v in mu.items() if k not in ("by_day", "by_session")},
                    "budget": weekly,
                    "pct": round(100 * spent / weekly, 1) if weekly else None,
                    "week_frac": round(100 * frac, 1),
                    "projected_week_total": round(spent / frac) if frac else None,
                    "dry_at": dry_at},
        "chart": chart, "projects": projects, "unbound": unbound,
        "alloc_total": butler.portfolio_audit()["active_total_pct"],
        "portfolio": butler.portfolio_audit(),
        "fleet": fleet(),
        "events": butler.read_jsonl(butler.ROOT / "events.jsonl")[-25:][::-1],
        "scanned_at": dt.datetime.fromtimestamp(_cache["ts"]).strftime("%H:%M:%S") if _cache["ts"] else None,
    }


def edit_project(slug, fn):
    pj = butler.project_path(slug) / "project.json"
    p = butler.load_json(pj, None)
    if p is None:
        return False
    fn(p)
    butler.save_json(pj, p)
    return True


class H(BaseHTTPRequestHandler):
    server_version = "butler-ui/2.0"

    def log_message(self, *a):
        pass

    def _json(self, obj, code=200):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _body(self):
        try:
            return json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))),
                              parse_float=json_float, parse_constant=reject_json_constant)
        except (ValueError, json.JSONDecodeError):
            return None

    def _host_ok(self):
        port = self.server.server_address[1]
        return self.headers.get("Host") in (f"127.0.0.1:{port}", f"localhost:{port}")

    def do_GET(self):
        if not self._host_ok():
            return self._json({"error": "unrecognised Host"}, 403)
        path = self.path.split("?")[0]
        if path == "/":
            body = (HERE / "webui.html").read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("X-Frame-Options", "DENY")
            self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'; object-src 'none'")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        elif path == "/api/state":
            try:
                self._json(state())
            except Exception as e:
                self._json({"error": str(e)}, 500)
        else:
            self._json({"error": "not found"}, 404)

    def do_POST(self):
        port = self.server.server_address[1]
        if not self._host_ok() or self.headers.get("Origin") not in (None, f"http://127.0.0.1:{port}", f"http://localhost:{port}"):
            return self._json({"error": "cross-origin request refused"}, 403)
        if self.headers.get("Content-Type", "").split(";")[0].strip() != "application/json":
            return self._json({"error": "application/json required"}, 415)
        try:
            size = int(self.headers.get("Content-Length", 0))
        except ValueError:
            return self._json({"error": "bad length"}, 400)
        if not 0 < size <= 65536:
            return self._json({"error": "body too large or empty"}, 413)
        path = self.path.split("?")[0]
        b = self._body()
        if not isinstance(b, dict):
            return self._json({"error": "bad json"}, 400)
        for field in ("project", "account", "type", "status", "session", "job", "note", "machine"):
            if field in b and b[field] is not None and not isinstance(b[field], str):
                return self._json({"error": "invalid text field"}, 400)
        try:
            with _mutation_lock:
                return self._route(path, b)
        except (ValueError, TypeError, OverflowError) as e:
            return self._json({"error": str(e)}, 400)
        except Exception as e:
            return self._json({"error": str(e)}, 500)

    def _route(self, path, b):
        if path == "/api/refresh":
            recompute()
            return self._json({"ok": True})
        if path == "/api/collect":
            return self._json({"error": "remote collection requires explicit CLI invocation"}, 403)
        if path == "/api/event":
            if b.get("type") not in ("rate_limit", "pause", "resume", "note"):
                return self._json({"error": "bad type"}, 400)
            ev = {"type": b["type"], "ts": dt.datetime.now(dt.timezone.utc).isoformat(),
                  "account": butler.active_account(), "project": b.get("project"),
                  "note": (b.get("note") or "")[:500], "source": "webui"}
            if b["type"] == "rate_limit":
                hours = butler.config().get("session_window_hours", 5)
                ev["resume_at"] = (dt.datetime.now(dt.timezone.utc)
                                   + dt.timedelta(hours=hours)).isoformat()
            butler.append_jsonl(butler.ROOT / "events.jsonl", ev)
            return self._json({"ok": True})
        if path == "/api/alloc":
            pct = b.get("pct")
            if not finite_number(pct) or not 0 <= pct <= 100:
                return self._json({"error": "bad pct"}, 400)
            slug = b.get("project", "")
            p = butler.load_json(butler.project_path(slug) / "project.json", None)
            if p is None:
                return self._json({"error": "unknown project"}, 404)
            p["budget_pct_weekly"] = pct
            audit = butler.portfolio_audit((slug, p))
            if audit["verdict"] != "proceed":
                return self._json({"error": "portfolio would be overallocated", **audit}, 409)
            butler.save_json(butler.project_path(slug) / "project.json", p)
            return self._json({"ok": True, "portfolio": audit})
        if path == "/api/status":
            if b.get("status") not in ("active", "parked"):
                return self._json({"error": "bad status"}, 400)
            slug = b.get("project", "")
            p = butler.load_json(butler.project_path(slug) / "project.json", None)
            if p is None:
                return self._json({"error": "unknown project"}, 404)
            p["status"] = b["status"]
            audit = butler.portfolio_audit((slug, p))
            if audit["verdict"] != "proceed" and b["status"] == "active":
                return self._json({"error": "portfolio would be overallocated", **audit}, 409)
            butler.save_json(butler.project_path(slug) / "project.json", p)
            return self._json({"ok": True, "portfolio": audit})
        if path == "/api/bind":
            sid = (b.get("session") or "").strip()
            if not re.fullmatch(r"[0-9a-f-]{4,40}", sid):
                return self._json({"error": "bad session id"}, 400)
            ok = edit_project(b.get("project", ""),
                              lambda p: p.update(sessions=sorted(set(p.get("sessions", []) + [sid]))))
            return self._json({"ok": ok})
        if path == "/api/config":
            acct, weekly_m = b.get("account"), b.get("weekly_m")
            cfg = butler.config()
            if acct not in cfg["accounts"] or not finite_number(weekly_m) or weekly_m <= 0 or not finite_number(weekly_m * 1e6):
                return self._json({"error": "bad account/weekly_m"}, 400)
            cfg["accounts"][acct]["weekly_weighted_budget"] = int(weekly_m * 1e6)
            butler.save_json(butler.ROOT / "config.json", cfg)
            return self._json({"ok": True})
        if path == "/api/normalize":
            target = b.get("target", 85)
            limit = butler.config().get("portfolio_budget_pct", 85)
            if not finite_number(target) or not finite_number(limit) or target <= 0 or target > limit:
                return self._json({"error": f"target must be in (0, {limit}]"}, 400)
            allp = butler.all_projects()
            active = {slug: p for slug, p in allp.items() if p.get("status", "active") == "active"}
            if any(not finite_number(p.get("budget_pct_weekly", 0)) or p.get("budget_pct_weekly", 0) < 0 for p in active.values()):
                return self._json({"error": "invalid stored allocation"}, 400)
            total = sum(p.get("budget_pct_weekly", 0) for p in active.values())
            if not finite_number(total) or total <= 0:
                return self._json({"error": "nothing to normalize"}, 400)
            k = target / total
            for slug in active:
                edit_project(slug, lambda p: p.update(
                    budget_pct_weekly=round(p.get("budget_pct_weekly", 0) * k, 1)))
            return self._json({"ok": True, "factor": round(k, 3)})
        if path == "/api/gpu-log":
            slug, job = b.get("project"), (b.get("job") or "").strip()
            gpus, hours = b.get("gpus"), b.get("hours")
            if slug not in butler.all_projects() or not job or \
               not finite_number(gpus) or not finite_number(hours) or \
               gpus <= 0 or hours <= 0 or not finite_number(gpus * hours):
                return self._json({"error": "bad gpu-log"}, 400)
            with butler.gpu_ledger_lock():
                butler.append_jsonl(butler.GPU_LEDGER,
                                    {"type": "legacy_usage",
                                     "ts": dt.datetime.now(dt.timezone.utc).isoformat(),
                                     "project": slug, "job": job, "gpus": gpus, "hours": hours,
                                     "gpu_hours": gpus * hours, "note": "webui"})
            return self._json({"ok": True})
        if path == "/api/switch":
            acct = b.get("account")
            if acct not in butler.config()["accounts"]:
                return self._json({"error": "unknown account"}, 400)
            lock = {"account": acct, "since": dt.datetime.now(dt.timezone.utc).isoformat(),
                    "by": "webui"}
            butler.save_json(butler.ROOT / "account.lock", lock)
            butler.append_jsonl(butler.ROOT / "events.jsonl",
                                {"type": "switch", "ts": lock["since"], "account": acct,
                                 "by": "webui"})
            return self._json({"ok": True, "next": "Local label only; provider authentication is unchanged."})
        return self._json({"error": "not found"}, 404)


if __name__ == "__main__":
    print(f"butler ui v2 on http://127.0.0.1:{PORT}  (ledger: {butler.ROOT})")

    ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()
