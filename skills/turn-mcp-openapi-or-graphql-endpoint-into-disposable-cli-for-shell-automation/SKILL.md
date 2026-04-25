---
title: "Turn an MCP, OpenAPI, or GraphQL endpoint into a disposable CLI for shell automation"
description: "Generate a shell-ready CLI from an MCP server, OpenAPI spec, or GraphQL endpoint so an agent can discover commands and call tools immediately without hand-written wrappers."
verification: "security_reviewed"
source: "https://github.com/knowsuchagency/mcp2cli"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "knowsuchagency/mcp2cli"
  github_stars: 1940
---

# Turn an MCP, OpenAPI, or GraphQL endpoint into a disposable CLI for shell automation

Use mcp2cli when an agent needs to inspect or call an existing MCP server, OpenAPI spec, or GraphQL endpoint from the shell right away. It discovers commands at runtime, handles auth patterns including headers and OAuth, and gives the agent a small CLI surface it can script, retry, and pipe through other terminal tools. This is skill-shaped because the job is narrow and repeatable: adapt an already-existing endpoint into a temporary command-line interface for shell-first automation. It is not a generic API framework listing, SDK generator card, server-hosting product, or long-lived integration platform entry. Invoke it when the blocker is missing CLI ergonomics around an existing endpoint, not when you need to design the API, publish a server, or build a permanent client library.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/turn-mcp-openapi-or-graphql-endpoint-into-disposable-cli-for-shell-automation/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/turn-mcp-openapi-or-graphql-endpoint-into-disposable-cli-for-shell-automation
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/turn-mcp-openapi-or-graphql-endpoint-into-disposable-cli-for-shell-automation`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/turn-mcp-openapi-or-graphql-endpoint-into-disposable-cli-for-shell-automation/)
