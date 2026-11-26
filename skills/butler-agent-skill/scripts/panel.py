#!/usr/bin/env python3
"""butler panel — interactive control panel for the cellar (rich, Python 3.14).

Views:  [1] Overview   [2] Projects   [3] Fleet   [4] Events
Keys :  1-4 switch view · j/k or ↑/↓ move · enter open project · b/esc back
        r recompute usage · q quit
Flags:  --once [view]   render a single frame to stdout (no interaction)
"""
import json
import os
import re
import select
import subprocess
import sys
import termios
import time
import tty as tty_mod
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import butler  # noqa: E402  (shared ledger helpers)

from rich import box  # noqa: E402
from rich.console import Console, Group  # noqa: E402
from rich.layout import Layout  # noqa: E402
from rich.live import Live  # noqa: E402
from rich.panel import Panel  # noqa: E402
from rich.table import Table  # noqa: E402
from rich.text import Text  # noqa: E402

ROOT = butler.ROOT
VIEWS = ["overview", "projects", "fleet", "events"]


# ---------------------------------------------------------------- data

def bar(pct, width=18):
    pct = 0 if pct is None else pct
    filled = int(min(pct, 100) / 100 * width)
    color = "green" if pct < 60 else "yellow" if pct < 90 else "red"
    over = " [bold red]OVER[/]" if pct > 100 else ""
    return f"[{color}]{'█' * filled}{'░' * (width - filled)}[/] {pct:5.1f}%{over}"


def fmt_tokens(n):
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n / 1_000:.0f}k"
    return str(int(n))


class State:
    def __init__(self):
        self.cfg = butler.config()
        self.view = "overview"
        self.sel = 0
        self.detail = None          # project slug when drilled in
        self.usage = {}             # slug -> scan result (lazy)
        self.machine_usage = None
        self.msg = ""

    # -- collectors -------------------------------------------------
    def projects(self):
        return butler.all_projects()

    def account(self):
        return butler.active_account() or "(no lock — run butler switch)"

    def acct_cfg(self, p=None):
        name = butler.active_account() or ((p or {}).get("accounts") or ["personal"])[0]
        return name, self.cfg["accounts"].get(name, {})

    def compute_usage(self, slug, p):
        name, acct = self.acct_cfg(p)
        ws = butler.week_start(acct)
        u = butler.scan_usage(p.get("roots", []), ws, p.get("sessions"))
        budget = acct.get("weekly_weighted_budget", 0) * p.get("budget_pct_weekly", 0) / 100.0
        self.usage[slug] = {"u": u, "budget": budget,
                            "pct": (100 * u["weighted"] / budget) if budget else None}

    def compute_all(self):
        for slug, p in self.projects().items():
            self.compute_usage(slug, p)
        name, acct = self.acct_cfg()
        ws = butler.week_start(acct)
        self.machine_usage = butler.scan_usage([r for p in butler.all_projects().values() for r in p.get("roots", [])], ws)

    def fleet(self):
        if not butler.config().get("inspect_local_processes", False):
            return []
        rows = []
        names = {}
        fleet_md = ROOT / "FLEET.md"
        if fleet_md.exists():
            for m in re.finditer(r"\|\s*(ttys\d+)\s*\|\s*\*?\*?([^|*]+?)\*?\*?\s*\|\s*([^|]+?)\s*\|",
                                 fleet_md.read_text()):
                names[m.group(1)] = (m.group(2).strip(), m.group(3).strip())
        out = subprocess.run(["ps", "-axo", "pid=,tty=,etime=,command="],
                             capture_output=True, text=True).stdout
        for line in out.splitlines():
            parts = line.split(None, 3)
            if len(parts) < 4 or not parts[3].startswith("claude"):
                continue
            pid, tty, etime = parts[0], parts[1], parts[2]
            name, mission = names.get(tty, ("?", "unknown — see FLEET.md"))
            rows.append({"tty": tty, "pid": pid, "up": etime, "name": name, "mission": mission})
        rows.sort(key=lambda r: r["tty"])
        return rows

    def events(self, n=20):
        return butler.read_jsonl(ROOT / "events.jsonl")[-n:][::-1]


# ---------------------------------------------------------------- views

