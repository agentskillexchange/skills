---
title: "Calculate routes, ETAs, and place lookups inside agent planning workflows with TomTom MCP"
description: "Gives an MCP-compatible agent structured place search, geocoding, routing, ETA, traffic, and map lookups so travel, field-service, and logistics tasks can stay inside an automated planning workflow."
verification: "security_reviewed"
source: "https://github.com/tomtom-international/tomtom-mcp"
author: "TomTom"
publisher_type: "company"
category:
  - "Integrations & Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "tomtom-international/tomtom-mcp"
  github_stars: 45
  npm_package: "@tomtom-org/tomtom-mcp"
  npm_weekly_downloads: 356
---

# Calculate routes, ETAs, and place lookups inside agent planning workflows with TomTom MCP

Gives an MCP-compatible agent structured place search, geocoding, routing, ETA, traffic, and map lookups so travel, field-service, and logistics tasks can stay inside an automated planning workflow.

## Prerequisites

MCP-compatible client, TomTom API key with MCP access, and either the hosted TomTom MCP endpoint or Node.js 22+ for local use.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Connect your MCP client to the hosted endpoint at https://mcp.tomtom.com/maps with a tomtom-api-key header, or run it locally with npm install @tomtom-org/tomtom-mcp@latest or npx @tomtom-org/tomtom-mcp@latest. Provide TOMTOM_API_KEY, then register the server in your MCP client configuration.
```

## Documentation

- https://developer.tomtom.com/tomtom-mcp/documentation/overview

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/calculate-routes-etas-and-place-lookups-inside-agent-planning-workflows-with-tomtom-mcp/)
