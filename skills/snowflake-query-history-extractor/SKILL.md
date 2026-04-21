---
title: "Snowflake Query History Extractor"
slug: "snowflake-query-history-extractor"
description: "Extracts query history and performance metadata from Snowflake using the Snowflake Python Connector and INFORMATION_SCHEMA.QUERY_HISTORY view. Identifies expensive queries by credits consumed, data scanned, and spillage to remote storage. Exports results to a Pandas DataFrame for downstream analysis or Slack reporting."
verification: security_reviewed
source: "https://pypi.org/project/snowflake-connector-python/"
framework:
  - "ChatGPT Agents"
---

# Snowflake Query History Extractor

Extracts query history and performance metadata from Snowflake using the Snowflake Python Connector and INFORMATION_SCHEMA.QUERY_HISTORY view. Identifies expensive queries by credits consumed, data scanned, and spillage to remote storage. Exports results to a Pandas DataFrame for downstream analysis or Slack reporting.

## Installation

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snowflake-query-history-extractor/)
