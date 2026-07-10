---
title: "Connect Azure DevOps projects, work items, repos, and pipelines to MCP agents"
description: "Use Azure DevOps MCP when an agent needs governed access to ADO projects, work items, builds, repos, test plans, wikis, and pipelines."
verification: "security_reviewed"
source: "https://github.com/microsoft/azure-devops-mcp"
author: "Microsoft"
publisher_type: "organization"
category:
  - "Integrations & Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "microsoft/azure-devops-mcp"
  github_stars: 1725
  npm_package: "@azure-devops/mcp"
  npm_weekly_downloads: 334283
---

# Connect Azure DevOps projects, work items, repos, and pipelines to MCP agents

Use Azure DevOps MCP when an agent needs governed access to ADO projects, work items, builds, repos, test plans, wikis, and pipelines.

## Prerequisites

Azure DevOps organization, MCP-capable client, Microsoft authentication, and Node.js 20+ for the optional local stdio server

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Start with the Azure DevOps Remote MCP Server using the upstream onboarding documentation. For local stdio use, install Node.js 20+ and configure the MCP client command as npx -y @azure-devops/mcp <organization>, optionally restricting domains such as core, work, work-items, search, repositories, wiki, test-plans, pipelines, or advanced-security.
```

## Documentation

- https://learn.microsoft.com/en-us/azure/devops/mcp-server/remote-mcp-server?view=azure-devops

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/connect-azure-devops-projects-work-items-repos-and-pipelines-to-mcp-agents/)
