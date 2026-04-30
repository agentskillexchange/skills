---
title: "Diagnose OpenClaw node pairing and route failures"
description: "Guides an agent through the exact route, pairing, and auth checks needed when an OpenClaw companion node fails to connect over LAN, Tailscale, or a public URL. Use it when a node setup is broken and you need diagnosis, not when you simply want to list devices or advertise OpenClaw itself."
verification: "security_reviewed"
source: "https://github.com/openclaw/openclaw/tree/main/skills/node-connect"
author: "openclaw"
publisher_type: "open-source"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
---

# Diagnose OpenClaw node pairing and route failures

Guides an agent through the exact route, pairing, and auth checks needed when an OpenClaw companion node fails to connect over LAN, Tailscale, or a public URL. Use it when a node setup is broken and you need diagnosis, not when you simply want to list devices or advertise OpenClaw itself.

## Prerequisites

openclaw CLI, optional Tailscale CLI

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Included with OpenClaw skill distributions that ship node-connect.
```

## Documentation

- https://github.com/openclaw/openclaw/tree/main/skills/node-connect

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diagnose-openclaw-node-pairing-and-route-failures/)
