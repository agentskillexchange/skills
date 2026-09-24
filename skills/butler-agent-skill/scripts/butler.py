#!/usr/bin/env python3
"""Local project budgets and atomic GPU reservations.
Claude weighted-token estimates are not actual Codex quota. Transcript and provider
cache imports are opt-in. This runtime does not launch compute or enforce a provider budget.
"""
import argparse
import contextlib
import datetime as dt
import fcntl
import json
import math
import os
import sys
import tempfile
from pathlib import Path
from typing import Any

ROOT = Path(os.environ.get("BUTLER_ROOT", "./.butler")).expanduser().absolute()
CLAUDE_PROJECTS = Path(os.environ["BUTLER_CLAUDE_PROJECTS"]).expanduser() if os.environ.get("BUTLER_CLAUDE_PROJECTS") else ROOT / "disabled-transcript-input"

DEFAULT_CONFIG = {
    "accounts": {},
    "weights": {"input": 1.0, "output": 5.0, "cache_creation": 1.25, "cache_read": 0.1},
    "session_window_hours": 5,
    "portfolio_budget_pct": 85,
    "gpu_scopes": {},
}


def now_utc():
    return dt.datetime.now(dt.timezone.utc)


def load_json(path, default):
    try:
        return json.loads(Path(path).read_text())
    except (OSError, json.JSONDecodeError):
        return default


def ensure_private_root():
    """Only adopt an empty directory or one containing recognizable Butler state.

    Never chmod a home, working tree root, ancestor, symlink or mixed-use directory.
    Existing dedicated state is made owner-only; unrelated directories are refused.
    """
    resolved = ROOT.resolve()
    forbidden = {Path.home().resolve(), Path.cwd().resolve(), *Path.cwd().resolve().parents}
    if ROOT.is_symlink() or resolved in forbidden:
        raise ValueError("BUTLER_ROOT must be a dedicated private state directory")
    names = {"projects", "gpu", "remote", "config.json", "events.jsonl", "account.lock", "FLEET.md", "LEDGER.md"}
    if ROOT.exists():
        if not ROOT.is_dir():
            raise ValueError("BUTLER_ROOT is not a directory")
        for entry in ROOT.iterdir():
            temporary = any(entry.name.startswith("." + name + ".") for name in names)
            if entry.name not in names and not temporary:
                raise ValueError("refusing a mixed-use BUTLER_ROOT; choose a dedicated state directory")
    ROOT.mkdir(parents=True, exist_ok=True, mode=0o700)
    os.chmod(ROOT, 0o700)


def private_parent(path):
    path = Path(path).absolute()
    # Validate containment before creating or changing any directory.
    try:
        relative = path.relative_to(ROOT.absolute())
        path.resolve().relative_to(ROOT.resolve())
    except ValueError as exc:
        raise ValueError("private write must stay within BUTLER_ROOT") from exc
    ensure_private_root()
    parent = ROOT
    for part in relative.parts[:-1]:
        parent = parent / part
        if parent.is_symlink():
            raise ValueError("symlinked state directories are not supported")
        parent.mkdir(exist_ok=True, mode=0o700)
        os.chmod(parent, 0o700)
    if path.is_symlink():
        raise ValueError("symlinked state files are not supported")
    return path


def write_private_text(path, text):
    path = private_parent(path)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w") as f:
            os.fchmod(f.fileno(), 0o600)
            f.write(text)
            f.flush()
            os.fsync(f.fileno())
        os.replace(temporary, path)
    except Exception:
        try:
            os.unlink(temporary)
        except OSError:
            pass
        raise


def save_json(path, obj):
    # Reject invalid numbers before creating directories or replacing prior state.
    body = json.dumps(obj, indent=2, sort_keys=True, allow_nan=False) + "\n"
    write_private_text(path, body)


def config():
    return load_json(ROOT / "config.json", DEFAULT_CONFIG)


def append_private_text(path, text):
    """Stable side lock plus atomic replacement prevents partial private appends."""
    path = private_parent(path)
    lock_path = private_parent(path.parent / ("." + path.name + ".append.lock"))
    fd = os.open(lock_path, os.O_RDWR | os.O_CREAT | getattr(os, "O_NOFOLLOW", 0), 0o600)
    with os.fdopen(fd, "a+") as lock:
        os.fchmod(lock.fileno(), 0o600)
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        previous = path.read_text() if path.exists() else ""
        write_private_text(path, previous + text)


def append_jsonl(path, obj):
    body = json.dumps(obj, sort_keys=True, allow_nan=False) + "\n"
    append_private_text(path, body)


@contextlib.contextmanager
def gpu_ledger_lock():
    """Serialize a GPU admission decision and its append across processes."""
    lock_path = private_parent(ROOT / "gpu" / "ledger.lock")
    fd = os.open(lock_path, os.O_RDWR | os.O_CREAT | getattr(os, "O_NOFOLLOW", 0), 0o600)
    with os.fdopen(fd, "a+") as lock:
        os.fchmod(lock.fileno(), 0o600)
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(lock.fileno(), fcntl.LOCK_UN)


def read_jsonl(path, *, tolerate_torn_final=True):
    """Read JSONL, optionally requiring a final terminator for safe appends."""
    out = []
    try:
        with open(path, newline="") as f:
            lines = f.readlines()
            for line_number, line in enumerate(lines, 1):
                if not line.strip():
                    continue
                is_unterminated_final = (
                    line_number == len(lines)
                    and not line.endswith(("\n", "\r"))
                )
                if is_unterminated_final and not tolerate_torn_final:
                    raise ValueError(
                        f"{path}: unterminated JSONL at line {line_number}"
                    )
                try:
                    out.append(json.loads(line))
                except json.JSONDecodeError as exc:
                    if is_unterminated_final:
                        # Ignore only the one row an interrupted append can leave torn.
                        continue
                    raise ValueError(
                        f"{path}: malformed JSONL at line {line_number}"
                    ) from exc
    except OSError:
        return []
    return out


def encode_root(root):
    """Claude Code encodes a cwd /a/b/c as directory name -a-b-c."""
    return str(Path(root).resolve()).replace("/", "-")


def project_path(slug):
    import re
    if not isinstance(slug, str) or not re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9._-]{0,63}", slug):
        raise ValueError("invalid project identifier")
    return ROOT / "projects" / slug


def load_project(slug):
    p = load_json(project_path(slug) / "project.json", None)
    if p is None:
        sys.exit(f"butler: unknown project '{slug}' — register it first")
    return p


def all_projects():
    out = {}
    for d in sorted((ROOT / "projects").glob("*/project.json")):
        out[d.parent.name] = load_json(d, {})
    return out


def week_start(account_cfg):
    n = now_utc()
    dow = int(account_cfg.get("reset_dow", 0))
    hour = int(account_cfg.get("reset_hour_utc", 0))
    delta = (n.weekday() - dow) % 7
    start = (n - dt.timedelta(days=delta)).replace(hour=hour, minute=0, second=0, microsecond=0)
    if start > n:
        start -= dt.timedelta(days=7)
    return start


def parse_ts(s):
    try:
        return dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
    except (ValueError, AttributeError):
        return None


def scan_usage(roots, since, sessions=None, timeline=None):
    """Sum weighted token usage from Claude Code transcripts under the given roots."""
    w = config()["weights"]
    totals = {"input": 0, "output": 0, "cache_creation": 0, "cache_read": 0,
              "weighted": 0.0, "sessions": set(), "by_model": {}, "by_day": {}, "by_session": {}, "by_account": {}}
    prefixes = [encode_root(r) for r in roots]
    if not CLAUDE_PROJECTS.is_dir():
        totals["sessions"] = 0
        return totals
    for proj_dir in CLAUDE_PROJECTS.iterdir():
        if not proj_dir.is_dir():
            continue
        if not any(proj_dir.name == p or proj_dir.name.startswith(p + "-") for p in prefixes):
            continue
        for jf in proj_dir.rglob("*.jsonl"):
            if sessions and not any(s in str(jf) for s in sessions):
                continue
            try:
                if since and dt.datetime.fromtimestamp(jf.stat().st_mtime, dt.timezone.utc) < since:
                    continue  # file untouched since window start — skip cheaply
                with open(jf) as f:
                    for line in f:
                        if '"usage"' not in line:
                            continue
                        try:
                            obj = json.loads(line)
                        except json.JSONDecodeError:
                            continue
                        ts = parse_ts(obj.get("timestamp", ""))
                        if since and ts and ts < since:
                            continue
                        msg = obj.get("message") or {}
                        u = msg.get("usage") or obj.get("usage") or {}
                        if not u:
                            continue
                        i = u.get("input_tokens", 0) or 0
                        o = u.get("output_tokens", 0) or 0
                        cc = u.get("cache_creation_input_tokens", 0) or 0
                        cr = u.get("cache_read_input_tokens", 0) or 0
                        totals["input"] += i
                        totals["output"] += o
                        totals["cache_creation"] += cc
                        totals["cache_read"] += cr
                        weighted = (i * w["input"] + o * w["output"]
                                    + cc * w["cache_creation"] + cr * w["cache_read"])
                        totals["weighted"] += weighted
                        sid = obj.get("sessionId", jf.stem)
                        totals["sessions"].add(sid)
                        totals["by_session"][sid] = totals["by_session"].get(sid, 0.0) + weighted
                        day = (obj.get("timestamp") or "")[:10]
                        if day:
                            totals["by_day"][day] = totals["by_day"].get(day, 0.0) + weighted
                        if timeline:
                            tsp = parse_ts(obj.get("timestamp") or "")
                            acct = account_at(timeline, tsp.timestamp()) if tsp else timeline[0][1]
                            totals["by_account"][acct] = totals["by_account"].get(acct, 0.0) + weighted
                        model = msg.get("model", "unknown")
                        totals["by_model"][model] = totals["by_model"].get(model, 0.0) + weighted
            except OSError:
                continue
    totals["sessions"] = len(totals["sessions"])
    return totals


