---
title: "Hookdeck CLI for Webhook Development and Event Debugging"
description: "Hookdeck CLI is the official command-line interface for Hookdeck, a webhook infrastructure platform used to receive, route, replay, and inspect events. The upstream project lives at GitHub under hookdeck/hookdeck-cli, ships as an npm package named hookdeck-cli, and is documented on Hookdeck’s docs site. The repository is actively maintained and the CLI supports local webhook forwarding, event debugging, gateway resource management, and MCP server mode for AI-agent tooling.\nAs an ASE skill, this entry is for workflows where an agent needs to stand up a reliable webhook development loop without hand-rolling tunnels and ad hoc logging. A practical pattern is: run Hookdeck CLI locally, expose a temporary webhook endpoint, forward matching events to a local service, and use the event history to inspect failed deliveries or replay requests during debugging. Because Hookdeck CLI can manage sources, connections, destinations, and events, it also fits runbook-style automation for webhook setup and incident handling.\nIntegration points include local development environments, CI smoke tests, webhook-first SaaS integrations, and MCP-enabled agent stacks. In practice, teams pair it with Node.js services, localhost API servers, or event-driven backends. The primary install path in upstream docs is npm, though Homebrew packages are also available. For agent builders, Hookdeck CLI is especially relevant when a skill needs structured webhook forwarding, event replay, or MCP-based access to webhook resources from an assistant or coding agent."
verification: security_reviewed
source: "https://github.com/hookdeck/hookdeck-cli"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "hookdeck/hookdeck-cli"
  github_stars: 353
---

# Hookdeck CLI for Webhook Development and Event Debugging

Hookdeck CLI is the official command-line interface for Hookdeck, a webhook infrastructure platform used to receive, route, replay, and inspect events. The upstream project lives at GitHub under hookdeck/hookdeck-cli, ships as an npm package named hookdeck-cli, and is documented on Hookdeck’s docs site. The repository is actively maintained and the CLI supports local webhook forwarding, event debugging, gateway resource management, and MCP server mode for AI-agent tooling.
As an ASE skill, this entry is for workflows where an agent needs to stand up a reliable webhook development loop without hand-rolling tunnels and ad hoc logging. A practical pattern is: run Hookdeck CLI locally, expose a temporary webhook endpoint, forward matching events to a local service, and use the event history to inspect failed deliveries or replay requests during debugging. Because Hookdeck CLI can manage sources, connections, destinations, and events, it also fits runbook-style automation for webhook setup and incident handling.
Integration points include local development environments, CI smoke tests, webhook-first SaaS integrations, and MCP-enabled agent stacks. In practice, teams pair it with Node.js services, localhost API servers, or event-driven backends. The primary install path in upstream docs is npm, though Homebrew packages are also available. For agent builders, Hookdeck CLI is especially relevant when a skill needs structured webhook forwarding, event replay, or MCP-based access to webhook resources from an assistant or coding agent.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/hookdeck-cli-webhook-development-event-debugging
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/hookdeck-cli-webhook-development-event-debugging` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hookdeck-cli-webhook-development-event-debugging/)
