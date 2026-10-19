#!/usr/bin/env python3
"""Discover every locally-listening HTTP UI, then build + open a navigable launcher dashboard.

Scans listening TCP ports (via lsof), probes each over HTTP on 127.0.0.1, captures the page
<title> and the owning process, and renders a dark launcher page you can click through. Also
prints a concise table to the terminal.

Usage:
  python3 scan_uis.py            # scan, build dashboard, open it, print table
  python3 scan_uis.py --no-open  # don't launch the browser
  python3 scan_uis.py --json     # emit raw JSON of discovered UIs and exit
"""
import concurrent.futures as cf
import html
import json
import re
import subprocess
import sys
import shutil
import urllib.request
from pathlib import Path

OUT = Path.home() / ".local/state/local-uis"
OUT.mkdir(parents=True, exist_ok=True)
DASH = OUT / "dashboard.html"

# ports we never want to treat as a browsable UI (infra/noise)
SKIP_PORTS = {22, 53, 5353, 137, 138, 139, 445, 631, 137}
# process names that are servers but not user UIs (tune as needed)
NOISY_CMDS = {"rapportd", "ControlCe", "sharingd", "identitys"}


def listening_ports():
    """Return {port: {'pid','cmd'}} for TCP listeners on loopback/all-interfaces."""
    try:
        raw = subprocess.run(
            ["lsof", "-nP", "-iTCP", "-sTCP:LISTEN"],
            capture_output=True, text=True, timeout=15,
        ).stdout
    except Exception as e:
        print(f"lsof failed: {e}", file=sys.stderr)
        return {}
    found = {}
    for line in raw.splitlines()[1:]:
        parts = line.split()
        if len(parts) < 9:
            continue
        cmd, pid, name = parts[0], parts[1], parts[8]
        m = re.search(r":(\d+)$", name)
        if not m:
            continue
        # only loopback or wildcard binds are reachable at 127.0.0.1
        host = name.rsplit(":", 1)[0]
        if host not in ("127.0.0.1", "*", "[::1]", "localhost", "[::]"):
            continue
        port = int(m.group(1))
        if port in SKIP_PORTS or cmd in NOISY_CMDS:
            continue
        found.setdefault(port, {"pid": pid, "cmd": cmd})
    return found


def probe(port):
    """Return dict if the port speaks HTTP, else None."""
    url = f"http://127.0.0.1:{port}/"
    req = urllib.request.Request(url, headers={"User-Agent": "local-uis-scan"})
    try:
        with urllib.request.urlopen(req, timeout=1.4) as r:
            status = r.status
            ctype = r.headers.get("Content-Type", "")
            body = b""
            if "html" in ctype.lower() or ctype == "":
                body = r.read(8192)
        title = ""
        mt = re.search(rb"<title[^>]*>(.*?)</title>", body, re.I | re.S)
        if mt:
            title = html.unescape(mt.group(1).decode("utf-8", "ignore")).strip()[:90]
        return {"port": port, "status": status, "ctype": ctype.split(";")[0], "title": title}
    except urllib.error.HTTPError as e:
        # 401/403/404 etc still means something is serving here
        return {"port": port, "status": e.code, "ctype": "", "title": ""}
    except Exception:
        return None


def scan():
    ports = listening_ports()
    uis = []
    with cf.ThreadPoolExecutor(max_workers=24) as ex:
        for port, res in zip(ports, ex.map(probe, ports)):
            if res:
                res.update(ports[port])
                uis.append(res)
    uis.sort(key=lambda d: d["port"])
    return uis


def build(uis):
    def card(u):
        port, title = u["port"], u["title"] or "(no title)"
        cmd, pid, status = u["cmd"], u["pid"], u["status"]
        url = f"http://127.0.0.1:{port}/"
        gated = status in (401, 403)
        st = f'<span class="pill gate">auth {status}</span>' if gated else \
             (f'<span class="pill ok">{status}</span>' if status < 400 else f'<span class="pill warn">{status}</span>')
        return (f'<a class="card" href="{url}" target="_blank" rel="noopener">'
                f'<div class="top"><span class="port">:{port}</span>{st}</div>'
                f'<div class="title">{html.escape(title)}</div>'
                f'<div class="meta"><span class="cmd">{html.escape(cmd)}</span>'
                f'<span class="pid">pid {pid}</span></div>'
                f'<div class="url">{url}</div></a>')

    cards = "".join(card(u) for u in uis) or '<p class="empty">No local HTTP UIs are listening right now.</p>'
    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Local UIs — {len(uis)} running</title><style>
