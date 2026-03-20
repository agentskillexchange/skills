---
name: Snowflake Query History Extractor
description: Extracts query history and performance metadata from Snowflake using the Snowflake Python Connector and INFORMATION_SCHEMA.QUERY_HISTORY view. Identifies expensive queries by credits consumed, data scanned, and spillage to remote storage. Exports results to a Pandas DataFrame for downstream analysis or Slack reporting.
category: Data Extraction &amp; Transformation
framework: Any Agent
verification: verified_metadata
rating: 4.5
reviews: 19
source: https://agentskillexchange.com/skill/snowflake-query-history-extractor/
---

# Snowflake Query History Extractor

Extracts query history and performance metadata from Snowflake using the Snowflake Python Connector and INFORMATION_SCHEMA.QUERY_HISTORY view. Identifies expensive queries by credits consumed, data scanned, and spillage to remote storage. Exports results to a Pandas DataFrame for downstream analysis or Slack reporting.

## Overview

Extracts query history and performance metadata from Snowflake using the Snowflake Python Connector and INFORMATION_SCHEMA.QUERY_HISTORY view. Identifies expensive queries by credits consumed, data scanned, and spillage to remote storage. Exports results to a Pandas DataFrame for downstream analysis or Slack reporting.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill snowflake-query-history-extractor
```

### OpenClaw

```bash
clawhub install snowflake-query-history-extractor
```

### Claude Code

```bash
claude mcp add snowflake-query-history-extractor
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/snowflake-query-history-extractor/) for detailed installation instructions.

## Verification

- **Status**: verified_metadata
- **Category**: Data Extraction &amp; Transformation
- **Framework**: Any Agent
- **Rating**: 4.5/5 (19 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/snowflake-query-history-extractor/)
