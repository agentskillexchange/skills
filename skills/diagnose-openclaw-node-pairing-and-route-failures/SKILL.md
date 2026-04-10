---
name: "Diagnose OpenClaw node pairing and route failures"
description: "Guides an agent through the exact route, pairing, and auth checks needed when an OpenClaw companion node fails to connect over LAN, Tailscale, or a public URL. Use it when a node setup is broken and you need diagnosis, not when you simply want to list devices or advertise OpenClaw itself."
verification: security_reviewed
source: "https://github.com/openclaw/openclaw/tree/main/skills/node-connect"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
---

# Diagnose OpenClaw node pairing and route failures

This entry uses the node-connect skill from the openclaw/openclaw repository. The agent behavior is diagnostic and narrow: determine the intended topology, inspect the gateway route OpenClaw is actually advertising, compare that route to the failure mode, and recommend one concrete fix path for pairing or authorization problems. It is a troubleshooting runbook, not a platform listing.
Invoke this instead of using the product normally when a user is blocked by setup failure. Typical triggers include QR setup codes that do not connect, manual host and port connections that work on local Wi-Fi but fail on a VPS or tailnet, stale bootstrap tokens, pairing requests that are pending but unapproved, or confusing errors around gateway.bind, gateway.remote.url, Tailscale, and public pairing URLs. In those moments the task is not “use OpenClaw,” it is “diagnose why node-to-gateway connectivity is broken.”
The scope boundary is what keeps this skill-shaped. It does not try to describe the whole OpenClaw project, companion apps, or node feature set. It focuses on a single operator job: find the real route from node to gateway and fix auth or pairing in that path. That boundary prevents it from being just another platform, SDK, or server entry.
Integration points are the OpenClaw CLI commands the runbook centers on, including openclaw qr --json, device approval checks, gateway config inspection, and optional Tailscale status verification. It belongs in diagnostics and connectivity support workflows.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diagnose-openclaw-node-pairing-and-route-failures/)