CLAUDE_JSON = Path(os.environ["BUTLER_CLAUDE_CACHE"]).expanduser() if os.environ.get("BUTLER_CLAUDE_CACHE") else ROOT / "disabled-provider-cache"


def real_utilization():
    """Optional cached Claude provider report; may be stale and is not Codex quota."""
    d = load_json(CLAUDE_JSON, {})
    cu = d.get("cachedUsageUtilization")
    if not cu:
        return None
    util = cu.get("utilization", {})
    uuid = cu.get("accountUuid")
    name = None
    for an, ac in config()["accounts"].items():
        if ac.get("uuid") == uuid:
            name = an
            break
    limits = util.get("limits", [])
    def block(k):
        b = util.get(k) or {}
        return {"pct": b.get("utilization"), "resets_at": b.get("resets_at")}
    scoped = [{"model": ((l.get("scope") or {}).get("model") or {}).get("display_name"),
               "pct": l.get("percent"), "severity": l.get("severity"),
               "active": l.get("is_active"), "resets_at": l.get("resets_at")}
              for l in limits if l.get("kind") == "weekly_scoped"]
    return {"account": name, "uuid": uuid,
            "fetched_at_ms": cu.get("fetchedAtMs"),
            "five_hour": block("five_hour"), "seven_day": block("seven_day"),
            "scoped": scoped,
            "worst": max([l.get("percent") or 0 for l in limits], default=0)}


def account_timeline():
    """[(epoch, account)] — who held the machine when. Approximate before first switch."""
    cfg = config()
    tl = [(0.0, cfg.get("default_account") or next(iter(cfg["accounts"]), "unconfigured"))]
    for ev in read_jsonl(ROOT / "events.jsonl"):
        if ev.get("type") == "switch" and ev.get("account"):
            t = parse_ts(ev.get("ts", ""))
            if t:
                tl.append((t.timestamp(), ev["account"]))
    return sorted(tl)


def account_at(timeline, epoch):
    acct = timeline[0][1]
    for t, a in timeline:
        if t <= epoch:
            acct = a
        else:
            break
    return acct


REMOTE_COLLECTOR = r'''
import json,sys,os,datetime
since=__SINCE__; W=__WEIGHTS__
root=os.path.expanduser("~/.claude/projects")
tot={"weighted":0.0,"by_day":{},"by_session":{},"by_model":{},"sessions":0}
seen=set()
for dp,_,fns in os.walk(root):
  for fn in fns:
    if not fn.endswith(".jsonl"):continue
    p=os.path.join(dp,fn)
    try:
      if os.path.getmtime(p)<since:continue
      f=open(p,encoding="utf-8",errors="replace")
    except OSError:continue
    with f:
      for line in f:
        if '"usage"' not in line:continue
        try:o=json.loads(line)
        except:continue
        ts=o.get("timestamp","")
        try:
          t=datetime.datetime.fromisoformat(ts.replace("Z","+00:00")).timestamp()
          if t<since:continue
        except (ValueError,AttributeError):pass
        m=o.get("message") or {}
        u=m.get("usage") or o.get("usage") or {}
        if not u:continue
        w=((u.get("input_tokens") or 0)*W["input"]+(u.get("output_tokens") or 0)*W["output"]
           +(u.get("cache_creation_input_tokens") or 0)*W["cache_creation"]
           +(u.get("cache_read_input_tokens") or 0)*W["cache_read"])
        tot["weighted"]+=w
        d=ts[:10]
        if d:tot["by_day"][d]=tot["by_day"].get(d,0)+w
        sid=o.get("sessionId",fn[:-6]);seen.add(sid)
        tot["by_session"][sid]=tot["by_session"].get(sid,0)+w
        md=m.get("model","unknown");tot["by_model"][md]=tot["by_model"].get(md,0)+w
tot["sessions"]=len(seen)
tot["by_session"]=dict(sorted(tot["by_session"].items(),key=lambda kv:-kv[1])[:60])
tot["by_day"]={k:round(v) for k,v in tot["by_day"].items()}
tot["by_model"]={k:round(v) for k,v in tot["by_model"].items()}
print(json.dumps(tot))
'''


def collect_machine(name, mcfg, since_epoch):
    import subprocess as sp
    script = (REMOTE_COLLECTOR
              .replace("__SINCE__", repr(float(since_epoch)))
              .replace("__WEIGHTS__", json.dumps(config()["weights"])))
    r = sp.run(["ssh", "-o", "ConnectTimeout=6", "-o", "BatchMode=yes", mcfg["ssh"], "python3", "-"],
               input=script, capture_output=True, text=True, timeout=180)
    if r.returncode != 0 or not r.stdout.strip():
        raise RuntimeError((r.stderr or "no output").strip()[-300:])
    data = json.loads(r.stdout.strip().splitlines()[-1])
    snap = {"machine": name, "account": mcfg.get("account"),
            "fetched_at": now_utc().isoformat(), "since": since_epoch, "data": data}
    save_json(ROOT / "remote" / f"{name}.json", snap)
    return snap


def cmd_collect(args):
    cfg = config()
    acct = cfg["accounts"].get(cfg.get("default_account") or "", {})
    since = week_start(acct).timestamp()
    out = {}
    for name, m in cfg.get("machines", {}).items():
        if m.get("local") or not m.get("enabled"):
            continue
        if args.machine and name != args.machine:
            continue
        try:
            snap = collect_machine(name, m, since)
            out[name] = {"ok": True, "weighted": round(snap["data"]["weighted"]),
                         "sessions": snap["data"]["sessions"]}
        except Exception as e:
            out[name] = {"ok": False, "error": str(e)[:200]}
    print(json.dumps(out, indent=2))


def active_account():
    lock = load_json(ROOT / "account.lock", {})
    return lock.get("account")


def portfolio_audit(replace=None):
    """Return active token allocations, optionally replacing one project in-memory."""
    projects = all_projects()
    if replace:
        projects[replace[0]] = replace[1]
    active = {slug: p for slug, p in projects.items() if p.get("status", "active") == "active"}
    total = sum(float(p.get("budget_pct_weekly", 0) or 0) for p in active.values())
    limit = float(config().get("portfolio_budget_pct", 85))
    return {
        "verdict": "proceed" if total <= limit else "overallocated",
        "active_total_pct": round(total, 2),
        "limit_pct": limit,
        "headroom_pct": round(limit - total, 2),
        "active_projects": {slug: p.get("budget_pct_weekly", 0) for slug, p in active.items()},
    }


# ---------------------------------------------------------------- commands

def cmd_init(args):
    ensure_private_root()
    if not (ROOT / "config.json").exists() or args.force:
        save_json(ROOT / "config.json", DEFAULT_CONFIG)
    private_parent(ROOT / "projects" / ".placeholder")
    print(f"initialized {ROOT} — edit config.json: account names, weekly budgets, reset day")


def cmd_register(args):
    if not math.isfinite(args.weekly_pct) or args.weekly_pct < 0:
        print(json.dumps({"verdict": "invalid",
                          "reason": "weekly_pct must be a finite non-negative number"}, indent=2))
        sys.exit(1)
    p = {
        "slug": args.project,
        "roots": args.root,
        "sessions": args.session or [],
        "budget_pct_weekly": args.weekly_pct,
        "accounts": args.accounts.split(",") if args.accounts else list(config()["accounts"]),
        "gpu_hours": {"day": args.gpu_day, "week": args.gpu_week, "month": args.gpu_month},
        "status": "active",
        "created": now_utc().isoformat(),
    }
    audit = portfolio_audit((args.project, p))
    if audit["verdict"] != "proceed" and not args.allow_overcommit:
        print(json.dumps({**audit, "reason": "active token allocations exceed the portfolio limit",
                          "override": "--allow-overcommit"}, indent=2))
        sys.exit(1)
    save_json(project_path(args.project) / "project.json", p)
    print(json.dumps(p, indent=2))


def cmd_portfolio_audit(args):
    audit = portfolio_audit()
    print(json.dumps(audit, indent=2))
    sys.exit(0 if audit["verdict"] == "proceed" else 1)


