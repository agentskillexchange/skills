---
name: "Docker MCP Server"
description: "Use this skill when you need to list running containers, inspect images, view container logs, or manage Docker volumes and networks from your AI agent. It enables agents to perform container management tasks and debug Docker-based applications without direct terminal access."
category: "Developer Tools"
framework: "MCP-compatible"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/docker-mcp-server/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "docker"  # from ase_tool_match
  github_stars: 71560  # from ase_github_stars (integer, not string)
  github_repo: "moby/moby"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Docker MCP Server

Use this skill when you need to list running containers, inspect images, view container logs, or manage Docker volumes and networks from your AI agent. It enables agents to perform container management tasks and debug Docker-based applications without direct terminal access.

## Overview

Use this skill when you need to list running containers, inspect images, view container logs, or manage Docker volumes and networks from your AI agent. It enables agents to perform container management tasks and debug Docker-based applications without direct terminal access.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill docker-mcp-server
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill docker-mcp-server -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill docker-mcp-server -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill docker-mcp-server -a codex
```

### OpenClaw

```bash
clawhub install docker-mcp-server
```

## Source

- Marketplace: https://agentskillexchange.com/skills/docker-mcp-server/
