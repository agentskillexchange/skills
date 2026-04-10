---
title: "Snowflake Query Optimizer Agent"
description: "Analyzes and optimizes Snowflake SQL queries using the QUERY_HISTORY and ACCESS_HISTORY views in ACCOUNT_USAGE. Identifies expensive scans, recommends clustering keys, and monitors warehouse credit consumption via WAREHOUSE_METERING_HISTORY."
slug: "snowflake-query-optimizer-agent"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/snowflake-query-optimizer-agent/"
listed: true
---

# Snowflake Query Optimizer Agent

Analyzes and optimizes Snowflake SQL queries using the QUERY_HISTORY and ACCESS_HISTORY views in ACCOUNT_USAGE. Identifies expensive scans, recommends clustering keys, and monitors warehouse credit consumption via WAREHOUSE_METERING_HISTORY.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install snowflake-query-optimizer-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Snowflake Query Optimizer Agent analyzes SQL performance using Snowflake’s ACCOUNT_USAGE schema views. It queries QUERY_HISTORY for execution metrics including bytes scanned, compilation time, queuing time, and spill-to-disk indicators to identify optimization candidates.
Core analysis includes scanning ACCESS_HISTORY for column-level access patterns to recommend optimal clustering keys via ALTER TABLE ... CLUSTER BY. The skill evaluates micro-partition pruning efficiency using SYSTEM$CLUSTERING_INFORMATION() and recommends re-clustering when overlap depth exceeds thresholds.
Cost management features monitor WAREHOUSE_METERING_HISTORY for credit consumption trends, identify idle warehouses with auto-suspend recommendations, and analyze WAREHOUSE_LOAD_HISTORY for right-sizing decisions. The agent generates query profiles using SYSTEM$EXPLAIN_JSON_TO_TEXT() for visual execution plan analysis. It detects common anti-patterns: SELECT *, unnecessary ORDER BY in subqueries, cross joins, and functions on filter columns preventing pruning. Supports materialized view recommendations based on repeated query patterns from QUERY_HISTORY aggregation. Monitors data sharing and replication costs across regions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snowflake-query-optimizer-agent/)
