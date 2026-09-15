# Local UIs

Local UIs finds running local web interfaces and puts them on one clickable
launcher page. It is useful after agents have built dashboards, notebooks,
previews, and development servers across several tasks: the tools may still be
running even when the terminal or conversation containing their URLs is gone.

Ask “What local UIs are running?” and get titles, ports, process names, PIDs, and
HTTP response status, with links to open each detected service. No maintained
port list or app registration is required.

## Skill and scanner

[SKILL.md](SKILL.md) tells an agent when to scan and how to interpret the results.
[scan_uis.py](scan_uis.py) does the work and can also run directly without an
agent. It uses Python's standard library and the system `lsof` command—no
third-party Python packages or hosted service.

The scanner reads TCP listeners, filters out known infrastructure noise, probes
candidate ports over HTTP at `127.0.0.1`, and extracts page titles where
available. It prints a terminal table and writes a static launcher to
`~/.local/state/local-uis/dashboard.html`.

It discovers services that already exist. It does not start apps, recover
stopped servers, manage their lifetimes, or inspect the agent conversation that
created them.

## Install and run

```bash
npx skills add AntreasAntoniou/local-uis
```

From the installed skill directory or repository checkout:

```bash
python3 scan_uis.py            # build the dashboard and open it
python3 scan_uis.py --no-open
python3 scan_uis.py --json     # print results without building a dashboard
```

Requirements: Python 3 and `lsof`. Browser opening uses `open` on macOS or
`xdg-open` on Linux when available; otherwise open the reported HTML file yourself.

## What the results do—and do not—prove

An HTTP response means something answered, not that the application works.
The dashboard distinguishes authentication gates (`401`/`403`) from other
responses, including error pages. It is a snapshot; rerun before making a
current-state claim.

Discovery is best-effort: HTTPS-only or IPv6-only services, invisible listeners,
slow responses, and apps needing a particular hostname or path may be missed or
poorly identified. A reachable API can appear even if it has no useful UI.

Probes begin at loopback addresses, but the current HTTP client follows redirects
and uses standard proxy handling; this is not a network-isolation guarantee.
Likewise, finding a service through loopback does not prove it is inaccessible
from other machines. Run it only where probing local services is authorized.

Page titles and process metadata can be sensitive. The dashboard stays on disk
and uses ordinary filesystem permissions, not an enforced owner-only storage
policy. Review it before sharing or publishing it.

## Test

```bash
python3 -m unittest discover -s tests
```

The dashboard-rendering test writes to the dashboard path above and can replace
an existing launcher. It uses synthetic service metadata and does not run a scan.

Released under the [MIT License](LICENSE).
