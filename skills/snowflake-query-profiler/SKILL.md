---
title: Snowflake Query Profiler
description: The Snowflake Query Profiler skill analyzes query performance patterns
  using Snowflake Information Schema views and the QUERY_HISTORY table function. It
  identifies expensive queries by examining bytes scanned, compilation time, execution
  time, and spillage to local and remote storage. The skill recommends optimization
  strategies including clustering key selection based on filter and join predicate
  analysis, search optimization service candidates from SYSTEM$CLUSTERING_INFORMATION,
  and warehouse auto-scaling configuration tuning. Features include query plan visualization
  from GET_QUERY_OPERATOR_STATS, automatic identification of partition pruning failures,
  and materialized view recommendation based on repetitive subquery patterns. Integrates
  with Snowflake Resource Monitors API for cost correlation and supports Snowsight
  dashboard generation for ongoing performance tracking.
verification: security_reviewed
source: https://agentskillexchange.com/skills/snowflake-query-profiler/
category:
- Data Extraction &amp; Transformation
framework:
- ChatGPT Agents
---

# Snowflake Query Profiler

The Snowflake Query Profiler skill analyzes query performance patterns using Snowflake Information Schema views and the QUERY_HISTORY table function. It identifies expensive queries by examining bytes scanned, compilation time, execution time, and spillage to local and remote storage. The skill recommends optimization strategies including clustering key selection based on filter and join predicate analysis, search optimization service candidates from SYSTEM$CLUSTERING_INFORMATION, and warehouse auto-scaling configuration tuning. Features include query plan visualization from GET_QUERY_OPERATOR_STATS, automatic identification of partition pruning failures, and materialized view recommendation based on repetitive subquery patterns. Integrates with Snowflake Resource Monitors API for cost correlation and supports Snowsight dashboard generation for ongoing performance tracking.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snowflake-query-profiler/)