def v_overview(st: State):
    name, acct = st.acct_cfg()
    weekly = acct.get("weekly_weighted_budget", 0)
    mu = st.machine_usage
    lines = [f"[bold]Active account:[/] [cyan]{st.account()}[/]"]
    if mu:
        pct = 100 * mu["weighted"] / weekly if weekly else 0
        lines.append(f"[bold]Machine, this week:[/] {fmt_tokens(mu['weighted'])} weighted "
                     f"/ {fmt_tokens(weekly)}  {bar(pct)}")
        lines.append(f"  sessions: {mu['sessions']}   raw in/out: "
                     f"{fmt_tokens(mu['input'])}/{fmt_tokens(mu['output'])}   "
                     f"cache r/w: {fmt_tokens(mu['cache_read'])}/{fmt_tokens(mu['cache_creation'])}")
    else:
        lines.append("[dim]usage not computed — press r[/]")
    head = Panel(Text.from_markup("\n".join(lines)), title="cellar", box=box.ROUNDED)

    t = Table(box=box.SIMPLE_HEAD, expand=True)
    for c in ("project", "alloc", "spent", "budget", ""):
        t.add_column(c)
    projs = st.projects()
    if not projs:
        t.add_row("[dim]no projects registered — butler register --project …[/]", "", "", "", "")
    for slug, p in projs.items():
        u = st.usage.get(slug)
        if u:
            t.add_row(slug, f"{p.get('budget_pct_weekly')}%", fmt_tokens(u["u"]["weighted"]),
                      fmt_tokens(u["budget"]), bar(u["pct"] or 0))
        else:
            t.add_row(slug, f"{p.get('budget_pct_weekly')}%", "[dim]r to compute[/]", "", "")
    mid = Panel(t, title="projects", box=box.ROUNDED)

    ev = Table(box=box.SIMPLE, expand=True, show_header=False)
    ev.add_column("ts", style="dim", width=17)
    ev.add_column("what")
    for e in st.events(6):
        color = {"rate_limit": "red", "switch": "cyan", "pause": "yellow",
                 "resume": "green"}.get(e.get("type"), "white")
        ev.add_row(e.get("ts", "")[:16],
                   f"[{color}]{e.get('type')}[/] {e.get('project') or ''} {e.get('note') or ''}")
    if not st.events(1):
        ev.add_row("", "[dim]no events yet[/]")
    tail = Panel(ev, title="recent events", box=box.ROUNDED)
    return Group(head, mid, tail)


def v_projects(st: State):
    projs = list(st.projects().items())
    if st.detail:
        return v_project_detail(st)
    t = Table(box=box.SIMPLE_HEAD, expand=True, title="projects — enter to open")
    for c in ("", "project", "alloc %", "accounts", "gpu d/w/m", "status"):
        t.add_column(c)
    if not projs:
        t.add_row("", "[dim]none registered[/]", "", "", "", "")
    for i, (slug, p) in enumerate(projs):
        g = p.get("gpu_hours", {})
        cur = "[bold cyan]▶[/]" if i == st.sel else " "
        style = "bold" if i == st.sel else ""
        t.add_row(cur, Text(slug, style=style), str(p.get("budget_pct_weekly")),
                  ",".join(p.get("accounts", [])),
                  f"{g.get('day')}/{g.get('week')}/{g.get('month')}", p.get("status", "?"))
    return Panel(t, box=box.ROUNDED)


def v_project_detail(st: State):
    slug = st.detail
    p = st.projects().get(slug)
    if not p:
        st.detail = None
        return v_projects(st)
    u = st.usage.get(slug)
    lines = [f"[bold]{slug}[/]   status: {p.get('status')}   accounts: {','.join(p.get('accounts', []))}"]
    lines.append(f"roots: {'; '.join(p.get('roots', []))}")
    if u:
        lines.append(f"week: {fmt_tokens(u['u']['weighted'])} / {fmt_tokens(u['budget'])}  {bar(u['pct'] or 0)}")
    now = time.time()
    import datetime as dt
    for wname, days in (("day", 1), ("week", 7), ("month", 30)):
        lim = p.get("gpu_hours", {}).get(wname)
        snap = butler._gpu_snapshot(
            slug, dt.datetime.fromtimestamp(now - days * 86400, dt.timezone.utc))
        committed = snap["committed_gpu_hours"]
        reserved = snap["reserved_gpu_hours"]
        pct = (100 * committed / lim) if lim else 0
        lines.append(f"gpu {wname:5}: {committed:6.1f}h ({reserved:.1f} reserved) / "
                     f"{lim or '∞'}  {bar(pct) if lim else ''}")
    info = Panel(Text.from_markup("\n".join(lines)), title=f"project: {slug}", box=box.ROUNDED)

    sess = butler.read_jsonl(butler.project_path(slug) / "sessions.jsonl")[-8:][::-1]
    t = Table(box=box.SIMPLE, expand=True, show_header=False)
    t.add_column("ts", style="dim", width=17)
    t.add_column("summary")
    for s in sess:
        t.add_row(s.get("ts", "")[:16], s.get("summary", ""))
    if not sess:
        t.add_row("", "[dim]no sessions logged[/]")
    hist = Panel(t, title="session history", box=box.ROUNDED)

    art = butler.project_path(slug) / "artifacts.md"
    atext = art.read_text().strip()[-800:] if art.exists() else "[dim]no artifacts[/]"
    mission = butler.project_path(slug) / "MISSION.md"
    mnote = "MISSION.md ✓" if mission.exists() else "[yellow]MISSION.md missing[/]"
    arts = Panel(Text.from_markup(atext + f"\n\n{mnote}"), title="artifacts", box=box.ROUNDED)
    return Group(info, hist, arts)


