---
name: "Local UIs"
slug: "local-uis"
description: "Discover locally running HTTP interfaces, identify their listening ports and processes, and build a browsable launcher dashboard. Use when the user asks what web apps, dashboards, notebooks, or development servers are running locally or wants a single page from which to open them."
category: "Developer Tools"
framework: "Codex"
verification: "listed"
source: "https://github.com/AntreasAntoniou/local-uis"
---

# Local UIs

Discover what is serving now instead of relying on a hard-coded port list.

## Run

```bash
python3 scan_uis.py
```

Use `--no-open` to create the launcher without opening it, or `--json` for machine-readable results.

The scanner:

1. reads TCP listeners with `lsof`;
2. limits probes to services reachable through `127.0.0.1`;
3. performs short HTTP probes in parallel;
4. records response status, page title, process name, and PID;
5. writes `~/.local/state/local-uis/dashboard.html`.

## Interpret results

- 2xx and 3xx responses are available.
- 401 and 403 responses show a live service that requires authentication.
- Other 4xx and 5xx responses are reachable but unhealthy or not serving a root page.
- The dashboard is a snapshot. Re-run the scan before making a current-state claim.

## Safety

- The tool does not probe other hosts or non-loopback addresses.
- A service bound to all interfaces may still be externally reachable; this scanner does not establish network isolation.
- Page titles and process metadata can be sensitive. Do not publish the generated dashboard without review.
- Do not treat an HTTP response as proof that the application behind it is healthy.

On macOS the dashboard opens with `open`; on Linux it uses `xdg-open` when available.

## Installation and upstream provenance

The upstream skill identifier is `local-uis`. Install its instructions into a Codex project using the version-pinned, third-party Vercel Labs installer:

```bash
npx --yes skills@1.5.23 add AntreasAntoniou/local-uis --skill local-uis --agent codex --yes
```

Skill installation is separate from runtime setup. Read the [upstream README](https://github.com/AntreasAntoniou/local-uis#readme) for required tools, platform constraints, optional integrations, and execution instructions. A successful skill install does not establish that every runtime integration has been exercised or is available on the current host. Do not install credentials, private archives, mail, writing corpora, or session logs with this package.

This contribution preserves the upstream instructions and accompanying MIT [license](LICENSE), with ASE catalogue metadata and this installation section added. The source snapshot is [`0bf2fdec39cb`](https://github.com/AntreasAntoniou/local-uis/tree/0bf2fdec39cbfe5914c075dbf65e31ffd76a703a). The `listed` tier identifies a source-backed submission; it is not a security-review claim.
