---
name: Snowflake Query History Extractor
description: Extracts query history and performance metadata from Snowflake using
  the Snowflake Python Connector and INFORMATION_SCHEMA.QUERY_HISTORY view. Identifies
  expensive queries by credits consumed, data scanned, and spillage to remote storage.
  Exports results to a Pandas DataFrame for downstream analysis or Slack reporting.
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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snowflake-query-history-extractor/)