def v_fleet(st: State):
    rows = st.fleet()
    t = Table(box=box.SIMPLE_HEAD, expand=True,
              title=f"claude fleet — {len(rows)} live sessions (roster: ~/.butler/FLEET.md)")
    for c in ("", "tty", "pid", "up", "agent", "mission"):
        t.add_column(c)
    for i, r in enumerate(rows):
        cur = "[bold cyan]▶[/]" if i == st.sel else " "
        style = "bold" if i == st.sel else ""
        name_style = "green" if r["name"] not in ("?",) and "MYSTERY" not in r["name"] else "yellow"
        t.add_row(cur, Text(r["tty"], style=style), r["pid"], r["up"],
                  f"[{name_style}]{r['name']}[/]", r["mission"][:70])
    return Panel(t, box=box.ROUNDED)


def v_events(st: State):
    t = Table(box=box.SIMPLE_HEAD, expand=True, title="events (newest first)")
    for c in ("ts", "type", "account", "project", "note / resume_at"):
        t.add_column(c)
    evs = st.events(25)
    if not evs:
        t.add_row("[dim]none yet[/]", "", "", "", "")
    for e in evs:
        color = {"rate_limit": "red", "switch": "cyan", "pause": "yellow",
                 "resume": "green"}.get(e.get("type"), "white")
        t.add_row(e.get("ts", "")[:19], f"[{color}]{e.get('type')}[/]",
                  e.get("account") or "", e.get("project") or "",
                  (e.get("note") or "") + (" → " + e["resume_at"][:16] if e.get("resume_at") else ""))
    return Panel(t, box=box.ROUNDED)


def render(st: State, console: Console):
    layout = Layout()
    tabs = "  ".join(
        f"[reverse bold] {i + 1}:{v} [/]" if v == st.view else f" {i + 1}:{v} "
        for i, v in enumerate(VIEWS))
    header = Panel(Text.from_markup(
        f"[bold]🍷 BUTLER[/] — keeper of the cellar    {tabs}    "
        f"[dim]{time.strftime('%a %H:%M:%S')}[/]"), box=box.HEAVY, style="on grey11")
    body = {"overview": v_overview, "projects": v_projects,
            "fleet": v_fleet, "events": v_events}[st.view](st)
    foot = Text.from_markup(
        f"[dim]1-4 views · j/k move · enter open · b back · r recompute usage · q quit"
        f"{('   [yellow]' + st.msg + '[/]') if st.msg else ''}[/]")
    layout.split_column(Layout(header, size=3), Layout(body), Layout(foot, size=1))
    return layout


# ---------------------------------------------------------------- main

def main():
    st = State()
    console = Console()
    if "--once" in sys.argv:
        idx = sys.argv.index("--once")
        if len(sys.argv) > idx + 1 and sys.argv[idx + 1] in VIEWS:
            st.view = sys.argv[idx + 1]
        st.compute_all()
        console.print(render(st, console))
        return

    st.compute_all()
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    tty_mod.setcbreak(fd)
    try:
        with Live(render(st, console), console=console, screen=True, auto_refresh=False) as live:
            while True:
                r, _, _ = select.select([sys.stdin], [], [], 2.0)
                if r:
                    ch = os.read(fd, 1).decode(errors="ignore")
                    if ch == "\x1b":                      # escape / arrow
                        seq = os.read(fd, 2).decode(errors="ignore") if select.select([sys.stdin], [], [], 0.05)[0] else ""
                        if seq == "[A":
                            ch = "k"
                        elif seq == "[B":
                            ch = "j"
                        else:
                            ch = "b"
                    if ch == "q":
                        break
                    elif ch in "1234":
                        st.view = VIEWS[int(ch) - 1]
                        st.sel, st.detail, st.msg = 0, None, ""
                    elif ch == "j":
                        st.sel += 1
                    elif ch == "k":
                        st.sel = max(0, st.sel - 1)
                    elif ch in ("\r", "\n") and st.view == "projects" and not st.detail:
                        projs = list(st.projects())
                        if projs:
                            st.sel = min(st.sel, len(projs) - 1)
                            st.detail = projs[st.sel]
                    elif ch == "b":
                        st.detail = None
                    elif ch == "r":
                        st.msg = "recomputing…"
                        live.update(render(st, console), refresh=True)
                        st.compute_all()
                        st.msg = f"usage recomputed {time.strftime('%H:%M:%S')}"
                # clamp selection
                n = len(st.fleet()) if st.view == "fleet" else len(st.projects())
                st.sel = max(0, min(st.sel, max(0, n - 1)))
                live.update(render(st, console), refresh=True)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


if __name__ == "__main__":
    main()
