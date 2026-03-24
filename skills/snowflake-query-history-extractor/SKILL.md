---
name: "Snowflake Query History Extractor"
description: "Extracts query history and performance metadata from Snowflake using the Snowflake Python Connector and INFORMATION_SCHEMA.QUERY_HISTORY view. Identifies expensive queries by credits consumed, data scanned, and spillage to remote storage. Exports results to a Pandas DataFrame for downstream analysis or Slack reporting."
category: "Data Extraction & Transformation"
framework: "ChatGPT Agents"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/snowflake-query-history-extractor/"
tool_ecosystem:
  tool: "snowflake"
  github_stars: 0
  npm_weekly_downloads: 0
  github_repo: ""
  license: ""
  maintained: false
---

# Snowflake Query History Extractor

Extracts query history and performance metadata from Snowflake using the Snowflake Python Connector and INFORMATION_SCHEMA.QUERY_HISTORY view. Identifies expensive queries by credits consumed, data scanned, and spillage to remote storage. Exports results to a Pandas DataFrame for downstream analysis or Slack reporting.

## Installation

### Any Agent (npx)
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

| | |
|---|---|
| **Category** | Data Extraction & Transformation |
| **Framework** | ChatGPT Agents |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | snowflake |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/snowflake-query-history-extractor/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
