---
title: "Diagnose OpenClaw node pairing and route failures"
description: "Guides an agent through the exact route, pairing, and auth checks needed when an OpenClaw companion node fails to connect over LAN, Tailscale, or a public URL. Use it when a node setup is broken and you need diagnosis, not when you simply want to list devices or advertise OpenClaw itself."
verification: "security_reviewed"
source: "https://github.com/openclaw/openclaw/tree/main/skills/node-connect"
category:
  - "Runbooks & Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "openclaw/openclaw"
  github_stars: 356821
  license: "MIT"
---

# Diagnose OpenClaw node pairing and route failures

This entry uses the node-connect skill from the openclaw/openclaw repository. The agent behavior is diagnostic and narrow: determine the intended topology, inspect the gateway route OpenClaw is actually advertising, compare that route to the failure mode, and recommend one concrete fix path for pairing or authorization problems. It is a troubleshooting runbook, not a platform listing.


Invoke this instead of using the product normally when a user is blocked by setup failure. Typical triggers include QR setup codes that do not connect, manual host and port connections that work on local Wi-Fi but fail on a VPS or tailnet, stale bootstrap tokens, pairing requests that are pending but unapproved, or confusing errors around gateway.bind, gateway.remote.url, Tailscale, and public pairing URLs. In those moments the task is not “use OpenClaw,” it is “diagnose why node-to-gateway connectivity is broken.”


The scope boundary is what keeps this skill-shaped. It does not try to describe the whole OpenClaw project, companion apps, or node feature set. It focuses on a single operator job: find the real route from node to gateway and fix auth or pairing in that path. That boundary prevents it from being just another platform, SDK, or server entry.


Integration points are the OpenClaw CLI commands the runbook centers on, including openclaw qr --json, device approval checks, gateway config inspection, and optional Tailscale status verification. It belongs in diagnostics and connectivity support workflows.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diagnose-openclaw-node-pairing-and-route-failures/)
