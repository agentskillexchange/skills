---
name: "Snowflake Query History Extractor"
description: "Extracts query history and performance metadata from Snowflake using the Snowflake Python Connector and INFORMATION_SCHEMA.QUERY_HISTORY view. Identifies expensive queries by credits consumed, data scanned, and spillage to remote storage. Exports results to a Pandas DataFrame for downstream analysis or Slack reporting."
category: "Data Extraction & Transformation"
framework: "ChatGPT Agents"
verification: verified_metadata
rating: 4.5
reviews: 19
creator: "Leo Park"
creator_handle: "@leopark"
creator_verified: true
source: "https://agentskillexchange.com/skills/snowflake-query-history-extractor/"
---
# Snowflake Query History Extractor

Extracts query history and performance metadata from Snowflake using the Snowflake Python Connector and INFORMATION_SCHEMA.QUERY_HISTORY view. Identifies expensive queries by credits consumed, data scanned, and spillage to remote storage. Exports results to a Pandas DataFrame for downstream analysis or Slack reporting.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill snowflake-query-history-extractor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill snowflake-query-history-extractor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill snowflake-query-history-extractor -a cursor
```

### OpenClaw

```bash
clawhub install snowflake-query-history-extractor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill snowflake-query-history-extractor -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Data Extraction & Transformation |
| Framework | ChatGPT Agents |
| Verification | Verified Metadata |
| Rating | 4.5/5 (19 reviews) |

## Creator

**Leo Park** (Verified Creator ✓)
- Profile: [@leopark](https://agentskillexchange.com/browse-skills/?creator=leopark)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/snowflake-query-history-extractor/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
