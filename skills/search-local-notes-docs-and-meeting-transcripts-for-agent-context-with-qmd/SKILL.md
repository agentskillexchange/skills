---
name: "Search local notes, docs, and meeting transcripts for agent context with QMD"
slug: "search-local-notes-docs-and-meeting-transcripts-for-agent-context-with-qmd"
description: "Index local notes, docs, and meeting transcripts, then return ranked files or structured JSON so an agent can pull only the context it needs."
github_stars: 22082
verification: "listed"
source: "https://github.com/tobi/qmd"
author: "tobi"
publisher_type: "open_source_project"
category: "Research & Scraping"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "tobi/qmd"
  github_stars: 22082
  npm_package: "@tobilu/qmd"
  npm_weekly_downloads: 25854
---

# Search local notes, docs, and meeting transcripts for agent context with QMD

Index local notes, docs, and meeting transcripts, then return ranked files or structured JSON so an agent can pull only the context it needs.

## Prerequisites

Node or Bun, local document folders, optional local GGUF model via node-llama-cpp for semantic search and reranking

## Installation

Use the upstream install or setup path that matches your environment:
- npm install -g @tobilu/qmd
- npx @tobilu/qmd ...
- npm install @tobilu/qmd
- brew install sqlite

Requirements and caveats from upstream:
- QMD combines BM25 full-text search, vector semantic search, and LLM re-ranking—all running locally via node-llama-cpp with GGUF models.
- Use QMD as a library in your own Node.js or Bun applications.
- The SDK requires explicit dbPath — no defaults are assumed. This makes it safe to embed in any application without side effects.

Basic usage or getting-started notes:
- sh
- # or
- bun install -g @tobilu/qmd

- Source: https://github.com/tobi/qmd
- Extracted from upstream docs: https://raw.githubusercontent.com/tobi/qmd/HEAD/README.md

## Documentation

- https://github.com/tobi/qmd

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/search-local-notes-docs-and-meeting-transcripts-for-agent-context-with-qmd/)
