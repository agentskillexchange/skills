---
title: "Turn an MCP, OpenAPI, or GraphQL endpoint into a disposable CLI for shell automation"
slug: "turn-mcp-openapi-or-graphql-endpoint-into-disposable-cli-for-shell-automation"
description: "Generate a shell-ready CLI from an MCP server, OpenAPI spec, or GraphQL endpoint so an agent can discover commands and call tools immediately without hand-written wrappers."
verification: "security_reviewed"
source: "https://github.com/knowsuchagency/mcp2cli"
author: "Knowsuch Agency"
publisher_type: "company"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "knowsuchagency/mcp2cli"
  github_stars: 1940
---

# Turn an MCP, OpenAPI, or GraphQL endpoint into a disposable CLI for shell automation

Generate a shell-ready CLI from an MCP server, OpenAPI spec, or GraphQL endpoint so an agent can discover commands and call tools immediately without hand-written wrappers.

## Prerequisites

Python with uv or uvx, network access to the target MCP/OpenAPI/GraphQL endpoint, and any required auth headers or OAuth credentials for that endpoint.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
<p>Run <code>uvx mcp2cli --help</code> for an ephemeral install, or <code>uv tool install mcp2cli</code> for a persistent global install. Then point it at an MCP server with <code>--mcp</code>, an OpenAPI spec with <code>--spec</code>, or a GraphQL endpoint with <code>--graphql</code>, use <code>--list</code> to discover generated subcommands, and call the command you need with the same connection and auth flags.</p>
```

## Documentation

- https://github.com/knowsuchagency/mcp2cli

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/turn-mcp-openapi-or-graphql-endpoint-into-disposable-cli-for-shell-automation/)
