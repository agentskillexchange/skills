---
name: "Diagnose OpenClaw node pairing and route failures"
slug: "diagnose-openclaw-node-pairing-and-route-failures"
description: "Guides an agent through the exact route, pairing, and auth checks needed when an OpenClaw companion node fails to connect over LAN, Tailscale, or a public URL. Use it when a node setup is broken and you need diagnosis, not when you simply want to list devices or advertise OpenClaw itself."
verification: "security_reviewed"
source: "https://github.com/openclaw/openclaw/tree/main/skills/node-connect"
author: "openclaw"
publisher_type: "open-source"
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
---

# Diagnose OpenClaw node pairing and route failures

Guides an agent through the exact route, pairing, and auth checks needed when an OpenClaw companion node fails to connect over LAN, Tailscale, or a public URL. Use it when a node setup is broken and you need diagnosis, not when you simply want to list devices or advertise OpenClaw itself.

## Prerequisites

openclaw CLI, optional Tailscale CLI

## Installation

Use the upstream install or setup path that matches your environment:
- npm install -g openclaw@latest
- Use pnpm for source checkouts. The repository is a pnpm workspace, and bundled
- git clone https://github.com/openclaw/openclaw.git
- pnpm install

Requirements and caveats from upstream:
- Runtime: **Node 24 (recommended) or Node 22.19+**.
- Public inbound DMs require an explicit opt-in: set dmPolicy="open" and include "*" in the channel allowlist (allowFrom / channels.discord.allowFrom / channels.slack.allowFrom; legacy: channels.discord.dm.allowFrom, ch...
- Group/channel safety: set agents.defaults.sandbox.mode: "non-main" to run non-main sessions inside sandboxes. Docker is the default sandbox backend; SSH and OpenShell backends are also available.

Basic usage or getting-started notes:
- **OpenClaw** is a _personal AI assistant_ you run on your own devices.
- [Website](https://openclaw.ai) · [Docs](https://docs.openclaw.ai) · [Vision](VISION.md) · [DeepWiki](https://deepwiki.com/openclaw/openclaw) · [Getting Started](https://docs.openclaw.ai/start/getting-started) · [Updat...
- New install? Start here: [Getting started](https://docs.openclaw.ai/start/getting-started)

- Source: https://github.com/openclaw/openclaw/tree/main/skills/node-connect
- Extracted from upstream docs: https://raw.githubusercontent.com/openclaw/openclaw/HEAD/README.md

## Documentation

- https://github.com/openclaw/openclaw/tree/main/skills/node-connect

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diagnose-openclaw-node-pairing-and-route-failures/)
