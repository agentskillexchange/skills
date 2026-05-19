---
name: "Build a self-updating agent memory graph with GBrain"
slug: "build-a-self-updating-agent-memory-graph-with-gbrain"
description: "Use GBrain to give OpenClaw or Hermes-style agents a local knowledge brain with markdown ingestion, entity links, hybrid search, scheduled consolidation, and MCP access."
github_stars: 17347
verification: "listed"
source: "https://github.com/garrytan/gbrain"
author: "Garry Tan"
publisher_type: "individual"
category: "Templates & Workflows"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "garrytan/gbrain"
  github_stars: 17347
---

# Build a self-updating agent memory graph with GBrain

Use GBrain to give OpenClaw or Hermes-style agents a local knowledge brain with markdown ingestion, entity links, hybrid search, scheduled consolidation, and MCP access.

## Prerequisites

GBrain CLI, Bun/Node-compatible runtime, PGLite or Postgres with pgvector, markdown knowledge base, optional MCP server deployment

## Installation

Requirements and caveats from upstream:
- gbrain init --pglite # 2 seconds; no server, no Docker
- Run bun run test for the fast loop, bun run verify for the pre-push gate, bun run ci:local to run the full Docker-backed CI stack locally. Detailed test discipline in [CONTRIBUTING.md](CONTRIBUTING.md).

Basic usage or getting-started notes:
- Built by the President and CEO of Y Combinator to run his actual AI agents. The production brain behind his OpenClaw and Hermes deployments: **17,888 pages, 4,383 people, 723 companies**, 21 cron jobs running autonomo...
- **New in v0.35.7 — Temporal trajectory + founder scorecard.** Author typed metric assertions in the ## Facts fence (mrr=50000, arr=2000000, team_size=12) and gbrain stores them as first-class typed columns. gbrain eva...
- GBrain runs in three shapes. Pick the one that matches how you use AI agents today.

- Source: https://github.com/garrytan/gbrain
- Extracted from upstream docs: https://raw.githubusercontent.com/garrytan/gbrain/HEAD/README.md

## Documentation

- https://github.com/garrytan/gbrain/blob/master/llms.txt

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-a-self-updating-agent-memory-graph-with-gbrain/)
