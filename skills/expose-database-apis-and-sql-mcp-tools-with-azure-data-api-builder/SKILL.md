---
title: "Expose database APIs and SQL MCP tools with Azure Data API Builder"
description: "Use Azure Data API Builder to generate secure REST, GraphQL, and SQL MCP access for supported databases so agents can query and operate data through bounded tools."
verification: "security_reviewed"
source: "https://github.com/Azure/data-api-builder"
author: "Microsoft Azure"
publisher_type: "organization"
category:
  - "Integrations & Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "Azure/data-api-builder"
  github_stars: 1442
---

# Expose database APIs and SQL MCP tools with Azure Data API Builder

Use Azure Data API Builder to generate secure REST, GraphQL, and SQL MCP access for supported databases so agents can query and operate data through bounded tools.

## Prerequisites

.NET 8 or later, Data API Builder CLI, supported database, MCP-compatible agent client

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install .NET 8 or later, run `dotnet tool install microsoft.dataapibuilder -g`, initialize a `dab-config.json` with `dab init`, add database entities and permissions, then run Data API Builder and connect an agent client to the documented SQL MCP server when MCP access is required.
```

## Documentation

- https://learn.microsoft.com/en-us/azure/data-api-builder/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/expose-database-apis-and-sql-mcp-tools-with-azure-data-api-builder/)
