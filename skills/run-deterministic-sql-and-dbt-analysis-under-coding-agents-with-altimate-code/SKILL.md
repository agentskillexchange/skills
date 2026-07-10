---
title: "Run deterministic SQL and dbt analysis under coding agents with Altimate Code"
description: "Adds deterministic SQL analysis, dbt-aware tooling, warehouse metadata, lineage, and test-generation workflows underneath Claude Code, Codex, or terminal-driven agent sessions."
verification: "listed"
source: "https://github.com/AltimateAI/altimate-code"
author: "Altimate AI"
publisher_type: "Organization"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "AltimateAI/altimate-code"
  github_stars: 552
  npm_package: "altimate-code"
  npm_weekly_downloads: 195
---

# Run deterministic SQL and dbt analysis under coding agents with Altimate Code

Adds deterministic SQL analysis, dbt-aware tooling, warehouse metadata, lineage, and test-generation workflows underneath Claude Code, Codex, or terminal-driven agent sessions.

## Prerequisites

altimate-code CLI, an LLM provider key or local model, and optional dbt project or warehouse credentials for the deterministic data-engineering workflows

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with npm install -g altimate-code, launch altimate, configure the LLM provider, and optionally run /discover to index the local dbt project, warehouse connections, and related tools before invoking the SQL and dbt workflows.
```

## Documentation

- https://altimate.sh

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-deterministic-sql-and-dbt-analysis-under-coding-agents-with-altimate-code/)
