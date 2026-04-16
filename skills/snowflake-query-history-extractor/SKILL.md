---
title: "Snowflake Query History Extractor"
description: "Extracts query history and performance metadata from Snowflake using the Snowflake Python Connector and INFORMATION_SCHEMA.QUERY_HISTORY view. Identifies expensive queries by credits consumed, data scanned, and spillage to remote storage. Exports results to a Pandas DataFrame for downstream analysis or Slack reporting."
verification: "security_reviewed"
source: "https://pypi.org/project/snowflake-connector-python/"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  license: "Apache-2.0"
---

# Snowflake Query History Extractor

This skill connects to Snowflake using the snowflake-connector-python library with key-pair authentication or username/password. It queries the SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY view (or INFORMATION_SCHEMA.QUERY_HISTORY for session-scoped analysis) to retrieve query executions over a configurable time window. Queries are ranked by CREDITS_USED_CLOUD_SERVICES, BYTES_SCANNED, and BYTES_SPILLED_TO_REMOTE_STORAGE. The skill identifies warehouse sizing inefficiencies by comparing actual bytes scanned against partition pruning ratios derived from PARTITIONS_TOTAL and PARTITIONS_SCANNED columns. Results are loaded into a Pandas DataFrame and can be exported as CSV, pushed to a Snowflake staging table, or formatted as a Slack Block Kit message via the Slack Web API. Supports multi-account analysis using Snowflake Organization Account Usage views.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snowflake-query-history-extractor/)
