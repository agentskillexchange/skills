---
name: "Coordinate multi-agent Claude Code and Codex workflows with Ruflo"
slug: "coordinate-multi-agent-claude-code-and-codex-workflows-with-ruflo"
description: "Install Ruflo when an operator needs Claude Code or Codex agents to coordinate swarms, memory, hooks, and MCP tools across a bounded project workflow."
github_stars: 59039
verification: "security_reviewed"
source: "https://github.com/ruvnet/ruflo"
author: "ruvnet"
publisher_type: "organization"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "ruvnet/ruflo"
  github_stars: 59039
  npm_package: "ruflo"
  npm_weekly_downloads: 83473
---

# Coordinate multi-agent Claude Code and Codex workflows with Ruflo

Install Ruflo when an operator needs Claude Code or Codex agents to coordinate swarms, memory, hooks, and MCP tools across a bounded project workflow.

## Prerequisites

Claude Code or Codex, Node.js/npx, Ruflo CLI or Claude Code plugin, optional MCP client support

## Installation

Use the upstream install or setup path that matches your environment:
- npx claude-flow@latest federation init
- npx claude-flow@latest federation join wss://team-b.example.com:8443
- npx claude-flow@latest federation send --to team-b --type task-request \
- npx claude-flow@latest federation status

Requirements and caveats from upstream:
- | 🏠 | **Self-hostable** | Web UI is shipped as Docker (ruflo/src/ruvocal/Dockerfile) with embedded Mongo. Deploy to your own Cloud Run / Fly / Kubernetes / docker-compose. The hosted [flo.ruv.io](https://flo.ruv.io/)...
- | 🔗 | **Wired to MCP tools** | Every action node maps to a tool call (RuFlo's ~210 MCP tools, your custom servers, or shell). The planner schedules them in parallel where the dependency graph allows. |
- | 📊 | **Behavioral trust scoring** | Formula (0.4×success + 0.2×uptime + 0.2×threat + 0.2×integrity) continuously evaluates peers. Upgrades require history; downgrades are instant. |

Basic usage or getting-started notes:
- Orchestrate 100+ specialized AI agents across machines, teams, and trust boundaries. Ruflo adds coordinated swarms, self-learning memory, federated comms, and enterprise security to Claude Code — so agents don't just...
- | 🦾 | **ruvLLM self-learning AI** | Native support for [ruvLLM](https://github.com/ruvnet/RuVector/tree/main/examples/ruvLLM) (lives in ruvnet/RuVector/examples/ruvLLM) — RuFlo's self-improving local model layer. Rout...
- | 🔌 | **Bring your own MCP servers** | Click the **MCP (n)** pill in the chat input → *Add Server* and paste any MCP endpoint (HTTP, SSE, or stdio). Your tools join RuFlo's native ones in the same parallel-execution f...

- Source: https://github.com/ruvnet/ruflo
- Extracted from upstream docs: https://raw.githubusercontent.com/ruvnet/ruflo/HEAD/README.md

## Documentation

- https://github.com/ruvnet/ruflo

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/coordinate-multi-agent-claude-code-and-codex-workflows-with-ruflo/)
