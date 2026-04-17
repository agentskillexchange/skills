---
title: "Snowflake Query Optimizer Agent"
description: "The Snowflake Query Optimizer Agent analyzes SQL performance using Snowflake’s ACCOUNT_USAGE schema views. It queries QUERY_HISTORY for execution metrics including bytes scanned, compilation time, queuing time, and spill-to-disk indicators to identify optimization candidates.\nCore analysis includes scanning ACCESS_HISTORY for column-level access patterns to recommend optimal clustering keys via ALTER TABLE ... CLUSTER BY. The skill evaluates micro-partition pruning efficiency using SYSTEM$CLUSTERING_INFORMATION() and recommends re-clustering when overlap depth exceeds thresholds.\nCost management features monitor WAREHOUSE_METERING_HISTORY for credit consumption trends, identify idle warehouses with auto-suspend recommendations, and analyze WAREHOUSE_LOAD_HISTORY for right-sizing decisions. The agent generates query profiles using SYSTEM$EXPLAIN_JSON_TO_TEXT() for visual execution plan analysis. It detects common anti-patterns: SELECT *, unnecessary ORDER BY in subqueries, cross joins, and functions on filter columns preventing pruning. Supports materialized view recommendations based on repeated query patterns from QUERY_HISTORY aggregation. Monitors data sharing and replication costs across regions."
verification: security_reviewed
source: "https://pypi.org/project/snowflake-connector-python/"
framework:
  - "OpenClaw"
---

# Snowflake Query Optimizer Agent

The Snowflake Query Optimizer Agent analyzes SQL performance using Snowflake’s ACCOUNT_USAGE schema views. It queries QUERY_HISTORY for execution metrics including bytes scanned, compilation time, queuing time, and spill-to-disk indicators to identify optimization candidates.
Core analysis includes scanning ACCESS_HISTORY for column-level access patterns to recommend optimal clustering keys via ALTER TABLE ... CLUSTER BY. The skill evaluates micro-partition pruning efficiency using SYSTEM$CLUSTERING_INFORMATION() and recommends re-clustering when overlap depth exceeds thresholds.
Cost management features monitor WAREHOUSE_METERING_HISTORY for credit consumption trends, identify idle warehouses with auto-suspend recommendations, and analyze WAREHOUSE_LOAD_HISTORY for right-sizing decisions. The agent generates query profiles using SYSTEM$EXPLAIN_JSON_TO_TEXT() for visual execution plan analysis. It detects common anti-patterns: SELECT *, unnecessary ORDER BY in subqueries, cross joins, and functions on filter columns preventing pruning. Supports materialized view recommendations based on repeated query patterns from QUERY_HISTORY aggregation. Monitors data sharing and replication costs across regions.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/snowflake-query-optimizer-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/snowflake-query-optimizer-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snowflake-query-optimizer-agent/)
