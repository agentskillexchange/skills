---
title: Snowflake Query History Extractor
description: This skill connects to Snowflake using the snowflake-connector-python
  library with key-pair authentication or username/password. It queries the SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
  view (or INFORMATION_SCHEMA.QUERY_HISTORY for session-scoped analysis) to retrieve
  query executions over a configurable time window. Queries are ranked by CREDITS_USED_CLOUD_SERVICES,
  BYTES_SCANNED, and BYTES_SPILLED_TO_REMOTE_STORAGE. The skill identifies warehouse
  sizing inefficiencies by comparing actual bytes scanned against partition pruning
  ratios derived from PARTITIONS_TOTAL and PARTITIONS_SCANNED columns. Results are
  loaded into a Pandas DataFrame and can be exported as CSV, pushed to a Snowflake
  staging table, or formatted as a Slack Block Kit message via the Slack Web API.
  Supports multi-account analysis using Snowflake Organization Account Usage views.
verification: security_reviewed
source: https://agentskillexchange.com/skills/snowflake-query-history-extractor/
category:
- Data Extraction &amp; Transformation
framework:
- ChatGPT Agents
---

# Snowflake Query History Extractor

This skill connects to Snowflake using the snowflake-connector-python library with key-pair authentication or username/password. It queries the SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY view (or INFORMATION_SCHEMA.QUERY_HISTORY for session-scoped analysis) to retrieve query executions over a configurable time window. Queries are ranked by CREDITS_USED_CLOUD_SERVICES, BYTES_SCANNED, and BYTES_SPILLED_TO_REMOTE_STORAGE. The skill identifies warehouse sizing inefficiencies by comparing actual bytes scanned against partition pruning ratios derived from PARTITIONS_TOTAL and PARTITIONS_SCANNED columns. Results are loaded into a Pandas DataFrame and can be exported as CSV, pushed to a Snowflake staging table, or formatted as a Slack Block Kit message via the Slack Web API. Supports multi-account analysis using Snowflake Organization Account Usage views.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snowflake-query-history-extractor/)
