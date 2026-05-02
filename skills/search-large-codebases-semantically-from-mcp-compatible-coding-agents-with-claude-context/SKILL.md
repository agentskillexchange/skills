---
title: "Search large codebases semantically from MCP-compatible coding agents with Claude Context"
description: "Use Claude Context when a coding agent needs targeted semantic retrieval from a very large repository instead of repeatedly loading folders or files into prompt context. It indexes code into a vector database and exposes code-search retrieval through MCP for Claude Code and other compatible agent clients."
verification: "security_reviewed"
source: "https://github.com/zilliztech/claude-context"
category:
  - "Developer Tools"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "zilliztech/claude-context"
  github_stars: 9226
  npm_package: "@zilliz/claude-context-mcp"
  npm_weekly_downloads: 2386
---

# Search large codebases semantically from MCP-compatible coding agents with Claude Context

Claude Context is an MCP-delivered semantic code search workflow for coding agents. It indexes a repository into a vector store and returns the most relevant code for a task, so the agent can navigate large codebases without repeatedly dumping whole directories into context.

Invoke this instead of using the product normally when the agent needs code-aware retrieval as part of an interactive coding loop, especially on large repositories where naive file reads are expensive or incomplete. The scope boundary is that the publishable skill is the agent-facing retrieval workflow through MCP, not a generic vector database, not a general code search product listing, and not just a package card.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/search-large-codebases-semantically-from-mcp-compatible-coding-agents-with-claude-context/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/search-large-codebases-semantically-from-mcp-compatible-coding-agents-with-claude-context
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/search-large-codebases-semantically-from-mcp-compatible-coding-agents-with-claude-context`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/search-large-codebases-semantically-from-mcp-compatible-coding-agents-with-claude-context/)
