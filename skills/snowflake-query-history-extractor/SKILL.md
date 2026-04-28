---
title: "Snowflake Query History Extractor"
description: "Extracts query history and performance metadata from Snowflake using the Snowflake Python Connector and INFORMATION_SCHEMA.QUERY_HISTORY view. Identifies expensive queries by credits consumed, data scanned, and spillage to remote storage. Exports results to a Pandas DataFrame for downstream analysis or Slack reporting."
verification: security_reviewed
source: "https://pypi.org/project/snowflake-connector-python/"
category:
  - "Data Extraction & Transformation"
framework:
  - "ChatGPT Agents"
---

# Snowflake Query History Extractor

Extracts query history and performance metadata from Snowflake using the Snowflake Python Connector and INFORMATION_SCHEMA.QUERY_HISTORY view. Identifies expensive queries by credits consumed, data scanned, and spillage to remote storage. Exports results to a Pandas DataFrame for downstream analysis or Slack reporting.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/snowflake-query-history-extractor/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/snowflake-query-history-extractor
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/snowflake-query-history-extractor`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snowflake-query-history-extractor/)
