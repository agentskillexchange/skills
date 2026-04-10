---
title: "Hookdeck CLI for Webhook Development and Event Debugging"
description: "Hookdeck CLI is Hookdeck’s official command-line tool for forwarding webhooks to localhost, managing event gateway resources, and running an MCP server for agent workflows. It is useful when you need repeatable webhook testing, local event inspection, and a bridge between webhook infrastructure and agent tooling."
slug: "hookdeck-cli-webhook-development-event-debugging"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/hookdeck/hookdeck-cli"
tool_ecosystem:
  github_repo: "hookdeck/hookdeck-cli"
  github_stars: 353
---

# Hookdeck CLI for Webhook Development and Event Debugging

Hookdeck CLI is Hookdeck’s official command-line tool for forwarding webhooks to localhost, managing event gateway resources, and running an MCP server for agent workflows. It is useful when you need repeatable webhook testing, local event inspection, and a bridge between webhook infrastructure and agent tooling.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install hookdeck-cli-webhook-development-event-debugging
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Hookdeck CLI is the official command-line interface for Hookdeck, a webhook infrastructure platform used to receive, route, replay, and inspect events. The upstream project lives at GitHub under hookdeck/hookdeck-cli, ships as an npm package named hookdeck-cli, and is documented on Hookdeck’s docs site. The repository is actively maintained and the CLI supports local webhook forwarding, event debugging, gateway resource management, and MCP server mode for AI-agent tooling.
As an ASE skill, this entry is for workflows where an agent needs to stand up a reliable webhook development loop without hand-rolling tunnels and ad hoc logging. A practical pattern is: run Hookdeck CLI locally, expose a temporary webhook endpoint, forward matching events to a local service, and use the event history to inspect failed deliveries or replay requests during debugging. Because Hookdeck CLI can manage sources, connections, destinations, and events, it also fits runbook-style automation for webhook setup and incident handling.
Integration points include local development environments, CI smoke tests, webhook-first SaaS integrations, and MCP-enabled agent stacks. In practice, teams pair it with Node.js services, localhost API servers, or event-driven backends. The primary install path in upstream docs is npm, though Homebrew packages are also available. For agent builders, Hookdeck CLI is especially relevant when a skill needs structured webhook forwarding, event replay, or MCP-based access to webhook resources from an assistant or coding agent.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hookdeck-cli-webhook-development-event-debugging/)
