---
name: "MongoDB MCP Server"
description: "MCP server for MongoDB that enables AI agents to query collections, manage documents, create indexes, run aggregation pipelines, and inspect schema metadata without writing MongoDB driver code."
category: "Developer Tools"
framework: "MCP-compatible"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/mongodb-mcp-server/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "mongodb"  # from ase_tool_match
  github_stars: 10180  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 10909882  # from ase_npm_downloads
  github_repo: "mongodb/node-mongodb-native"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# MongoDB MCP Server

MCP server for MongoDB that enables AI agents to query collections, manage documents, create indexes, run aggregation pipelines, and inspect schema metadata without writing MongoDB driver code.

## Overview

MCP server for MongoDB that enables AI agents to query collections, manage documents, create indexes, run aggregation pipelines, and inspect schema metadata without writing MongoDB driver code.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill mongodb-mcp-server
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill mongodb-mcp-server -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill mongodb-mcp-server -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill mongodb-mcp-server -a codex
```

### OpenClaw

```bash
clawhub install mongodb-mcp-server
```

## Source

- Marketplace: https://agentskillexchange.com/skills/mongodb-mcp-server/
