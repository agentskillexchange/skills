---
title: "Build temporal context graphs for agent memory from evolving facts with Graphiti"
description: "Use Graphiti when an agent needs long-term memory that tracks what changed, when it changed, and which source episode produced each fact, instead of storing flat chunks or chat history alone."
verification: "security_reviewed"
source: "https://github.com/getzep/graphiti"
author: "Zep"
publisher_type: "company"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "getzep/graphiti"
  github_stars: 24898
  npm_package: "graphiti-core"
  npm_weekly_downloads: 529336
---

# Build temporal context graphs for agent memory from evolving facts with Graphiti

Use Graphiti when an agent needs long-term memory that tracks what changed, when it changed, and which source episode produced each fact, instead of storing flat chunks or chat history alone.

## Prerequisites

Python environment, Graphiti library, backing graph/database components per Graphiti docs, agent application that can ingest episodes and query memory.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Graphiti in your Python environment, configure the storage back end described in the Graphiti docs, define the entity and relationship types your agent needs, then connect your ingestion pipeline so new episodes continuously update the temporal graph before querying it from your agent runtime.
```

## Documentation

- https://help.getzep.com/graphiti

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-temporal-context-graphs-for-agent-memory-from-evolving-facts-with-graphiti/)
