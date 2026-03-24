---
name: "SQL Query Optimizer"
description: "Use this skill when you need to analyze and optimize slow SQL queries by reviewing query plans, index usage, and table statistics. It takes a SQL query and EXPLAIN output, identifies inefficiencies like full table scans and missing indexes, and suggests optimized query rewrites."
category: "Data Extraction & Transformation"
framework: "Claude Agents"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/sql-query-optimizer/"
---

# SQL Query Optimizer

Use this skill when you need to analyze and optimize slow SQL queries by reviewing query plans, index usage, and table statistics. It takes a SQL query and EXPLAIN output, identifies inefficiencies like full table scans and missing indexes, and suggests optimized query rewrites.

## Overview

Use this skill when you need to analyze and optimize slow SQL queries by reviewing query plans, index usage, and table statistics. It takes a SQL query and EXPLAIN output, identifies inefficiencies like full table scans and missing indexes, and suggests optimized query rewrites.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sql-query-optimizer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sql-query-optimizer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sql-query-optimizer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sql-query-optimizer -a codex
```

### OpenClaw

```bash
clawhub install sql-query-optimizer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/sql-query-optimizer/
