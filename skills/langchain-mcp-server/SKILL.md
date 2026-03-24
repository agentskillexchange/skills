---
name: "LangChain MCP Server"
description: "Use this skill to build and execute LangChain chains, access LangChain’s agent tools ecosystem, and manage memory and conversation history through MCP. It enables agents to leverage LangChain’s extensive tool library and chain-building capabilities. Trigger when you need to compose multi-step AI workflows, use LangChain-specific tools, or manage conversation memory across sessions."
category: "Developer Tools"
framework: "MCP-compatible"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/langchain-mcp-server/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "langchain"  # from ase_tool_match
  github_stars: 17321  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 2137497  # from ase_npm_downloads
  github_repo: "langchain-ai/langchainjs"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# LangChain MCP Server

Use this skill to build and execute LangChain chains, access LangChain’s agent tools ecosystem, and manage memory and conversation history through MCP. It enables agents to leverage LangChain’s extensive tool library and chain-building capabilities. Trigger when you need to compose multi-step AI workflows, use LangChain-specific tools, or manage conversation memory across sessions.

## Overview

Use this skill to build and execute LangChain chains, access LangChain’s agent tools ecosystem, and manage memory and conversation history through MCP. It enables agents to leverage LangChain’s extensive tool library and chain-building capabilities. Trigger when you need to compose multi-step AI workflows, use LangChain-specific tools, or manage conversation memory across sessions.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill langchain-mcp-server
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill langchain-mcp-server -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill langchain-mcp-server -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill langchain-mcp-server -a codex
```

### OpenClaw

```bash
clawhub install langchain-mcp-server
```

## Source

- Marketplace: https://agentskillexchange.com/skills/langchain-mcp-server/
