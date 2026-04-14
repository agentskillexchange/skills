---
title: "Snowflake Query Profiler"
description: "Profiles and optimizes Snowflake SQL queries using the Snowflake Information Schema and Query History views. Identifies warehouse sizing issues, scanning inefficiencies, and recommends clustering keys."
verification: security_reviewed
source: "https://pypi.org/project/snowflake-connector-python/"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "ChatGPT Agents"
---

# Snowflake Query Profiler

The Snowflake Query Profiler skill analyzes query performance patterns using Snowflake Information Schema views and the QUERY_HISTORY table function. It identifies expensive queries by examining bytes scanned, compilation time, execution time, and spillage to local and remote storage. The skill recommends optimization strategies including clustering key selection based on filter and join predicate analysis, search optimization service candidates from SYSTEM$CLUSTERING_INFORMATION, and warehouse auto-scaling configuration tuning. Features include query plan visualization from GET_QUERY_OPERATOR_STATS, automatic identification of partition pruning failures, and materialized view recommendation based on repetitive subquery patterns. Integrates with Snowflake Resource Monitors API for cost correlation and supports Snowsight dashboard generation for ongoing performance tracking.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snowflake-query-profiler/)
