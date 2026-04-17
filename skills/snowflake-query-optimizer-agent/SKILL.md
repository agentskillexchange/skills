---
name: Snowflake Query Optimizer Agent
description: Analyzes and optimizes Snowflake SQL queries using the QUERY_HISTORY
  and ACCESS_HISTORY views in ACCOUNT_USAGE. Identifies expensive scans, recommends
  clustering keys, and monitors warehouse credit consumption via WAREHOUSE_METERING_HISTORY.
category: Data Extraction & Transformation
framework: OpenClaw
verification: security_reviewed
source: https://pypi.org/project/snowflake-connector-python/
---
# Snowflake Query Optimizer Agent
Analyzes and optimizes Snowflake SQL queries using the QUERY_HISTORY and ACCESS_HISTORY views in ACCOUNT_USAGE. Identifies expensive scans, recommends clustering keys, and monitors warehouse credit consumption via WAREHOUSE_METERING_HISTORY.

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