:root{{--bg:#0b0d11;--panel:#14181f;--edge:#262c36;--edge2:#333b47;--ink:#eef2f7;--dim:#9aa5b4;--faint:#6b7480;--ember:#e8622c;--gold:#ffab5e;--ok:#3ecf8e;--warn:#e5b567;--gate:#5b8def}}
*{{box-sizing:border-box}}body{{margin:0;color:var(--ink);font:15px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
 background:radial-gradient(80% 40% at 50% -6%,color-mix(in srgb,var(--ember) 12%,var(--bg)),var(--bg) 60%),var(--bg)}}
.wrap{{max-width:1120px;margin:0 auto;padding:44px 22px 70px}}
.brand{{display:flex;align-items:center;gap:10px;margin-bottom:6px}}.brand .f{{font-size:24px;filter:drop-shadow(0 0 10px color-mix(in srgb,var(--ember) 70%,transparent))}}
.brand b{{font-size:18px;font-weight:800}}.brand span{{color:var(--dim);font-size:12px;letter-spacing:2px;text-transform:uppercase}}
h1{{font-size:clamp(24px,4vw,36px);margin:10px 0 6px;font-weight:840;letter-spacing:-.7px}}
.lead{{color:var(--dim);margin:0 0 8px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:14px;margin-top:26px}}
.card{{display:block;text-decoration:none;color:inherit;background:var(--panel);border:1px solid var(--edge);border-radius:14px;padding:16px 17px;transition:border-color .12s,transform .1s;box-shadow:0 8px 22px rgba(0,0,0,.34)}}
.card:hover{{border-color:var(--ember);transform:translateY(-2px)}}
.top{{display:flex;align-items:center;justify-content:space-between;margin-bottom:8px}}
.port{{font-size:19px;font-weight:900;color:var(--gold);font-variant-numeric:tabular-nums}}
.pill{{font-size:10.5px;font-weight:800;text-transform:uppercase;letter-spacing:.5px;padding:3px 8px;border-radius:999px}}
.pill.ok{{color:var(--ok);background:color-mix(in srgb,var(--ok) 15%,transparent)}}
.pill.warn{{color:var(--warn);background:color-mix(in srgb,var(--warn) 15%,transparent)}}
.pill.gate{{color:var(--gate);background:color-mix(in srgb,var(--gate) 15%,transparent)}}
.title{{font-size:15.5px;font-weight:700;margin-bottom:8px;line-height:1.35}}
.meta{{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:6px}}
.cmd{{font-size:12px;color:var(--ink);background:var(--bg);border:1px solid var(--edge);padding:2px 8px;border-radius:6px;font-family:ui-monospace,Menlo,monospace}}
.pid{{font-size:12px;color:var(--faint)}}
.url{{font-size:12px;color:var(--dim);font-family:ui-monospace,Menlo,monospace;word-break:break-all}}
.empty{{color:var(--dim);margin-top:30px}}
footer{{color:var(--faint);font-size:12px;margin-top:36px;border-top:1px solid var(--edge);padding-top:16px}}
</style></head><body><div class="wrap">
<div class="brand"><span class="f">&#129520;</span><b>Local UIs</b><span>launcher</span></div>
<h1>{len(uis)} UI{'s' if len(uis)!=1 else ''} running locally</h1>
<p class="lead">Everything currently listening on <code>127.0.0.1</code> that speaks HTTP. Click a card to open it in a new tab.</p>
<div class="grid">{cards}</div>
<footer>Rerun the <code>local-uis</code> skill to refresh · auth-gated services (401/403) are up but need a login/tunnel.</footer>
</div></body></html>"""
    DASH.write_text(doc)
    return DASH


def main():
    args = sys.argv[1:]
    uis = scan()
    if "--json" in args:
        print(json.dumps(uis, indent=2))
        return
    path = build(uis)
    # terminal table
    if uis:
        print(f"\n  {len(uis)} local UI(s):\n")
        print(f"  {'PORT':<7}{'STATUS':<8}{'PROCESS':<14}TITLE")
        print(f"  {'-'*4:<7}{'-'*6:<8}{'-'*7:<14}{'-'*5}")
        for u in uis:
            print(f"  :{u['port']:<6}{u['status']:<8}{u['cmd']:<14}{(u['title'] or '(no title)')[:52]}")
    else:
        print("  No local HTTP UIs listening right now.")
    print(f"\n  dashboard: {path}\n  open:      file://{path}\n")
    if "--no-open" not in args:
        opener = shutil.which("open") or shutil.which("xdg-open")
        if opener:
            subprocess.run([opener, str(path)], check=False)
        else:
            print("  no supported browser opener found; use the file URL above", file=sys.stderr)


if __name__ == "__main__":
    main()