def cmd_usage(args):
    cfg = config()
    ru = real_utilization()
    if ru and not args.project:
        fresh = ""
        if ru.get("fetched_at_ms"):
            import datetime as _dt
            fresh = _dt.datetime.fromtimestamp(ru["fetched_at_ms"] / 1000).strftime(" (fetched %Y-%m-%d %H:%M)")
        print(f"Cached Claude usage — account {ru['account']}{fresh}:")
        print(f"  5-hour : {ru['five_hour']['pct']}%   resets {(ru['five_hour']['resets_at'] or '')[:16]}")
        print(f"  7-day  : {ru['seven_day']['pct']}%   resets {(ru['seven_day']['resets_at'] or '')[:16]}")
        for s in ru["scoped"]:
            print(f"  weekly {s['model']}: {s['pct']}% [{s['severity']}]{' ACTIVE' if s['active'] else ''}")
        print("  (below is the weighted-token PROXY, useful only for per-project relative split)\n")
    projects = {args.project: load_project(args.project)} if args.project else all_projects()
    since = None
    if args.days:
        since = now_utc() - dt.timedelta(days=args.days)
    report = {}
    for slug, p in projects.items():
        acct_name = active_account() or (p.get("accounts") or ["personal"])[0]
        acct = cfg["accounts"].get(acct_name, {})
        ws = week_start(acct)
        u = scan_usage(p.get("roots", []), since or ws, p.get("sessions"))
        budget = acct.get("weekly_weighted_budget", 0) * p.get("budget_pct_weekly", 0) / 100.0
        report[slug] = {
            "window_start": (since or ws).isoformat(),
            "account": acct_name,
            "weighted_used": round(u["weighted"]),
            "weekly_budget": round(budget),
            "pct_of_budget": round(100 * u["weighted"] / budget, 1) if budget else None,
            "raw": {k: u[k] for k in ("input", "output", "cache_creation", "cache_read")},
            "sessions": u["sessions"],
            "by_model": {k: round(v) for k, v in u["by_model"].items()},
        }
    print(json.dumps(report, indent=2))


def cmd_gate(args):
    cfg = config()
    p = load_project(args.project)
    allowed = p.get("accounts") or list(cfg["accounts"])
    active = active_account()
    acct_name = active if active in allowed else (allowed[0] if allowed else "unconfigured")
    acct = cfg["accounts"].get(acct_name, {})
    # 0) Optional cached Claude utilization (may be stale) — applies when this project's account is the active one
    ru = real_utilization()
    if ru and ru.get("account") == acct_name:
        fh = ru["five_hour"]["pct"] or 0
        wk = ru["seven_day"]["pct"] or 0
        if wk >= 100 or fh >= 100:
            which = "weekly" if wk >= 100 else "5-hour"
            resets = ru["seven_day"]["resets_at"] if wk >= 100 else ru["five_hour"]["resets_at"]
            v = {"verdict": "hard_stop", "reason": f"Cached Claude {which} limit reached ({max(wk, fh)}%)",
                 "account": acct_name, "resume_at": resets, "source": "cachedUsageUtilization",
                 "alternatives": [a for a in p.get("accounts", []) if a != acct_name]}
            print(json.dumps(v, indent=2)); sys.exit(2)
    # 1) hard stop: recorded rate-limit whose resume time is still in the future
    for ev in reversed(read_jsonl(ROOT / "events.jsonl")[-200:]):
        # an event with no recorded account is treated as the active account's
        if ev.get("type") == "rate_limit" and ev.get("account") in (acct_name, None):
            resume = parse_ts(ev.get("resume_at", ""))
            if resume and resume > now_utc():
                verdict = {"verdict": "hard_stop", "reason": "account window exhausted",
                           "account": acct_name, "resume_at": resume.isoformat(),
                           "alternatives": [a for a in p.get("accounts", []) if a != acct_name]}
                print(json.dumps(verdict, indent=2))
                sys.exit(2)
            break
    # 2) soft stop: project weekly % budget consumed
    ws = week_start(acct)
    u = scan_usage(p.get("roots", []), ws, p.get("sessions"))
    budget = acct.get("weekly_weighted_budget", 0) * p.get("budget_pct_weekly", 0) / 100.0
    used_pct = 100 * u["weighted"] / budget if budget else 0
    verdict = {"verdict": "proceed", "account": acct_name,
               "weighted_used": round(u["weighted"]), "weekly_budget": round(budget),
               "pct_of_budget": round(used_pct, 1), "week_start": ws.isoformat()}
    audit = portfolio_audit()
    verdict["portfolio"] = {k: audit[k] for k in ("verdict", "active_total_pct", "limit_pct")}
    if audit["verdict"] != "proceed":
        verdict["warnings"] = ["active token portfolio is overallocated; run portfolio-audit"]
    if budget <= 0:
        verdict["verdict"] = "soft_stop"
        verdict["reason"] = "project has no active weekly budget"
        verdict["alternatives"] = [a for a in p.get("accounts", []) if a != acct_name]
        print(json.dumps(verdict, indent=2))
        sys.exit(1)
    if u["weighted"] >= budget:
        verdict["verdict"] = "soft_stop"
        verdict["reason"] = "project weekly budget spent"
        verdict["alternatives"] = [a for a in p.get("accounts", []) if a != acct_name]
        print(json.dumps(verdict, indent=2))
        sys.exit(1)
    print(json.dumps(verdict, indent=2))


def cmd_event(args):
    ev = {"type": args.type, "ts": now_utc().isoformat(), "account": args.account or active_account(),
          "project": args.project, "note": args.note}
    if args.resume_at:
        ev["resume_at"] = args.resume_at
    elif args.type == "rate_limit":
        ev["resume_at"] = (now_utc() + dt.timedelta(hours=config()["session_window_hours"])).isoformat()
    append_jsonl(ROOT / "events.jsonl", ev)
    print(json.dumps(ev))


def cmd_switch(args):
    lock = {"account": args.account, "since": now_utc().isoformat(), "by": args.by or "manual"}
    save_json(ROOT / "account.lock", lock)
    append_jsonl(ROOT / "events.jsonl", {"type": "switch", "ts": lock["since"],
                                         "account": args.account, "by": lock["by"]})
    print(json.dumps(lock))
    print("Local account label changed; provider authentication is unchanged.", file=sys.stderr)


def cmd_session_log(args):
    rec = {"ts": now_utc().isoformat(), "account": active_account(),
           "summary": args.summary, "artifacts": args.artifact or []}
    append_jsonl(project_path(args.project) / "sessions.jsonl", rec)
    if args.artifact:
        art = project_path(args.project) / "artifacts.md"
        append_private_text(art, "".join(f"- {now_utc().date()} — {a}\n" for a in args.artifact))
    print(json.dumps(rec))


GPU_LEDGER = ROOT / "gpu" / "ledger.jsonl"

# Accepted `gpu-reconcile --outcome` values, in one place so the parser, the tests, and
# the docs cannot drift apart. The outcome is attribution, never accounting.
GPU_RECONCILE_OUTCOMES = (
    "completed",
    "failed",
    "failed_infrastructure",
    "killed",
    "cancelled",
    "launch_failed",
)


def _finite_number(value, name, *, positive=False):
    if value is None or isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be a number")
    value = float(value)
    if not math.isfinite(value) or (positive and value <= 0) or (not positive and value < 0):
        qualifier = "positive" if positive else "non-negative"
        raise ValueError(f"{name} must be a finite {qualifier} number")
    return value


def _identifier(value, name):
    value = str(value or "").strip()
    if not value or len(value) > 200 or any(ch in value for ch in "\r\n\0"):
        raise ValueError(f"{name} must be 1-200 printable characters")
    return value


def _gpu_scope(slug: str) -> dict[str, Any] | None:
    """Resolve and validate the optional aggregate GPU scope for a project.

    Args:
        slug: Registered project slug.

    Returns:
        The containing scope, or ``None`` when the project is unscoped.

    Raises:
        ValueError: If the global GPU scope configuration is invalid.
    """
    try:
        raw_config = json.loads((ROOT / "config.json").read_text())
    except FileNotFoundError:
        raw_config = DEFAULT_CONFIG
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError("config.json must be readable valid JSON") from exc
    if not isinstance(raw_config, dict):
        raise ValueError("config.json must contain an object")
    raw_scopes = raw_config.get("gpu_scopes", {})
    if not isinstance(raw_scopes, dict):
        raise ValueError("gpu_scopes must be an object")
    if not raw_scopes:
        return None

    registered = all_projects()
    claimed = {}
    resolved = None
    for raw_name, raw_scope in raw_scopes.items():
        if not isinstance(raw_name, str) or not raw_name.strip():
            raise ValueError("gpu scope names must be non-empty strings")
        name = raw_name.strip()
        if not isinstance(raw_scope, dict):
            raise ValueError(f"gpu scope '{name}' must be an object")
        raw_members = raw_scope.get("members")
        if not isinstance(raw_members, list) or not raw_members:
            raise ValueError(f"gpu scope '{name}' members must be a non-empty list")
        if any(not isinstance(member, str) or not member.strip()
               for member in raw_members):
            raise ValueError(f"gpu scope '{name}' members must be non-empty strings")
        members = [member.strip() for member in raw_members]
        if len(set(members)) != len(members):
            raise ValueError(f"gpu scope '{name}' contains duplicate members")

        admission_project = raw_scope.get("admission_project")
        if not isinstance(admission_project, str) or not admission_project.strip():
            raise ValueError(
                f"gpu scope '{name}' admission_project must be a non-empty string"
            )
        admission_project = admission_project.strip()
        if admission_project not in members:
            raise ValueError(
                f"gpu scope '{name}' admission_project must be one of its members"
            )
        capacity_mode = raw_scope.get("capacity_mode", "bounded")
        if capacity_mode not in {"bounded", "unlimited"}:
            raise ValueError(
                f"gpu scope '{name}' capacity_mode must be bounded or unlimited"
            )
        if capacity_mode == "unlimited":
            if not str(raw_scope.get("authorized_by") or "").strip():
                raise ValueError(
                    f"gpu scope '{name}' unlimited capacity requires authorized_by"
                )
            if not str(raw_scope.get("authorization_note") or "").strip():
                raise ValueError(
                    f"gpu scope '{name}' unlimited capacity requires authorization_note"
                )
        missing = sorted(set(members) - set(registered))
        if missing:
            raise ValueError(
                f"gpu scope '{name}' has unregistered members: {', '.join(missing)}"
            )
        for member in members:
            if member in claimed:
                raise ValueError(
                    f"gpu project '{member}' overlaps scopes "
                    f"'{claimed[member]}' and '{name}'"
                )
            claimed[member] = name
        if slug in members:
            resolved = {
                "name": name,
                "members": members,
                "admission_project": admission_project,
                "capacity_mode": capacity_mode,
            }
    return resolved


