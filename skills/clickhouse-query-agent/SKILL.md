---
name: "ClickHouse Query Agent"
description: "Execute analytical SQL queries against ClickHouse clusters, inspect table schemas, and monitor query performance through an AI agent interface. Supports materialized view management and partition-level operations for high-volume time-series data."
category: "Data Extraction & Transformation"
framework: "Custom Agents"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/clickhouse-query-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "clickhouse"  # from ase_tool_match
  github_stars: 46508  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 1471334  # from ase_npm_downloads
  github_repo: "ClickHouse/ClickHouse"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# ClickHouse Query Agent

Execute analytical SQL queries against ClickHouse clusters, inspect table schemas, and monitor query performance through an AI agent interface. Supports materialized view management and partition-level operations for high-volume time-series data.

## Overview

Execute analytical SQL queries against ClickHouse clusters, inspect table schemas, and monitor query performance through an AI agent interface. Supports materialized view management and partition-level operations for high-volume time-series data.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill clickhouse-query-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill clickhouse-query-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill clickhouse-query-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill clickhouse-query-agent -a codex
```

### OpenClaw

```bash
clawhub install clickhouse-query-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/clickhouse-query-agent/
