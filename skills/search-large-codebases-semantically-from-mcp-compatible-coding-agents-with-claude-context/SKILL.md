---
title: "Search large codebases semantically from MCP-compatible coding agents with Claude Context"
slug: "search-large-codebases-semantically-from-mcp-compatible-coding-agents-with-claude-context"
description: "Use Claude Context when a coding agent needs targeted semantic retrieval from a very large repository instead of repeatedly loading folders or files into prompt context. It indexes code into a vector database and exposes code-search retrieval through MCP for Claude Code and other compatible agent clients."
github_stars: 9226
verification: "security_reviewed"
source: "https://github.com/zilliztech/claude-context"
author: "Zilliz"
publisher_type: "Organization"
category: "Developer Tools"
framework: "MCP"
tool_ecosystem:
  github_repo: "zilliztech/claude-context"
  github_stars: 9226
  npm_package: "@zilliz/claude-context-mcp"
  npm_weekly_downloads: 2386
---

# Search large codebases semantically from MCP-compatible coding agents with Claude Context

Use Claude Context when a coding agent needs targeted semantic retrieval from a very large repository instead of repeatedly loading folders or files into prompt context. It indexes code into a vector database and exposes code-search retrieval through MCP for Claude Code and other compatible agent clients.

## Prerequisites

MCP-compatible coding agent; Node.js 20-23; OpenAI API key; Milvus or Zilliz Cloud vector database

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Configure the MCP server in your client using the upstream package, for example `claude mcp add claude-context -- npx @zilliz/claude-context-mcp@latest`, then provide the required OpenAI and Milvus/Zilliz credentials.
```

## Documentation

- https://github.com/zilliztech/claude-context/tree/master/docs

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/search-large-codebases-semantically-from-mcp-compatible-coding-agents-with-claude-context/)
