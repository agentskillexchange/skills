---
name: "Inspect Claude Code multi-agent runs with Agents Observe"
slug: "agents-observe-claude-code-observability"
description: "Gives Claude Code operators a live dashboard for multi-agent sessions, tool calls, file activity, and nested task progress so debugging starts from what the agents are actually doing."
github_stars: 421
verification: "listed"
source: "https://github.com/simple10/agents-observe"
author: "Joe Johnston"
publisher_type: "individual"
category: "Monitoring & Alerts"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "simple10/agents-observe"
  github_stars: 421
---

# Inspect Claude Code multi-agent runs with Agents Observe

Gives Claude Code operators a live dashboard for multi-agent sessions, tool calls, file activity, and nested task progress so debugging starts from what the agents are actually doing.

## Prerequisites

Claude Code, Docker, Node.js, and a local browser. The plugin runs a local server/container and captures Claude Code hook events for dashboard inspection.

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/simple10/agents-observe.git agents-observe
- brew install just
- docker-compose.yml # Container orchestration - not used by the plugin

Requirements and caveats from upstream:
- [Docker](https://www.docker.com/) (required — the server runs as a container)
- [Node.js](https://nodejs.org/) (required — hook scripts run via node)
- If docker or node are not installed on your host, the plugin will fail to properly load.

Basic usage or getting-started notes:
- bash
- # Add this repo as a marketplace
- claude plugin marketplace add simple10/agents-observe

- Source: https://github.com/simple10/agents-observe
- Extracted from upstream docs: https://raw.githubusercontent.com/simple10/agents-observe/HEAD/README.md

## Documentation

- https://github.com/simple10/agents-observe#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/agents-observe-claude-code-observability/)
