---
title: "Hookdeck CLI for Webhook Development and Event Debugging"
description: "Hookdeck CLI is the official command-line interface for Hookdeck , a webhook infrastructure platform used to receive, route, replay, and inspect events. The upstream project lives at GitHub under hookdeck/hookdeck-cli , ships as an npm package named hookdeck-cli , and is documented on Hookdeck&#8217;s docs site. The repository is actively maintained and the CLI supports local webhook forwarding, event debugging, gateway resource management, and MCP server mode for AI-agent tooling. As an ASE skill, this entry is for workflows where an agent needs to stand up a reliable webhook development loop without hand-rolling tunnels and ad hoc logging. A practical pattern is: run Hookdeck CLI locally, expose a temporary webhook endpoint, forward matching events to a local service, and use the event history to inspect failed deliveries or replay requests during debugging. Because Hookdeck CLI can manage sources, connections, destinations, and events, it also fits runbook-style automation for webhook setup and incident handling. Integration points include local development environments, CI smoke tests, webhook-first SaaS integrations, and MCP-enabled agent stacks. In practice, teams pair it with Node.js services, localhost API servers, or event-driven backends. The primary install path in upstream docs is npm, though Homebrew packages are also available. For agent builders, Hookdeck CLI is especially relevant when a skill needs structured webhook forwarding, event replay, or MCP-based access to webhook resources from an assistant or coding agent."
source: "https://github.com/hookdeck/hookdeck-cli"
verification: "security_reviewed"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "hookdeck/hookdeck-cli"
  github_stars: 353
---

# Hookdeck CLI for Webhook Development and Event Debugging

Hookdeck CLI is the official command-line interface for Hookdeck , a webhook infrastructure platform used to receive, route, replay, and inspect events. The upstream project lives at GitHub under hookdeck/hookdeck-cli , ships as an npm package named hookdeck-cli , and is documented on Hookdeck&#8217;s docs site. The repository is actively maintained and the CLI supports local webhook forwarding, event debugging, gateway resource management, and MCP server mode for AI-agent tooling. As an ASE skill, this entry is for workflows where an agent needs to stand up a reliable webhook development loop without hand-rolling tunnels and ad hoc logging. A practical pattern is: run Hookdeck CLI locally, expose a temporary webhook endpoint, forward matching events to a local service, and use the event history to inspect failed deliveries or replay requests during debugging. Because Hookdeck CLI can manage sources, connections, destinations, and events, it also fits runbook-style automation for webhook setup and incident handling. Integration points include local development environments, CI smoke tests, webhook-first SaaS integrations, and MCP-enabled agent stacks. In practice, teams pair it with Node.js services, localhost API servers, or event-driven backends. The primary install path in upstream docs is npm, though Homebrew packages are also available. For agent builders, Hookdeck CLI is especially relevant when a skill needs structured webhook forwarding, event replay, or MCP-based access to webhook resources from an assistant or coding agent.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hookdeck-cli-webhook-development-event-debugging/)
