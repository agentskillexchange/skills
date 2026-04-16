---
title: "Snowflake Query Profiler"
description: "Profiles and optimizes Snowflake SQL queries using the Snowflake Information Schema and Query History views. Identifies warehouse sizing issues, scanning inefficiencies, and recommends clustering keys."
verification: "security_reviewed"
source: "https://pypi.org/project/snowflake-connector-python/"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  license: "Apache-2.0"
---

# Snowflake Query Profiler

The Snowflake Query Profiler skill analyzes query performance patterns using Snowflake Information Schema views and the QUERY_HISTORY table function. It identifies expensive queries by examining bytes scanned, compilation time, execution time, and spillage to local and remote storage. The skill recommends optimization strategies including clustering key selection based on filter and join predicate analysis, search optimization service candidates from SYSTEM$CLUSTERING_INFORMATION, and warehouse auto-scaling configuration tuning. Features include query plan visualization from GET_QUERY_OPERATOR_STATS, automatic identification of partition pruning failures, and materialized view recommendation based on repetitive subquery patterns. Integrates with Snowflake Resource Monitors API for cost correlation and supports Snowsight dashboard generation for ongoing performance tracking.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snowflake-query-profiler/)