def _gpu_scope_reservation_owners(
    scope: dict[str, Any], events: list[dict[str, Any]]
) -> dict[str, str]:
    """Map scoped reservation IDs to their exact owning projects.

    Args:
        scope: Validated aggregate GPU scope.
        events: One locked snapshot of the global GPU ledger.

    Returns:
        Reservation ID to member-project mapping.

    Raises:
        ValueError: If an ID is invalid or occurs under multiple member projects.
    """
    members = set(scope["members"])
    owners = {}
    for event in events:
        if not isinstance(event, dict):
            raise ValueError(
                f"gpu scope '{scope['name']}' contains a non-object ledger row"
            )
        reservation_id = event.get("reservation_id")
        project = event.get("project")
        if event.get("type") != "reservation" or project not in members:
            continue
        try:
            normalized_id = _identifier(reservation_id, "reservation_id")
        except ValueError as exc:
            raise ValueError(
                f"gpu scope '{scope['name']}' contains an invalid reservation id"
            ) from exc
        if reservation_id != normalized_id:
            raise ValueError(
                f"gpu scope '{scope['name']}' contains an invalid reservation id"
            )
        owners.setdefault(reservation_id, set()).add(project)
    duplicates = {
        reservation_id: projects
        for reservation_id, projects in owners.items()
        if len(projects) > 1
    }
    if duplicates:
        details = "; ".join(
            f"{reservation_id} ({', '.join(sorted(projects))})"
            for reservation_id, projects in sorted(duplicates.items())
        )
        raise ValueError(
            f"gpu scope '{scope['name']}' has cross-member duplicate "
            f"reservation ids: {details}"
        )
    return {
        reservation_id: next(iter(projects))
        for reservation_id, projects in owners.items()
    }


def _gpu_numeric_anomaly(event, typ, reservation_id):
    """Return the first invalid numeric field in a typed GPU ledger row."""
    fields = {
        "reservation": (
            ("gpus", True, False),
            ("hours", True, False),
            ("gpu_hours", True, False),
            ("estimated_cost", False, True),
            ("disk_gb", False, False),
        ),
        "reconcile": (
            ("actual_gpu_hours", False, False),
            ("actual_cost", False, False),
            ("retained_disk_gb", False, False),
        ),
        "disk_release": (("released_disk_gb", True, False),),
    }
    for name, positive, optional in fields[typ]:
        value = event.get(name)
        if optional and value is None:
            continue
        try:
            _finite_number(value, name, positive=positive)
        except ValueError:
            return f"invalid numeric {typ}:{reservation_id}:{name}"
    return None


def _usage_import_anomaly(event):
    """Return the first structural defect in one retroactive usage row."""
    usage_id = event.get("usage_id")
    try:
        if usage_id != _identifier(usage_id, "usage_id"):
            raise ValueError
    except ValueError:
        return "invalid usage id in usage import"
    try:
        if event.get("job") != _identifier(event.get("job"), "job"):
            raise ValueError
    except ValueError:
        return f"invalid job in usage import:{usage_id}"
    for name in ("actual_gpu_hours", "actual_cost"):
        try:
            _finite_number(event.get(name), name)
        except ValueError:
            return f"invalid numeric usage import:{usage_id}:{name}"
    occurred_at = parse_ts(event.get("occurred_at", ""))
    if occurred_at is None or occurred_at.utcoffset() is None:
        return f"invalid occurred_at in usage import:{usage_id}"
    currency = event.get("currency")
    if (
        not isinstance(currency, str)
        or len(currency) != 3
        or not currency.isalpha()
        or currency != currency.upper()
    ):
        return f"invalid currency in usage import:{usage_id}"
    if event.get("outcome") not in GPU_RECONCILE_OUTCOMES:
        return f"invalid outcome in usage import:{usage_id}"
    try:
        if event.get("evidence") != _identifier(event.get("evidence"), "evidence"):
            raise ValueError
    except ValueError:
        return f"invalid evidence in usage import:{usage_id}"
    return None


def _gpu_replay(slug, events=None):
    """Replay reservation, import, and legacy GPU accounting rows."""
    events = read_jsonl(GPU_LEDGER) if events is None else events
    reservations = {}
    reconciliations = {}
    disk_releases = {}
    legacy = []
    anomalies = []
    seen = {
        typ: set()
        for typ in ("reservation", "reconcile", "disk_release", "usage_import")
    }
    for e in events:
        if not isinstance(e, dict):
            anomalies.append("non-object ledger row")
            continue
        if e.get("project") != slug:
            continue
        typ = e.get("type")
        rid = e.get("reservation_id")
        if typ == "usage_import":
            usage_id = e.get("usage_id")
            if anomaly := _usage_import_anomaly(e):
                anomalies.append(anomaly)
                continue
            if usage_id in seen[typ]:
                anomalies.append(f"duplicate usage import:{usage_id}")
                continue
            seen[typ].add(usage_id)
            legacy.append(e)
        elif typ in seen:
            try:
                normalized_id = _identifier(rid, "reservation_id")
            except ValueError:
                anomalies.append(f"invalid reservation id in {typ}")
                continue
            if rid != normalized_id:
                anomalies.append(f"invalid reservation id in {typ}")
                continue
            if rid in seen[typ]:
                label = (
                    "reconciliation"
                    if typ == "reconcile"
                    else typ.replace("_", " ")
                )
                anomalies.append(f"duplicate {label}:{rid}")
                continue
            seen[typ].add(rid)
            if anomaly := _gpu_numeric_anomaly(e, typ, rid):
                anomalies.append(anomaly)
                continue
            if typ == "reservation":
                reservations[rid] = e
            elif typ == "reconcile":
                reconciliations[rid] = e
            else:
                disk_releases[rid] = e
        elif "gpu_hours" in e:
            value = e.get("gpu_hours")
            if (isinstance(value, bool) or not isinstance(value, (int, float))
                    or not math.isfinite(float(value))):
                anomalies.append("invalid numeric legacy usage:gpu_hours")
            else:
                legacy.append(e)
    for rid in reconciliations:
        if rid not in reservations:
            anomalies.append(f"orphan reconciliation:{rid}")
    for rid in disk_releases:
        if rid not in reconciliations:
            anomalies.append(f"orphan disk release:{rid}")
    return reservations, reconciliations, disk_releases, legacy, anomalies


def _gpu_snapshot(slug, since, events=None):
    """Committed usage in a rolling window: completed actuals plus active holds."""
    reservations, reconciliations, disk_releases, legacy, anomalies = _gpu_replay(slug, events)
    structural_anomalies = sorted(set(anomalies))
    completed = 0.0
    completed_cost = 0.0
    reserved = 0.0
    reserved_cost = 0.0
    active_gpus = 0.0
    active_disk_gb = 0.0

    for rid, reservation in reservations.items():
        rec = reconciliations.get(rid)
        if rec:
            rec_ts = parse_ts(rec.get("ts", ""))
            if rec_ts and rec_ts >= since:
                completed += max(0.0, float(rec.get("actual_gpu_hours", 0) or 0))
                completed_cost += max(0.0, float(rec.get("actual_cost", 0) or 0))
            if rid not in disk_releases:
                active_disk_gb += max(0.0, float(rec.get("retained_disk_gb", 0) or 0))
            continue
        # An unreconciled hold remains active even if it is older than this window.
        reserved += max(0.0, float(reservation.get("gpu_hours", 0) or 0))
        reserved_cost += max(0.0, float(reservation.get("estimated_cost", 0) or 0))
        active_gpus += max(0.0, float(reservation.get("gpus", 0) or 0))
        active_disk_gb += max(0.0, float(reservation.get("disk_gb", 0) or 0))

    imported = [e for e in legacy if e.get("type") == "usage_import"]
    legacy_rows = [e for e in legacy if e.get("type") != "usage_import"]
    legacy_raw = sum(float(e.get("gpu_hours", 0) or 0) for e in legacy_rows
                     if (ts := parse_ts(e.get("ts", ""))) and ts >= since)
    legacy_used = max(0.0, legacy_raw)
    if legacy_raw < 0:
        anomalies.append("legacy rolling usage clamped at zero")
    completed += legacy_used
    for event in imported:
        occurred_at = parse_ts(event.get("occurred_at", ""))
        if occurred_at and occurred_at >= since:
            completed += float(event["actual_gpu_hours"])
            completed_cost += float(event["actual_cost"])
    return {
        "completed_gpu_hours": completed,
        "reserved_gpu_hours": reserved,
        "committed_gpu_hours": completed + reserved,
        "completed_cost": completed_cost,
        "reserved_cost": reserved_cost,
        "committed_cost": completed_cost + reserved_cost,
        "active_gpus": active_gpus,
        "active_disk_gb": active_disk_gb,
        "active_reservations": len(reservations.keys() - reconciliations.keys()),
        "anomalies": sorted(set(anomalies)),
        "structural_anomalies": structural_anomalies,
    }


