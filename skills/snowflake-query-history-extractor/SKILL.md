---
title: "Snowflake Query History Extractor"
slug: "snowflake-query-history-extractor"
description: "Extracts query history and performance metadata from Snowflake using the Snowflake Python Connector and INFORMATION_SCHEMA.QUERY_HISTORY view. Identifies expensive queries by credits consumed, data scanned, and spillage to remote storage. Exports results to a Pandas DataFrame for downstream analysis or Slack reporting."
category: "Data Extraction &amp; Transformation"
framework: "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/snowflake-query-history-extractor/"
---

# Snowflake Query History Extractor

Extracts query history and performance metadata from Snowflake using the Snowflake Python Connector and INFORMATION_SCHEMA.QUERY_HISTORY view. Identifies expensive queries by credits consumed, data scanned, and spillage to remote storage. Exports results to a Pandas DataFrame for downstream analysis or Slack reporting.

## Installation

Choose the setup path that fits your environment:

1. Clone or download this skill into your skills directory.
2. Install it through your agent platform's skill manager if supported.
3. Add it as a Git submodule or vendored folder in your repo.
4. Copy the files into a local custom skills/workspace directory.
5. Pull it from the Agent Skill Exchange catalog or this GitHub repo.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snowflake-query-history-extractor/)
