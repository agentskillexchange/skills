---
name: "Snowflake Query History Extractor"
slug: "snowflake-query-history-extractor"
description: "Extracts query history and performance metadata from Snowflake using the Snowflake Python Connector and INFORMATION_SCHEMA.QUERY_HISTORY view. Identifies expensive queries by credits consumed, data scanned, and spillage to remote storage. Exports results to a Pandas DataFrame for downstream analysis or Slack reporting."
github_stars: 724
verification: "security_reviewed"
source: "https://github.com/snowflakedb/snowflake-connector-python"
category: "Data Extraction & Transformation"
framework: "ChatGPT Agents"
tool_ecosystem:
  github_repo: "snowflakedb/snowflake-connector-python"
  github_stars: 724
---

# Snowflake Query History Extractor

Extracts query history and performance metadata from Snowflake using the Snowflake Python Connector and INFORMATION_SCHEMA.QUERY_HISTORY view. Identifies expensive queries by credits consumed, data scanned, and spillage to remote storage. Exports results to a Pandas DataFrame for downstream analysis or Slack reporting.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snowflake-query-history-extractor/)
