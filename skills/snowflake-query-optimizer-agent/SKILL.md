---
title: "Snowflake Query Optimizer Agent"
description: "Analyzes and optimizes Snowflake SQL queries using the QUERY_HISTORY and ACCESS_HISTORY views in ACCOUNT_USAGE. Identifies expensive scans, recommends clustering keys, and monitors warehouse credit consumption via WAREHOUSE_METERING_HISTORY."
verification: "security_reviewed"
source: "https://pypi.org/project/snowflake-connector-python/"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "OpenClaw"
tool_ecosystem:
  license: "Apache-2.0"
---

# Snowflake Query Optimizer Agent

The Snowflake Query Optimizer Agent analyzes SQL performance using Snowflake’s ACCOUNT_USAGE schema views. It queries QUERY_HISTORY for execution metrics including bytes scanned, compilation time, queuing time, and spill-to-disk indicators to identify optimization candidates.

Core analysis includes scanning ACCESS_HISTORY for column-level access patterns to recommend optimal clustering keys via ALTER TABLE ... CLUSTER BY. The skill evaluates micro-partition pruning efficiency using SYSTEM$CLUSTERING_INFORMATION() and recommends re-clustering when overlap depth exceeds thresholds.

Cost management features monitor WAREHOUSE_METERING_HISTORY for credit consumption trends, identify idle warehouses with auto-suspend recommendations, and analyze WAREHOUSE_LOAD_HISTORY for right-sizing decisions. The agent generates query profiles using SYSTEM$EXPLAIN_JSON_TO_TEXT() for visual execution plan analysis. It detects common anti-patterns: SELECT *, unnecessary ORDER BY in subqueries, cross joins, and functions on filter columns preventing pruning. Supports materialized view recommendations based on repeated query patterns from QUERY_HISTORY aggregation. Monitors data sharing and replication costs across regions.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snowflake-query-optimizer-agent/)
