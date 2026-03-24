---
name: "Parquet Schema Extractor for S3"
description: "Extracts and validates Parquet file schemas from Amazon S3 using the PyArrow library and AWS S3 SDK (boto3). Compares schemas across multiple partitions to detect schema drift and incompatible type changes. Outputs a schema diff report with partition paths and affected column details."
category: "Data Extraction & Transformation"
framework: "Gemini"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/parquet-schema-extractor-for-s3/"
tool_ecosystem:
  tool: "parquet"
  github_stars: 387
  npm_weekly_downloads: 146943
  github_repo: "ironSource/parquetjs"
  license: "MIT"
  maintained: false
---

# Parquet Schema Extractor for S3

Extracts and validates Parquet file schemas from Amazon S3 using the PyArrow library and AWS S3 SDK (boto3). Compares schemas across multiple partitions to detect schema drift and incompatible type changes. Outputs a schema diff report with partition paths and affected column details.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill parquet-schema-extractor-for-s3
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill parquet-schema-extractor-for-s3 -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill parquet-schema-extractor-for-s3 -a cursor
```

### OpenClaw
```bash
clawhub install parquet-schema-extractor-for-s3
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill parquet-schema-extractor-for-s3 -a codex
```

## Details

| | |
|---|---|
| **Category** | Data Extraction & Transformation |
| **Framework** | Gemini |
| **Verification** | 📋 Listed |
| **Tool** | [parquet](https://github.com/ironSource/parquetjs) — ⭐ 387 · MIT |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/parquet-schema-extractor-for-s3/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