def _gpu_scope_snapshot(
    members: list[str], since: dt.datetime, events: list[dict[str, Any]]
) -> dict[str, Any]:
    """Sum exact-project accounting from one locked ledger read.

    Args:
        members: Project slugs whose accounting is aggregated.
        since: Inclusive start of the rolling accounting window.
        events: One locked snapshot of the global GPU ledger.

    Returns:
        Aggregate usage, cost, concurrency, disk, and anomaly fields.
    """
    numeric_fields = (
        "completed_gpu_hours", "reserved_gpu_hours", "committed_gpu_hours",
        "completed_cost", "reserved_cost", "committed_cost", "active_gpus",
        "active_disk_gb", "active_reservations",
    )
    total = {field: 0 for field in numeric_fields}
    anomalies = []
    structural_anomalies = []
    for member in members:
        snapshot = _gpu_snapshot(member, since, events)
        for field in numeric_fields:
            total[field] += snapshot[field]
        anomalies.extend(
            f"{member}: {anomaly}" for anomaly in snapshot["anomalies"]
        )
        structural_anomalies.extend(
            f"{member}: {anomaly}"
            for anomaly in snapshot["structural_anomalies"]
        )
    usage_owners = {}
    for event in events:
        if (
            isinstance(event, dict)
            and event.get("type") == "usage_import"
            and event.get("project") in members
        ):
            usage_owners.setdefault(event.get("usage_id"), set()).add(
                event.get("project")
            )
    for usage_id, owners in usage_owners.items():
        if len(owners) > 1:
            structural_anomalies.append(
                "cross-member duplicate usage import:"
                f"{usage_id} ({', '.join(sorted(owners))})"
            )
    total["anomalies"] = sorted(set(anomalies))
    total["structural_anomalies"] = sorted(set(structural_anomalies))
    return total


def _gpu_hours(slug, since):
    """Backward-compatible committed GPU-hours used by the dashboard surfaces."""
    return _gpu_snapshot(slug, since)["committed_gpu_hours"]


def _gpu_policy(project):
    policy = project.get("gpu_policy") or {}
    scope = _gpu_scope(project.get("slug")) if project.get("slug") else None
    mode = policy.get("mode", "bounded")
    if scope and scope.get("capacity_mode") == "unlimited":
        mode = "unlimited"
    if mode == "unlimited":
        return {
            "mode": "unlimited",
            "scope": scope.get("name") if scope else None,
            "max_concurrent_gpus": None,
            "max_grant_gpu_hours": None,
            "max_grant_wall_hours": None,
            "cash_month": None,
            "cash_currency": (policy.get("cash") or {}).get("currency", "GBP"),
            "max_disk_per_job_gb": None,
            "max_active_disk_gb": None,
        }
    return {
        "mode": "bounded",
        "scope": scope.get("name") if scope else None,
        "max_concurrent_gpus": policy.get("max_concurrent_gpus"),
        "max_grant_gpu_hours": policy.get("max_grant_gpu_hours"),
        "max_grant_wall_hours": policy.get("max_grant_wall_hours"),
        "cash_month": (policy.get("cash") or {}).get("month"),
        "cash_currency": (policy.get("cash") or {}).get("currency", "GBP"),
        "max_disk_per_job_gb": (policy.get("disk") or {}).get("max_per_job_gb"),
        "max_active_disk_gb": (policy.get("disk") or {}).get("max_active_gb"),
    }


def _evaluate_gpu_request(
    project: dict[str, Any],
    request: dict[str, Any],
    events: list[dict[str, Any]] | None = None,
    members: list[str] | None = None,
) -> dict[str, Any]:
    """Evaluate one request using the admission project's limits.

    Args:
        project: Project whose limits govern the admission decision.
        request: Normalized GPU request fields.
        events: Optional single snapshot of the global GPU ledger.
        members: Optional project slugs whose accounting is aggregated.

    Returns:
        Structured proceed or soft-stop decision with accounting details.
    """
    n = now_utc()
    windows = {"day": n - dt.timedelta(days=1), "week": n - dt.timedelta(days=7),
               "month": n - dt.timedelta(days=30)}
    policy = _gpu_policy(project)
    limits = {} if policy["mode"] == "unlimited" else project.get("gpu_hours") or {}
    request_hours = request["gpu_hours"]
    verdict = {
        "verdict": "proceed",
        "request": request,
        "policy": {"mode": policy["mode"], "scope": policy["scope"]},
        "windows": {},
        "checks": {},
    }
    reasons = []
    snapshots = {}
    for name, since in windows.items():
        snap = (
            _gpu_scope_snapshot(members, since, events)
            if members is not None
            else _gpu_snapshot(project["slug"], since, events)
        )
        snapshots[name] = snap
        budget = limits.get(name)
        verdict["windows"][name] = {
            "completed": round(snap["completed_gpu_hours"], 4),
            "reserved": round(snap["reserved_gpu_hours"], 4),
            "committed": round(snap["committed_gpu_hours"], 4),
            "budget": budget,
            "after_request": round(snap["committed_gpu_hours"] + request_hours, 4),
        }
        if budget is not None and snap["committed_gpu_hours"] + request_hours > float(budget):
            reasons.append(f"gpu {name} budget would be exceeded")

    month = snapshots["month"]
    if policy["max_grant_gpu_hours"] is not None and request_hours > float(policy["max_grant_gpu_hours"]):
        reasons.append("per-grant GPU-hour limit would be exceeded")
    if (policy["max_grant_wall_hours"] is not None and request["hours"] is not None
            and request["hours"] > float(policy["max_grant_wall_hours"])):
        reasons.append("per-grant wall-hour limit would be exceeded")
    concurrency_after = (
        month["active_gpus"] + request["gpus"]
        if request["gpus"] is not None else None
    )
    verdict["checks"]["concurrency"] = {
        "active": month["active_gpus"], "after_request": concurrency_after,
        "limit": policy["max_concurrent_gpus"],
    }
    if (policy["max_concurrent_gpus"] is not None
            and concurrency_after is not None
            and concurrency_after > float(policy["max_concurrent_gpus"])):
        reasons.append("concurrent GPU limit would be exceeded")
    elif policy["max_concurrent_gpus"] is not None and concurrency_after is None:
        verdict.setdefault("unchecked", []).append(
            "concurrency requires both --gpus and --hours in preview mode"
        )

    disk_after = month["active_disk_gb"] + request.get("disk_gb", 0)
    verdict["checks"]["disk"] = {
        "active_gb": month["active_disk_gb"], "after_request_gb": disk_after,
        "per_job_limit_gb": policy["max_disk_per_job_gb"],
        "active_limit_gb": policy["max_active_disk_gb"],
    }
    if (policy["max_disk_per_job_gb"] is not None
            and request.get("disk_gb", 0) > float(policy["max_disk_per_job_gb"])):
        reasons.append("per-job disk limit would be exceeded")
    if policy["max_active_disk_gb"] is not None and disk_after > float(policy["max_active_disk_gb"]):
        reasons.append("active disk limit would be exceeded")

    estimated_cost = request.get("estimated_cost")
    if policy["cash_month"] is not None and estimated_cost is None:
        reasons.append("cash-controlled project requires --estimated-cost")
    if (policy["cash_month"] is not None
            and request.get("currency", "").upper() != str(policy["cash_currency"]).upper()):
        reasons.append(f"cash estimate currency must be {policy['cash_currency']}")
    cost_after = month["committed_cost"] + (estimated_cost or 0)
    verdict["checks"]["cash"] = {
        "currency": policy["cash_currency"], "completed": month["completed_cost"],
        "reserved": month["reserved_cost"], "after_request": cost_after,
        "month_limit": policy["cash_month"],
    }
    if policy["cash_month"] is not None and cost_after > float(policy["cash_month"]):
        reasons.append("monthly cash limit would be exceeded")

    anomalies = sorted({a for snap in snapshots.values() for a in snap["anomalies"]})
    if anomalies:
        verdict["ledger_anomalies"] = anomalies
    structural_anomalies = sorted({
        anomaly
        for snapshot in snapshots.values()
        for anomaly in snapshot["structural_anomalies"]
    })
    if structural_anomalies:
        reason = "gpu ledger structural anomalies require repair"
        verdict["verdict"] = "invalid"
        verdict["reasons"] = [reason]
        verdict["reason"] = reason
        verdict["ledger_anomalies"] = sorted(set(
            verdict.get("ledger_anomalies", []) + structural_anomalies
        ))
    elif reasons:
        verdict["verdict"] = "soft_stop"
        verdict["reasons"] = reasons
        verdict["reason"] = reasons[0]
    return verdict


