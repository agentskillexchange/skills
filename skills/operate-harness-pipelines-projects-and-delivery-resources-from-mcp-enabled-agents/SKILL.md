---
title: "Operate Harness pipelines, projects, and delivery resources from MCP-enabled agents"
description: "Use the Harness MCP Server when an agent needs governed access to Harness pipelines, services, environments, feature flags, cost data, and related platform resources from an MCP workflow instead of sending a human through the Harness UI."
verification: security_reviewed
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/operate-harness-pipelines-projects-and-delivery-resources-from-mcp-enabled-agents/)
