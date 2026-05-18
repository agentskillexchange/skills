---
name: "Audit OpenClaw host security posture and hardening gaps"
slug: "audit-openclaw-host-security-posture-and-hardening-gaps"
description: "This skill uses OpenClaw's healthcheck workflow to inspect the host running the assistant, surface risky exposure, and turn the findings into a staged hardening plan. It is for operator-style audits with explicit approval gates, not a generic software listing or a replacement for OS administration."
verification: "listed"
source: "https://github.com/openclaw/openclaw/tree/main/skills/healthcheck"
author: "OpenClaw"
publisher_type: "open_source_project"
category: "Security & Verification"
framework: "OpenClaw"
---

# Audit OpenClaw host security posture and hardening gaps

This skill uses OpenClaw's healthcheck workflow to inspect the host running the assistant, surface risky exposure, and turn the findings into a staged hardening plan. It is for operator-style audits with explicit approval gates, not a generic software listing or a replacement for OS administration.

## Prerequisites

OpenClaw CLI

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

- Source: https://github.com/openclaw/openclaw/tree/main/skills/healthcheck
- Extracted from upstream docs: https://raw.githubusercontent.com/openclaw/openclaw/HEAD/README.md

## Documentation

- https://github.com/openclaw/openclaw/tree/main/skills/healthcheck

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-openclaw-host-security-posture-and-hardening-gaps/)
