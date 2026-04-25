---
title: "Operate Harness pipelines, projects, and delivery resources from MCP-enabled agents"
description: "Use the Harness MCP Server when an agent needs governed access to Harness pipelines, services, environments, feature flags, cost data, and related platform resources from an MCP workflow instead of sending a human through the Harness UI."
verification: "security_reviewed"
source: "https://github.com/harness/mcp-server"
category:
  - "CI/CD Integrations"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "harness/mcp-server"
  github_stars: 43
  npm_package: "harness-mcp-v2"
  npm_weekly_downloads: 1019
---

# Operate Harness pipelines, projects, and delivery resources from MCP-enabled agents

Use the Harness MCP Server when an agent needs to inspect, create, update, or troubleshoot Harness resources as part of a larger delivery workflow. The agent can work across organizations and projects, list and fetch platform objects, handle common CI/CD and delivery tasks through a small MCP tool surface, and apply prebuilt prompt templates for debugging failed runs, rollout planning, approvals, and cost or security review. The boundary is specific enough to be skill-shaped: this is for agent-side operation of Harness platform resources through MCP, not a generic CI/CD platform card and not a broad product listing for Harness itself.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/operate-harness-pipelines-projects-and-delivery-resources-from-mcp-enabled-agents/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/operate-harness-pipelines-projects-and-delivery-resources-from-mcp-enabled-agents
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/operate-harness-pipelines-projects-and-delivery-resources-from-mcp-enabled-agents`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/operate-harness-pipelines-projects-and-delivery-resources-from-mcp-enabled-agents/)
