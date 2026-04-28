---
title: Diagnose OpenClaw node pairing and route failures
description: Guides an agent through the exact route, pairing, and auth checks needed
  when an OpenClaw companion node fails to connect over LAN, Tailscale, or a public
  URL. Use it when a node setup is broken and you need diagnosis, not when you simply
  want to list devices or advertise OpenClaw itself.
verification: security_reviewed
source: https://github.com/openclaw/openclaw/tree/main/skills/node-connect
category:
- Runbooks & Diagnostics
framework:
- OpenClaw
tool_ecosystem:
  github_repo: openclaw/openclaw
  github_stars: 356821
---

# Diagnose OpenClaw node pairing and route failures

Guides an agent through the exact route, pairing, and auth checks needed when an OpenClaw companion node fails to connect over LAN, Tailscale, or a public URL. Use it when a node setup is broken and you need diagnosis, not when you simply want to list devices or advertise OpenClaw itself.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/diagnose-openclaw-node-pairing-and-route-failures/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/diagnose-openclaw-node-pairing-and-route-failures
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/diagnose-openclaw-node-pairing-and-route-failures`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diagnose-openclaw-node-pairing-and-route-failures/)
