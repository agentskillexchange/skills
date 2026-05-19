---
name: "Turn GitHub Issues into Fix PRs"
slug: "turn-github-issues-into-fix-prs"
description: "Use the gh-issues workflow to fetch filtered GitHub issues, spawn sub-agents for fixes, open PRs, and follow review comments. This is a bounded backlog-to-PR operator loop, not a general GitHub product listing."
verification: "security_reviewed"
source: "https://github.com/openclaw/openclaw/tree/main/skills/gh-issues"
category: "Developer Tools"
framework: "OpenClaw"
---

# Turn GitHub Issues into Fix PRs

Use the gh-issues workflow to fetch filtered GitHub issues, spawn sub-agents for fixes, open PRs, and follow review comments. This is a bounded backlog-to-PR operator loop, not a general GitHub product listing.

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

- Source: https://github.com/openclaw/openclaw/tree/main/skills/gh-issues
- Extracted from upstream docs: https://raw.githubusercontent.com/openclaw/openclaw/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/turn-github-issues-into-fix-prs/)
