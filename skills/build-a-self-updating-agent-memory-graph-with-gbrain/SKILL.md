---
title: "Build a self-updating agent memory graph with GBrain"
description: "Use GBrain to give OpenClaw or Hermes-style agents a local knowledge brain with markdown ingestion, entity links, hybrid search, scheduled consolidation, and MCP access."
verification: "security_reviewed"
source: "https://github.com/garrytan/gbrain"
author: "Garry Tan"
publisher_type: "individual"
category:
  - "Templates & Workflows"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "garrytan/gbrain"
  github_stars: 17347
---

# Build a self-updating agent memory graph with GBrain

Use GBrain to give OpenClaw or Hermes-style agents a local knowledge brain with markdown ingestion, entity links, hybrid search, scheduled consolidation, and MCP access.

## Prerequisites

GBrain CLI, Bun/Node-compatible runtime, PGLite or Postgres with pgvector, markdown knowledge base, optional MCP server deployment

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Follow the upstream INSTALL_FOR_AGENTS.md and AGENTS.md protocol, install the GBrain CLI from the GitHub source, choose PGLite for local use or Postgres for scale, then run gbrain doctor --json and configure ingestion, cron jobs, and optional MCP deployment.
```

## Documentation

- https://github.com/garrytan/gbrain/blob/master/llms.txt

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-a-self-updating-agent-memory-graph-with-gbrain/)
