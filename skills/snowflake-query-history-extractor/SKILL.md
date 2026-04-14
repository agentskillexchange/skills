---
title: "Snowflake Query History Extractor"
description: "Extracts query history and performance metadata from Snowflake using the Snowflake Python Connector and INFORMATION_SCHEMA.QUERY_HISTORY view. Identifies expensive queries by credits consumed, data scanned, and spillage to remote storage. Exports results to a Pandas DataFrame for downstream analysis or Slack reporting."
verification: security_reviewed
source: "https://pypi.org/project/snowflake-connector-python/"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "ChatGPT Agents"
---

# Snowflake Query History Extractor

This skill connects to Snowflake using the snowflake-connector-python library with key-pair authentication or username/password. It queries the SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY view (or INFORMATION_SCHEMA.QUERY_HISTORY for session-scoped analysis) to retrieve query executions over a configurable time window. Queries are ranked by CREDITS_USED_CLOUD_SERVICES, BYTES_SCANNED, and BYTES_SPILLED_TO_REMOTE_STORAGE. The skill identifies warehouse sizing inefficiencies by comparing actual bytes scanned against partition pruning ratios derived from PARTITIONS_TOTAL and PARTITIONS_SCANNED columns. Results are loaded into a Pandas DataFrame and can be exported as CSV, pushed to a Snowflake staging table, or formatted as a Slack Block Kit message via the Slack Web API. Supports multi-account analysis using Snowflake Organization Account Usage views.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snowflake-query-history-extractor/)