def _request_from_args(args, *, advisory=False):
    if advisory:
        gpu_hours = _finite_number(args.request, "request", positive=True)
        if (args.gpus is None) != (args.hours is None):
            raise ValueError("preview requires both --gpus and --hours, or neither")
        if args.gpus is None:
            gpus = None
            hours = None
        else:
            gpus = _finite_number(args.gpus, "gpus", positive=True)
            hours = _finite_number(args.hours, "hours", positive=True)
            if not math.isclose(gpus * hours, gpu_hours, rel_tol=1e-9, abs_tol=1e-9):
                raise ValueError("request must equal gpus multiplied by hours")
    else:
        gpus = _finite_number(args.gpus, "gpus", positive=True)
        hours = _finite_number(args.hours, "hours", positive=True)
        gpu_hours = gpus * hours
    cost = None if args.estimated_cost is None else _finite_number(args.estimated_cost, "estimated_cost")
    disk = _finite_number(args.disk_gb or 0, "disk_gb")
    currency = str(args.currency or "").strip().upper()
    if len(currency) != 3 or not currency.isalpha():
        raise ValueError("currency must be a three-letter code")
    return {"gpus": gpus, "hours": hours, "gpu_hours": gpu_hours,
            "estimated_cost": cost, "currency": currency, "disk_gb": disk}


def cmd_gpu_log(args):
    try:
        job = _identifier(args.job, "job")
        gpus = _finite_number(args.gpus, "gpus", positive=True)
        hours = _finite_number(args.hours, "hours", positive=True)
    except ValueError as exc:
        print(json.dumps({"verdict": "invalid", "reason": str(exc)}, indent=2))
        sys.exit(1)
    ev = {"type": "legacy_usage", "ts": now_utc().isoformat(), "project": args.project,
          "job": job, "gpus": gpus, "hours": hours, "gpu_hours": gpus * hours,
          "note": args.note}
    with gpu_ledger_lock():
        append_jsonl(GPU_LEDGER, ev)
    print(json.dumps(ev))


def cmd_gpu_import_usage(args):
    """Append one replay-safe historical usage event without creating a hold."""
    project = load_project(args.project)
    policy = _gpu_policy(project)
    try:
        usage_id = _identifier(args.usage_id, "usage_id")
        job = _identifier(args.job, "job")
        actual_hours = _finite_number(args.actual_gpu_hours, "actual_gpu_hours")
        actual_cost = (
            None
            if args.actual_cost is None
            else _finite_number(args.actual_cost, "actual_cost")
        )
        evidence = _identifier(args.evidence, "evidence")
        occurred_at = parse_ts(args.occurred_at)
        if occurred_at is None or occurred_at.utcoffset() is None:
            raise ValueError("occurred_at must be an ISO timestamp with timezone")
        if occurred_at > now_utc():
            raise ValueError("occurred_at cannot be in the future")
        currency = str(args.currency or "").strip().upper()
        if len(currency) != 3 or not currency.isalpha():
            raise ValueError("currency must be a three-letter code")
        scope = _gpu_scope(args.project)
    except ValueError as exc:
        print(json.dumps({"verdict": "invalid", "reason": str(exc)}, indent=2))
        sys.exit(1)
    if policy["cash_month"] is not None and actual_cost is None:
        print(json.dumps({
            "verdict": "invalid",
            "reason": "cash-controlled project requires --actual-cost",
        }, indent=2))
        sys.exit(1)
    if (
        policy["cash_month"] is not None
        and currency != str(policy["cash_currency"]).upper()
    ):
        print(json.dumps({
            "verdict": "invalid",
            "reason": f"usage currency must be {policy['cash_currency']}",
        }, indent=2))
        sys.exit(1)
    if scope and args.project != scope["admission_project"]:
        print(json.dumps({
            "verdict": "invalid",
            "reason": (
                f"gpu scope '{scope['name']}' imports usage only through "
                f"project '{scope['admission_project']}'"
            ),
        }, indent=2))
        sys.exit(1)
    event = {
        "type": "usage_import",
        "schema_version": 3,
        "ts": now_utc().isoformat(),
        "occurred_at": occurred_at.astimezone(dt.timezone.utc).isoformat(),
        "project": args.project,
        "usage_id": usage_id,
        "job": job,
        "actual_gpu_hours": actual_hours,
        "actual_cost": actual_cost or 0.0,
        "currency": currency,
        "outcome": args.outcome,
        "evidence": evidence,
        "note": args.note,
    }
    comparable = (
        "occurred_at", "project", "usage_id", "job", "actual_gpu_hours",
        "actual_cost", "currency", "outcome", "evidence", "note",
    )
    with gpu_ledger_lock():
        try:
            events = read_jsonl(GPU_LEDGER, tolerate_torn_final=False)
        except ValueError as exc:
            print(json.dumps({"verdict": "invalid", "reason": str(exc)}, indent=2))
            sys.exit(1)
        members = scope["members"] if scope else [args.project]
        structural_anomalies = sorted({
            f"{member}: {anomaly}" if scope else anomaly
            for member in members
            for anomaly in _gpu_replay(member, events)[4]
        })
        if structural_anomalies:
            print(json.dumps({
                "verdict": "invalid",
                "reason": "gpu ledger structural anomalies require repair",
                "ledger_anomalies": structural_anomalies,
            }, indent=2))
            sys.exit(1)
        existing = [
            candidate
            for candidate in events
            if isinstance(candidate, dict)
            and candidate.get("type") == "usage_import"
            and candidate.get("usage_id") == usage_id
        ]
        if existing:
            prior = existing[0]
            if (
                prior.get("project") == args.project
                and all(prior.get(key) == event.get(key) for key in comparable)
            ):
                print(json.dumps({
                    "verdict": "already_imported",
                    "usage": prior,
                }, indent=2))
                return
            print(json.dumps({
                "verdict": "invalid",
                "reason": "usage id conflicts with different import",
                "usage_id": usage_id,
            }, indent=2))
            sys.exit(1)
        append_jsonl(GPU_LEDGER, event)
    print(json.dumps({"verdict": "imported", "usage": event}, indent=2))


def cmd_gpu_gate(args):
    project = load_project(args.project)
    try:
        request = _request_from_args(args, advisory=True)
        scope = _gpu_scope(args.project)
    except ValueError as exc:
        print(json.dumps({"verdict": "invalid", "reason": str(exc)}, indent=2))
        sys.exit(1)
    if scope and args.project != scope["admission_project"]:
        print(json.dumps({
            "verdict": "invalid",
            "reason": (
                f"gpu scope '{scope['name']}' admits new work only through "
                f"project '{scope['admission_project']}'"
            ),
        }, indent=2))
        sys.exit(1)
    try:
        with gpu_ledger_lock():
            events = read_jsonl(GPU_LEDGER)
            if scope:
                _gpu_scope_reservation_owners(scope, events)
            verdict = _evaluate_gpu_request(
                project, request, events, scope["members"] if scope else None
            )
    except ValueError as exc:
        print(json.dumps({"verdict": "invalid", "reason": str(exc)}, indent=2))
        sys.exit(1)
    if scope:
        verdict["gpu_scope"] = scope
    verdict["mode"] = "advisory_read_only"
    verdict["next_action"] = "use gpu-reserve for atomic admission before launch"
    print(json.dumps(verdict, indent=2))
    sys.exit(0 if verdict["verdict"] == "proceed" else 1)


