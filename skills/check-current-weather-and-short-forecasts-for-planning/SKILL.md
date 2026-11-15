---
name: "Check current weather and short forecasts for planning"
slug: "check-current-weather-and-short-forecasts-for-planning"
description: "This skill lets an agent fetch current conditions and short forecasts with a lightweight weather workflow instead of sending a user to a weather site. It is narrowly scoped to quick planning questions, not historical analysis, severe-alert monitoring, or a generic weather product listing."
verification: "security_reviewed"
source: "https://github.com/openclaw/openclaw/tree/main/skills/weather"
author: "OpenClaw"
publisher_type: "open_source_project"
category: "Calendar, Email & Productivity"
framework: "OpenClaw"
---

# Check current weather and short forecasts for planning

This skill lets an agent fetch current conditions and short forecasts with a lightweight weather workflow instead of sending a user to a weather site. It is narrowly scoped to quick planning questions, not historical analysis, severe-alert monitoring, or a generic weather product listing.

## Prerequisites

curl

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

- Source: https://github.com/openclaw/openclaw/tree/main/skills/weather
- Extracted from upstream docs: https://raw.githubusercontent.com/openclaw/openclaw/HEAD/README.md

## Documentation

- https://wttr.in/:help

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/check-current-weather-and-short-forecasts-for-planning/)
