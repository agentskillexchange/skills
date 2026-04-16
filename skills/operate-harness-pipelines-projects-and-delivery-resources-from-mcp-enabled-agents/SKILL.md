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
  ase_npm_package: "harness-mcp-v2"
  npm_weekly_downloads: 1019
  license: "Apache-2.0"
---

# Operate Harness pipelines, projects, and delivery resources from MCP-enabled agents

Use the Harness MCP Server when an agent needs to inspect, create, update, or troubleshoot Harness resources as part of a larger delivery workflow. The agent can work across organizations and projects, list and fetch platform objects, handle common CI/CD and delivery tasks through a small MCP tool surface, and apply prebuilt prompt templates for debugging failed runs, rollout planning, approvals, and cost or security review. The boundary is specific enough to be skill-shaped: this is for agent-side operation of Harness platform resources through MCP, not a generic CI/CD platform card and not a broad product listing for Harness itself.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/operate-harness-pipelines-projects-and-delivery-resources-from-mcp-enabled-agents/)