def cmd_gpu_reserve(args):
    project = load_project(args.project)
    try:
        job = _identifier(args.job, "job")
        request = _request_from_args(args)
        reservation_id = _identifier(args.reservation_id or job, "reservation_id")
        scope = _gpu_scope(args.project)
    except ValueError as exc:
        print(json.dumps({"verdict": "invalid", "reason": str(exc)}, indent=2))
        sys.exit(1)
    with gpu_ledger_lock():
        try:
            events = read_jsonl(GPU_LEDGER, tolerate_torn_final=False)
            owners = _gpu_scope_reservation_owners(scope, events) if scope else {}
        except ValueError as exc:
            print(json.dumps({"verdict": "invalid", "reason": str(exc)}, indent=2))
            sys.exit(1)
        members = scope["members"] if scope else [args.project]
        structural_anomalies = sorted({
            f"{member}: {anomaly}" if scope else anomaly
            for member in members
            for anomaly in _gpu_replay(member, events)[4]
        })
        if structural_anomalies:
            print(json.dumps({
                "verdict": "invalid",
                "reason": "gpu ledger structural anomalies require repair",
                "ledger_anomalies": structural_anomalies,
            }, indent=2))
            sys.exit(1)
        reservations, reconciliations, _, _, _ = _gpu_replay(args.project, events)
        if reservation_id in reservations:
            existing = reservations[reservation_id]
            expected = {
                key: request[key]
                for key in (
                    "gpus", "hours", "gpu_hours", "estimated_cost", "currency",
                    "disk_gb",
                )
            }
            if scope and args.project != scope["admission_project"]:
                expected = {"job": job, **expected, "note": args.note}
            actual = {k: existing.get(k) for k in expected}
            if actual == expected and reservation_id not in reconciliations:
                print(json.dumps(
                    {"verdict": "already_reserved", "reservation": existing},
                    indent=2,
                ))
                return
            reason = (
                "reservation id already reconciled"
                if reservation_id in reconciliations
                else "reservation id conflicts with different request"
            )
            print(json.dumps({"verdict": "invalid", "reason": reason,
                              "reservation_id": reservation_id}, indent=2))
            sys.exit(1)
        if scope and args.project != scope["admission_project"]:
            print(json.dumps({
                "verdict": "invalid",
                "reason": (
                    f"gpu scope '{scope['name']}' admits new reservations only "
                    f"through project '{scope['admission_project']}'"
                ),
            }, indent=2))
            sys.exit(1)
        if scope and reservation_id in owners:
            print(json.dumps({
                "verdict": "invalid",
                "reason": (
                    f"reservation id belongs to scoped project "
                    f"'{owners[reservation_id]}'"
                ),
                "reservation_id": reservation_id,
            }, indent=2))
            sys.exit(1)
        verdict = _evaluate_gpu_request(
            project, request, events, scope["members"] if scope else None
        )
        if scope:
            verdict["gpu_scope"] = scope
        if verdict["verdict"] != "proceed":
            print(json.dumps(verdict, indent=2))
            sys.exit(1)
        ev = {"type": "reservation", "schema_version": 2, "ts": now_utc().isoformat(),
              "project": args.project, "reservation_id": reservation_id, "job": job,
              **request, "note": args.note}
        append_jsonl(GPU_LEDGER, ev)
    print(json.dumps({"verdict": "reserved", "reservation": ev}, indent=2))


def cmd_gpu_reconcile(args):
    project = load_project(args.project)
    policy = _gpu_policy(project)
    try:
        reservation_id = _identifier(args.reservation_id, "reservation_id")
        actual_hours = _finite_number(args.actual_gpu_hours, "actual_gpu_hours")
        actual_cost = None if args.actual_cost is None else _finite_number(args.actual_cost, "actual_cost")
        retained_disk_gb = _finite_number(args.retained_disk_gb, "retained_disk_gb")
    except ValueError as exc:
        print(json.dumps({"verdict": "invalid", "reason": str(exc)}, indent=2))
        sys.exit(1)
    if policy["cash_month"] is not None and actual_cost is None:
        print(json.dumps({"verdict": "invalid",
                          "reason": "cash-controlled project requires --actual-cost"}, indent=2))
        sys.exit(1)
    with gpu_ledger_lock():
        events = read_jsonl(GPU_LEDGER)
        reservations, reconciliations, _, _, _ = _gpu_replay(args.project, events)
        reservation = reservations.get(reservation_id)
        if not reservation:
            print(json.dumps({"verdict": "invalid", "reason": "unknown reservation id"}, indent=2))
            sys.exit(1)
        reserved_disk_gb = float(reservation.get("disk_gb", 0) or 0)
        if retained_disk_gb > reserved_disk_gb:
            print(json.dumps({"verdict": "invalid",
                              "reason": "retained disk exceeds the reserved disk claim"}, indent=2))
            sys.exit(1)
        ev = {"type": "reconcile", "schema_version": 2, "ts": now_utc().isoformat(),
              "project": args.project, "reservation_id": reservation_id,
              "job": reservation.get("job"), "actual_gpu_hours": actual_hours,
              "actual_cost": actual_cost or 0.0, "currency": reservation.get("currency", "GBP"),
              "retained_disk_gb": retained_disk_gb,
              "outcome": args.outcome, "note": args.note}
        existing = reconciliations.get(reservation_id)
        if existing:
            comparable = ("project", "reservation_id", "job", "actual_gpu_hours",
                          "actual_cost", "currency", "retained_disk_gb", "outcome", "note")
            if all(existing.get(k) == ev.get(k) for k in comparable):
                print(json.dumps({"verdict": "already_reconciled", "reconciliation": existing}, indent=2))
                return
            print(json.dumps({"verdict": "invalid", "reason": "conflicting reconciliation"}, indent=2))
            sys.exit(1)
        append_jsonl(GPU_LEDGER, ev)
    overrun = actual_hours > float(reservation.get("gpu_hours", 0) or 0)
    print(json.dumps({"verdict": "reconciled", "overrun": overrun, "reconciliation": ev}, indent=2))


def cmd_gpu_disk_release(args):
    load_project(args.project)
    try:
        reservation_id = _identifier(args.reservation_id, "reservation_id")
    except ValueError as exc:
        print(json.dumps({"verdict": "invalid", "reason": str(exc)}, indent=2))
        sys.exit(1)
    with gpu_ledger_lock():
        events = read_jsonl(GPU_LEDGER)
        reservations, reconciliations, disk_releases, _, _ = _gpu_replay(
            args.project, events
        )
        if reservation_id not in reservations or reservation_id not in reconciliations:
            print(json.dumps({"verdict": "invalid",
                              "reason": "disk release requires a reconciled reservation"}, indent=2))
            sys.exit(1)
        retained = float(reconciliations[reservation_id].get("retained_disk_gb", 0) or 0)
        if retained <= 0:
            print(json.dumps({"verdict": "invalid",
                              "reason": "reservation has no retained disk"}, indent=2))
            sys.exit(1)
        if reservation_id in disk_releases:
            print(json.dumps({"verdict": "already_released",
                              "release": disk_releases[reservation_id]}, indent=2))
            return
        ev = {"type": "disk_release", "schema_version": 2,
              "ts": now_utc().isoformat(), "project": args.project,
              "reservation_id": reservation_id,
              "job": reservations[reservation_id].get("job"),
              "released_disk_gb": retained, "evidence": args.evidence,
              "note": args.note}
        append_jsonl(GPU_LEDGER, ev)
    print(json.dumps({"verdict": "released", "release": ev}, indent=2))


def cmd_gpu_policy(args):
    project = load_project(args.project)
    policy = project.setdefault("gpu_policy", {})
    previous = {
        "gpu_hours": json.loads(json.dumps(project.get("gpu_hours", {}))),
        "gpu_policy": json.loads(json.dumps(policy)),
    }
    bounded_values = (
        args.max_concurrent_gpus,
        args.max_grant_gpu_hours,
        args.max_grant_wall_hours,
        args.cash_month,
        args.max_disk_per_job_gb,
        args.max_active_disk_gb,
    )
    if args.unlimited:
        if any(value is not None for value in bounded_values):
            print(json.dumps({
                "verdict": "invalid",
                "reason": "--unlimited cannot be combined with numeric limits",
            }, indent=2))
            sys.exit(1)
        if not args.authorized_by.strip() or not args.note.strip():
            print(json.dumps({
                "verdict": "invalid",
                "reason": "--unlimited requires --authorized-by and --note",
            }, indent=2))
            sys.exit(1)
        currency = (args.currency or (policy.get("cash") or {}).get("currency") or "GBP").upper()
        project["gpu_hours"] = {"day": None, "week": None, "month": None}
        policy.clear()
        policy.update({
            "mode": "unlimited",
            "authorized_by": args.authorized_by.strip(),
            "authorization_note": args.note.strip(),
            "authorized_at": now_utc().isoformat(),
            "max_concurrent_gpus": None,
            "max_grant_gpu_hours": None,
            "max_grant_wall_hours": None,
            "cash": {"currency": currency, "month": None},
            "disk": {"max_per_job_gb": None, "max_active_gb": None},
        })
        save_json(project_path(args.project) / "project.json", project)
        print(json.dumps({
            "verdict": "updated",
            "project": args.project,
            "mode": "unlimited",
            "previous": previous,
            "gpu_hours": project["gpu_hours"],
            "gpu_policy": policy,
        }, indent=2))
        return

    cash = policy.setdefault("cash", {})
    disk = policy.setdefault("disk", {})
    try:
        updates = {
            "max_concurrent_gpus": args.max_concurrent_gpus,
            "max_grant_gpu_hours": args.max_grant_gpu_hours,
            "max_grant_wall_hours": args.max_grant_wall_hours,
        }
        for key, value in updates.items():
            if value is not None:
                policy[key] = _finite_number(value, key, positive=True)
        if args.cash_month is not None:
            cash["month"] = _finite_number(args.cash_month, "cash_month", positive=True)
        if args.currency:
            cash["currency"] = args.currency.upper()
        if args.max_disk_per_job_gb is not None:
            disk["max_per_job_gb"] = _finite_number(args.max_disk_per_job_gb, "max_disk_per_job_gb", positive=True)
        if args.max_active_disk_gb is not None:
            disk["max_active_gb"] = _finite_number(args.max_active_disk_gb, "max_active_disk_gb", positive=True)
    except ValueError as exc:
        print(json.dumps({"verdict": "invalid", "reason": str(exc)}, indent=2))
        sys.exit(1)
    save_json(project_path(args.project) / "project.json", project)
    print(json.dumps({"project": args.project, "gpu_policy": policy}, indent=2))


