---
title: "Snowflake Query Profiler"
description: "The Snowflake Query Profiler skill analyzes query performance patterns using Snowflake Information Schema views and the QUERY_HISTORY table function. It identifies expensive queries by examining bytes scanned, compilation time, execution time, and spillage to local and remote storage. The skill recommends optimization strategies including clustering key selection based on filter and join predicate analysis, search optimization service candidates from SYSTEM$CLUSTERING_INFORMATION, and warehouse auto-scaling configuration tuning. Features include query plan visualization from GET_QUERY_OPERATOR_STATS, automatic identification of partition pruning failures, and materialized view recommendation based on repetitive subquery patterns. Integrates with Snowflake Resource Monitors API for cost correlation and supports Snowsight dashboard generation for ongoing performance tracking."
verification: security_reviewed
source: "https://pypi.org/project/snowflake-connector-python/"
framework:
  - "ChatGPT Agents"
---

# Snowflake Query Profiler

The Snowflake Query Profiler skill analyzes query performance patterns using Snowflake Information Schema views and the QUERY_HISTORY table function. It identifies expensive queries by examining bytes scanned, compilation time, execution time, and spillage to local and remote storage. The skill recommends optimization strategies including clustering key selection based on filter and join predicate analysis, search optimization service candidates from SYSTEM$CLUSTERING_INFORMATION, and warehouse auto-scaling configuration tuning. Features include query plan visualization from GET_QUERY_OPERATOR_STATS, automatic identification of partition pruning failures, and materialized view recommendation based on repetitive subquery patterns. Integrates with Snowflake Resource Monitors API for cost correlation and supports Snowsight dashboard generation for ongoing performance tracking.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/snowflake-query-profiler
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/snowflake-query-profiler` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snowflake-query-profiler/)
