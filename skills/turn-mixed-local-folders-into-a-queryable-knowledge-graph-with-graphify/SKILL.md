---
name: "Turn mixed local folders into a queryable knowledge graph with Graphify"
slug: "turn-mixed-local-folders-into-a-queryable-knowledge-graph-with-graphify"
description: "Ingest code, docs, PDFs, images, and video from local folders into a searchable knowledge graph so agents can follow entities and relationships instead of only raw text."
github_stars: 25688
verification: "listed"
source: "https://github.com/safishamsi/graphify"
author: "safishamsi"
publisher_type: "individual"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "safishamsi/graphify"
  github_stars: 25688
---

# Turn mixed local folders into a queryable knowledge graph with Graphify

Ingest code, docs, PDFs, images, and video from local folders into a searchable knowledge graph so agents can follow entities and relationships instead of only raw text.

## Prerequisites

Graphify CLI or MCP server, local project/document folders

## Installation

Use the upstream install or setup path that matches your environment:
- uv tool install graphifyy
- pipx install graphifyy
- pip install graphifyy
- **graphify: command not found?** Use uv tool install graphifyy or pipx install graphifyy — both put the CLI on PATH automatically. With plain pip, add ~/.local/bin (Linux) or ~/Library/Python/3.x/bin (Mac) to your PAT...

Requirements and caveats from upstream:
- | leiden | Leiden community detection (Python < 3.13 only) | pip install "graphifyy[leiden]" |
- /graphify . --cluster-only --exclude-hubs 99 # suppress utility super-hubs from god-node rankings

Basic usage or getting-started notes:
- For a readable architecture page with Mermaid call-flow diagrams, run:
- **Official package:** The PyPI package is graphifyy (double-y). Other graphify* packages on PyPI are not affiliated. The CLI command is still graphify.
- **Step 1 — install the package:**

- Source: https://github.com/safishamsi/graphify
- Extracted from upstream docs: https://raw.githubusercontent.com/safishamsi/graphify/HEAD/README.md

## Documentation

- https://github.com/safishamsi/graphify#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/turn-mixed-local-folders-into-a-queryable-knowledge-graph-with-graphify/)