def cmd_dashboard(args):
    cfg = config()
    lines = [f"# Oikonomos Ledger — {now_utc().isoformat()}",
             f"Active account: **{active_account() or 'unknown (run switch)'}**", ""]
    for slug, p in all_projects().items():
        acct_name = active_account() or (p.get("accounts") or ["personal"])[0]
        acct = cfg["accounts"].get(acct_name, {})
        u = scan_usage(p.get("roots", []), week_start(acct), p.get("sessions"))
        budget = acct.get("weekly_weighted_budget", 0) * p.get("budget_pct_weekly", 0) / 100.0
        pct = f"{100 * u['weighted'] / budget:.0f}%" if budget else "n/a"
        n = now_utc()
        gpu = {w: _gpu_snapshot(slug, n - dt.timedelta(days=d))
               for w, d in (("day", 1), ("week", 7), ("month", 30))}
        glim = p.get("gpu_hours", {})
        sess = read_jsonl(project_path(slug) / "sessions.jsonl")
        last = sess[-1]["ts"][:16] if sess else "never"
        lines += [f"## {slug}  ({p.get('status', '?')})",
                  f"- tokens this week: {round(u['weighted']):,} / {round(budget):,} weighted ({pct} of its {p.get('budget_pct_weekly')}% allocation)",
                  f"- gpu-hours committed (reserved): day {gpu['day']['committed_gpu_hours']:.1f} ({gpu['day']['reserved_gpu_hours']:.1f})/{glim.get('day')} · week {gpu['week']['committed_gpu_hours']:.1f} ({gpu['week']['reserved_gpu_hours']:.1f})/{glim.get('week')} · month {gpu['month']['committed_gpu_hours']:.1f} ({gpu['month']['reserved_gpu_hours']:.1f})/{glim.get('month')}",
                  f"- sessions logged: {len(sess)} (last {last})", ""]
    out = ROOT / "LEDGER.md"
    write_private_text(out, "\n".join(lines) + "\n")
    print(f"wrote {out}")


def cmd_panel(args):
    os.execv(sys.executable, [sys.executable, str(Path(__file__).parent / "panel.py")])


def cmd_web(args):
    os.execv(sys.executable, [sys.executable, str(Path(__file__).parent / "webui.py")])


def main():
    ap = argparse.ArgumentParser(prog="butler")
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("init"); s.add_argument("--force", action="store_true"); s.set_defaults(f=cmd_init)

    s = sub.add_parser("register")
    s.add_argument("--project", required=True)
    s.add_argument("--root", action="append", required=True, help="repeatable: cwd roots whose sessions belong to this project")
    s.add_argument("--session", action="append", help="repeatable: session-id (prefix ok) bound to this project — the attribution unit when all sessions share one cwd")
    s.add_argument("--weekly-pct", type=float, required=True)
    s.add_argument("--accounts", help="comma list, priority order")
    s.add_argument("--gpu-day", type=float, default=None)
    s.add_argument("--gpu-week", type=float, default=None)
    s.add_argument("--gpu-month", type=float, default=None)
    s.add_argument("--allow-overcommit", action="store_true",
                   help="explicitly permit active token allocations above portfolio_budget_pct")
    s.set_defaults(f=cmd_register)

    s = sub.add_parser("portfolio-audit")
    s.set_defaults(f=cmd_portfolio_audit)

    s = sub.add_parser("usage"); s.add_argument("--project"); s.add_argument("--days", type=int); s.set_defaults(f=cmd_usage)
    s = sub.add_parser("gate"); s.add_argument("--project", required=True); s.set_defaults(f=cmd_gate)

    s = sub.add_parser("event")
    s.add_argument("--type", required=True, choices=["rate_limit", "pause", "resume", "note"])
    s.add_argument("--project"); s.add_argument("--account"); s.add_argument("--note", default="")
    s.add_argument("--resume-at", help="ISO timestamp; for rate_limit defaults to now + session window")
    s.set_defaults(f=cmd_event)

    s = sub.add_parser("switch"); s.add_argument("--account", required=True); s.add_argument("--by"); s.set_defaults(f=cmd_switch)

    s = sub.add_parser("session-log")
    s.add_argument("--project", required=True); s.add_argument("--summary", required=True)
    s.add_argument("--artifact", action="append")
    s.set_defaults(f=cmd_session_log)

    s = sub.add_parser("gpu-log")
    s.add_argument("--project", required=True); s.add_argument("--job", required=True)
    s.add_argument("--gpus", type=float, required=True); s.add_argument("--hours", type=float, required=True)
    s.add_argument("--note", default="")
    s.set_defaults(f=cmd_gpu_log)

    s = sub.add_parser("gpu-import-usage")
    s.add_argument("--project", required=True)
    s.add_argument("--usage-id", required=True)
    s.add_argument("--job", required=True)
    s.add_argument("--occurred-at", required=True)
    s.add_argument("--actual-gpu-hours", type=float, required=True)
    s.add_argument("--actual-cost", type=float)
    s.add_argument("--currency", default="GBP")
    s.add_argument("--outcome", required=True, choices=GPU_RECONCILE_OUTCOMES)
    s.add_argument("--evidence", required=True)
    s.add_argument("--note", default="")
    s.set_defaults(f=cmd_gpu_import_usage)

    s = sub.add_parser("gpu-gate")
    s.add_argument("--project", required=True); s.add_argument("--request", type=float, required=True, help="gpu-hours about to be consumed")
    s.add_argument("--gpus", type=float); s.add_argument("--hours", type=float)
    s.add_argument("--estimated-cost", type=float); s.add_argument("--currency", default="GBP")
    s.add_argument("--disk-gb", type=float, default=0)
    s.set_defaults(f=cmd_gpu_gate)

    s = sub.add_parser("gpu-reserve")
    s.add_argument("--project", required=True); s.add_argument("--job", required=True)
    s.add_argument("--reservation-id", help="idempotency key; defaults to --job")
    s.add_argument("--gpus", type=float, required=True); s.add_argument("--hours", type=float, required=True)
    s.add_argument("--estimated-cost", type=float); s.add_argument("--currency", default="GBP")
    s.add_argument("--disk-gb", type=float, default=0); s.add_argument("--note", default="")
    s.set_defaults(f=cmd_gpu_reserve)

    s = sub.add_parser("gpu-reconcile")
    s.add_argument("--project", required=True); s.add_argument("--reservation-id", required=True)
    s.add_argument("--actual-gpu-hours", type=float, required=True)
    s.add_argument("--actual-cost", type=float)
    s.add_argument("--retained-disk-gb", type=float, default=0)
    s.add_argument("--outcome", default="completed", choices=GPU_RECONCILE_OUTCOMES,
                   help="failed_infrastructure = the provider/cluster/network/storage took "
                        "the run away; failed = the workload's own fault. Neither aliases "
                        "the other, and every outcome reconciles the same actual burn.")
    s.add_argument("--note", default="")
    s.set_defaults(f=cmd_gpu_reconcile)

    s = sub.add_parser("gpu-disk-release")
    s.add_argument("--project", required=True); s.add_argument("--reservation-id", required=True)
    s.add_argument("--evidence", required=True,
                   help="provider receipt, path, or URL proving the disk was deleted")
    s.add_argument("--note", default="")
    s.set_defaults(f=cmd_gpu_disk_release)

    s = sub.add_parser("gpu-policy")
    s.add_argument("--project", required=True)
    s.add_argument("--unlimited", action="store_true",
                   help="clear every GPU, grant, cash, concurrency, and disk ceiling")
    s.add_argument("--authorized-by", default="",
                   help="person exercising budget-policy authority for --unlimited")
    s.add_argument("--note", default="",
                   help="durable authorization rationale for --unlimited")
    s.add_argument("--max-concurrent-gpus", type=float)
    s.add_argument("--max-grant-gpu-hours", type=float)
    s.add_argument("--max-grant-wall-hours", type=float)
    s.add_argument("--cash-month", type=float); s.add_argument("--currency")
    s.add_argument("--max-disk-per-job-gb", type=float)
    s.add_argument("--max-active-disk-gb", type=float)
    s.set_defaults(f=cmd_gpu_policy)

    s = sub.add_parser("collect"); s.add_argument("--machine"); s.set_defaults(f=cmd_collect)

    s = sub.add_parser("panel"); s.set_defaults(f=cmd_panel)
    s = sub.add_parser("web"); s.set_defaults(f=cmd_web)

    s = sub.add_parser("dashboard"); s.set_defaults(f=cmd_dashboard)

    args = ap.parse_args()
    args.f(args)


if __name__ == "__main__":
    main()
