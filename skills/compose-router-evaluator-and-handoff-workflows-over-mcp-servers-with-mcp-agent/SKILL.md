---
title: "Compose router, evaluator, and handoff workflows over MCP servers with mcp-agent"
description: "Connect LLMs to MCP servers through composable patterns like router, evaluator-optimizer, and orchestrator flows without hand-managing server lifecycles."
verification: "security_reviewed"
source: "https://github.com/lastmile-ai/mcp-agent"
category:
  - "Templates & Workflows"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "lastmile-ai/mcp-agent"
  github_stars: 8276
  npm_package: "mcp-agent"
  npm_weekly_downloads: 29247
---

# Compose router, evaluator, and handoff workflows over MCP servers with mcp-agent

Use mcp-agent when the job is to wire an LLM to one or more MCP servers through explicit workflow patterns such as router, map-reduce, evaluator-optimizer, or orchestrator handoffs. The upstream project is centered on MCP-native composition and on managing MCP server connections so the operator can focus on the workflow itself.

Invoke this instead of using raw MCP clients or hand-rolled glue code when you need reusable MCP workflow patterns with clearer boundaries. The scope boundary is specific: this entry is about composing agent workflows over MCP servers. That keeps it skill-shaped and prevents it from collapsing into a generic framework listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/compose-router-evaluator-and-handoff-workflows-over-mcp-servers-with-mcp-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/compose-router-evaluator-and-handoff-workflows-over-mcp-servers-with-mcp-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/compose-router-evaluator-and-handoff-workflows-over-mcp-servers-with-mcp-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/compose-router-evaluator-and-handoff-workflows-over-mcp-servers-with-mcp-agent/)
