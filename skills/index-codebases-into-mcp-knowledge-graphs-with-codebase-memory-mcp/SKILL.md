---
name: "Index codebases into MCP knowledge graphs with codebase-memory-mcp"
slug: "index-codebases-into-mcp-knowledge-graphs-with-codebase-memory-mcp"
description: "Give coding agents a local MCP code intelligence graph for fast architecture, symbol, route, impact, and call-path queries across large repositories."
github_stars: 7266
verification: "security_reviewed"
source: "https://github.com/DeusData/codebase-memory-mcp"
author: "DeusData"
publisher_type: "organization"
category: "Integrations & Connectors"
framework: "MCP"
tool_ecosystem:
  github_repo: "DeusData/codebase-memory-mcp"
  github_stars: 7266
  npm_package: "codebase-memory-mcp"
  npm_weekly_downloads: 1956
---

# Index codebases into MCP knowledge graphs with codebase-memory-mcp

Give coding agents a local MCP code intelligence graph for fast architecture, symbol, route, impact, and call-path queries across large repositories.

## Prerequisites

MCP-compatible coding agent, codebase-memory-mcp binary or npm package, local repository access

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/DeusData/codebase-memory-mcp.git

Requirements and caveats from upstream:
- High-quality parsing through [tree-sitter](https://tree-sitter.github.io/tree-sitter/) AST analysis across all 158 languages, enhanced with [**Hybrid LSP** semantic type resolution](#hybrid-lsp) for Python, TypeScript...
- **Plug and play** — single static binary for macOS (arm64/amd64), Linux (arm64/amd64), and Windows (amd64). No Docker, no runtime dependencies, no API keys. Download → install → restart agent → done.
- **Semantic search** (semantic_query): vector search across the entire graph, powered by bundled Nomic nomic-embed-code embeddings (40K tokens, 768d int8) compiled into the binary — no API key, no Ollama, no Docker. 11...

Basic usage or getting-started notes:
- [![CI](https://img.shields.io/github/actions/workflow/status/DeusData/codebase-memory-mcp/dry-run.yml?label=CI)](https://github.com/DeusData/codebase-memory-mcp/actions/workflows/dry-run.yml)
- **The fastest and most efficient code intelligence engine for AI coding agents.** Full-indexes an average repository in milliseconds, the Linux kernel (28M LOC, 75K files) in 3 minutes. Answers structural queries in u...
- **One-line install** (macOS / Linux):

- Source: https://github.com/DeusData/codebase-memory-mcp
- Extracted from upstream docs: https://raw.githubusercontent.com/DeusData/codebase-memory-mcp/HEAD/README.md

## Documentation

- https://github.com/DeusData/codebase-memory-mcp

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/index-codebases-into-mcp-knowledge-graphs-with-codebase-memory-mcp/)
