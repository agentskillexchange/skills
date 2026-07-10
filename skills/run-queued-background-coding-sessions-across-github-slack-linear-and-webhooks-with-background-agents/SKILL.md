---
name: "Run queued background coding sessions across GitHub, Slack, Linear, and webhooks with background-agents"
slug: "run-queued-background-coding-sessions-across-github-slack-linear-and-webhooks-with-background-agents"
description: "Dispatch long-running coding work to background agents, check progress later, and pull reviewed outputs back into the main repo flow instead of babysitting one foreground session."
github_stars: 1591
verification: "security_reviewed"
source: "https://github.com/ColeMurray/background-agents"
author: "Cole Murray"
publisher_type: "individual"
category: "Developer Tools"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "ColeMurray/background-agents"
  github_stars: 1591
---

# Run queued background coding sessions across GitHub, Slack, Linear, and webhooks with background-agents

Dispatch long-running coding work to background agents, check progress later, and pull reviewed outputs back into the main repo flow instead of babysitting one foreground session.

## Prerequisites

GitHub App or repo access, deployed background-agents stack, sandbox infrastructure, supported model provider credentials, target repositories, and one or more trigger surfaces such as web UI, Slack, GitHub, Linear, or webhooks

## Installation

Use the upstream install or setup path that matches your environment:
- npm install
- pip install -r requirements.txt
- docker compose up -d postgres redis

Requirements and caveats from upstream:
- Access full development environments (Node.js, Python, git, browser automation, VS Code)
- │ │ (Node.js, Python, git, agent-browser) │ │
- **Pre-installed:** Node.js 22, Python 3.12, Bun, git, GitHub CLI, build-essential

Basic usage or getting-started notes:
- Run on a schedule — cron jobs, Sentry alerts, and webhook-triggered automations
- For a practical setup guide (local + contributor + deployment paths), start with
- **[docs/SETUP_GUIDE.md](docs/SETUP_GUIDE.md)**.

- Source: https://github.com/ColeMurray/background-agents
- Extracted from upstream docs: https://raw.githubusercontent.com/ColeMurray/background-agents/HEAD/README.md

## Documentation

- https://backgroundagents.dev

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-queued-background-coding-sessions-across-github-slack-linear-and-webhooks-with-background-agents/)
