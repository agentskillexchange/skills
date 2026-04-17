---
title: "Snowflake Query History Extractor"
description: "This skill connects to Snowflake using the snowflake-connector-python library with key-pair authentication or username/password. It queries the SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY view (or INFORMATION_SCHEMA.QUERY_HISTORY for session-scoped analysis) to retrieve query executions over a configurable time window. Queries are ranked by CREDITS_USED_CLOUD_SERVICES, BYTES_SCANNED, and BYTES_SPILLED_TO_REMOTE_STORAGE. The skill identifies warehouse sizing inefficiencies by comparing actual bytes scanned against partition pruning ratios derived from PARTITIONS_TOTAL and PARTITIONS_SCANNED columns. Results are loaded into a Pandas DataFrame and can be exported as CSV, pushed to a Snowflake staging table, or formatted as a Slack Block Kit message via the Slack Web API. Supports multi-account analysis using Snowflake Organization Account Usage views."
verification: security_reviewed
source: "https://pypi.org/project/snowflake-connector-python/"
framework:
  - "ChatGPT Agents"
---

# Snowflake Query History Extractor

This skill connects to Snowflake using the snowflake-connector-python library with key-pair authentication or username/password. It queries the SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY view (or INFORMATION_SCHEMA.QUERY_HISTORY for session-scoped analysis) to retrieve query executions over a configurable time window. Queries are ranked by CREDITS_USED_CLOUD_SERVICES, BYTES_SCANNED, and BYTES_SPILLED_TO_REMOTE_STORAGE. The skill identifies warehouse sizing inefficiencies by comparing actual bytes scanned against partition pruning ratios derived from PARTITIONS_TOTAL and PARTITIONS_SCANNED columns. Results are loaded into a Pandas DataFrame and can be exported as CSV, pushed to a Snowflake staging table, or formatted as a Slack Block Kit message via the Slack Web API. Supports multi-account analysis using Snowflake Organization Account Usage views.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/snowflake-query-history-extractor
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/snowflake-query-history-extractor` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snowflake-query-history-extractor/)
