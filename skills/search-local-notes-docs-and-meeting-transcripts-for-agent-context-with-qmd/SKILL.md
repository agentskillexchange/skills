---
title: "Search local notes, docs, and meeting transcripts for agent context with QMD"
description: "Index local notes, docs, and meeting transcripts, then return ranked files or structured JSON so an agent can pull only the context it needs."
verification: "security_reviewed"
source: "https://github.com/tobi/qmd"
author: "tobi"
publisher_type: "open_source_project"
category:
  - "Research & Scraping"
framework:
  - "Multi-Framework"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
npm install -g @tobilu/qmd or bun install -g @tobilu/qmd
```

## Documentation

- https://github.com/tobi/qmd

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/search-local-notes-docs-and-meeting-transcripts-for-agent-context-with-qmd/)
