---
name: "Snowflake Query Profiler"
description: "Profiles and optimizes Snowflake SQL queries using the Snowflake Information Schema and Query History views. Identifies warehouse sizing issues, scanning inefficiencies, and recommends clustering keys."
category: "Data Extraction & Transformation"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/snowflake-query-profiler/"
---
# Snowflake Query Profiler

Profiles and optimizes Snowflake SQL queries using the Snowflake Information Schema and Query History views. Identifies warehouse sizing issues, scanning inefficiencies, and recommends clustering keys.

The Snowflake Query Profiler skill analyzes query performance patterns using Snowflake Information Schema views and the QUERY_HISTORY table function. It identifies expensive queries by examining bytes scanned, compilation time, execution time, and spillage to local and remote storage. The skill recommends optimization strategies including clustering key selection based on filter and join predicate analysis, search optimization service candidates from SYSTEM$CLUSTERING_INFORMATION, and warehouse auto-scaling configuration tuning. Features include query plan visualization from GET_QUERY_OPERATOR_STATS, automatic identification of partition pruning failures, and materialized view recommendation based on repetitive subquery patterns. Integrates with Snowflake Resource Monitors API for cost correlation and supports Snowsight dashboard generation for ongoing performance tracking.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill snowflake-query-profiler
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill snowflake-query-profiler -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill snowflake-query-profiler -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill snowflake-query-profiler -a codex
```

### OpenClaw

```bash
clawhub install snowflake-query-profiler
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snowflake-query-profiler/)
