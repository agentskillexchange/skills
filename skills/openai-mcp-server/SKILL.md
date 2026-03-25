---
name: "OpenAI MCP Server"
description: "Use this skill to make GPT-4/o1 API calls, generate embeddings, manage fine-tuning jobs, and access OpenAI’s full model suite through the Model Context Protocol. It enables agents to leverage OpenAI’s capabilities without direct API integration. Trigger when you need to generate text with GPT-4, create embeddings for semantic search, or manage model fine-tuning workflows."
category: "Developer Tools"
framework: "MCP-compatible"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/openai-mcp-server/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "openai"  # from ase_tool_match
  github_stars: 10761  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 16275389  # from ase_npm_downloads
  github_repo: "openai/openai-node"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# OpenAI MCP Server

Use this skill to make GPT-4/o1 API calls, generate embeddings, manage fine-tuning jobs, and access OpenAI’s full model suite through the Model Context Protocol. It enables agents to leverage OpenAI’s capabilities without direct API integration. Trigger when you need to generate text with GPT-4, create embeddings for semantic search, or manage model fine-tuning workflows.

## Overview

Use this skill to make GPT-4/o1 API calls, generate embeddings, manage fine-tuning jobs, and access OpenAI’s full model suite through the Model Context Protocol. It enables agents to leverage OpenAI’s capabilities without direct API integration. Trigger when you need to generate text with GPT-4, create embeddings for semantic search, or manage model fine-tuning workflows.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill openai-mcp-server
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill openai-mcp-server -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill openai-mcp-server -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill openai-mcp-server -a codex
```

### OpenClaw

```bash
clawhub install openai-mcp-server
```

## Source

- Marketplace: https://agentskillexchange.com/skills/openai-mcp-server/
