---
name: "Triage Lunora deployment errors and migration status through MCP"
slug: "triage-lunora-deployment-errors-and-migration-status-through-mcp"
description: "Inspect Lunora logs, grouped errors, query performance and pending migrations through MCP, then return a scoped incident handoff without changing the deployment."
verification: "security_reviewed"
source: "https://github.com/anolilab/lunora/blob/6a5ea6cb971236545c5281bc00b910ef9f700f29/packages/mcp/README.md"
author: "Daniel Bannert / anolilab"
publisher_type: "organization"
category: "Runbooks & Diagnostics"
framework: "MCP"
---

# Triage Lunora deployment errors and migration status through MCP

Inspect Lunora logs, grouped errors, query performance and pending migrations through MCP, then return a scoped incident handoff without changing the deployment.

## Prerequisites

Node.js ^22.15.0 or >=24.11.0; npm/npx; stdio MCP client; @lunora/mcp@1.0.0-alpha.291; existing Lunora deployment and admin token

## Installation

Install or set up from the source-backed instructions:

Use Node.js ^22.15.0 or >=24.11.0 and an MCP client with stdio support. Configure command npx with args ["-y", "--package=@lunora/mcp@1.0.0-alpha.291", "lunora-mcp"]. Supply LUNORA_URL and LUNORA_ADMIN_TOKEN through the client secret configuration. Set LUNORA_MCP_ALLOW_OBSERVABILITY=1 for the approved diagnostic scope; explicitly set LUNORA_MCP_ALLOW_WRITES=0, LUNORA_MCP_ALLOW_AGENTS=0 and LUNORA_MCP_ALLOW_DATA_READS=0. The deployment admin token is privileged; read-only behavior comes from the MCP server configuration, not token scope. No new deployment or Cloudflare login is part of this workflow.

- Source: https://github.com/anolilab/lunora/blob/6a5ea6cb971236545c5281bc00b910ef9f700f29/packages/mcp/README.md

## Documentation

- https://github.com/anolilab/lunora/blob/6a5ea6cb971236545c5281bc00b910ef9f700f29/packages/mcp/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/triage-lunora-deployment-errors-and-migration-status-through-mcp/)
