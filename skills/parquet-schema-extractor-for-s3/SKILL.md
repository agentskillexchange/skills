---
name: "Parquet Schema Extractor for S3"
description: "Extracts and validates Parquet file schemas from Amazon S3 using the PyArrow library and AWS S3 SDK (boto3). Compares schemas across multiple partitions to detect schema drift and incompatible type changes. Outputs a schema diff report with partition paths and affected column details."
category: "Data Extraction &amp; Transformation"
framework: "Gemini"
verification: security_reviewed
source: "https://github.com/ironsource/parquetjs"
tool_ecosystem:
  tool: parquet
  github_repo: ironsource/parquetjs
  github_stars: 387
  license: MIT
  maintained: false
---
# Parquet Schema Extractor for S3

Extracts and validates Parquet file schemas from Amazon S3 using the PyArrow library and AWS S3 SDK (boto3). Compares schemas across multiple partitions to detect schema drift and incompatible type changes. Outputs a schema diff report with partition paths and affected column details.

## Overview

This skill uses boto3 to list objects in an S3 prefix and downloads Parquet file footers using range requests (GetObject with Range header) to avoid full file downloads. PyArrow is used to parse the Parquet metadata footer and extract the schema including field names, data types, and nullable flags. The skill compares schemas across partition directories by hashing schema fingerprints and flagging deviations. Type compatibility checks follow Arrow type promotion rules to identify breaking changes (e.g., INT32 to STRING conversions). Schema history is optionally stored in an AWS DynamoDB table for drift tracking across daily pipeline runs. Output includes a Markdown schema diff report with the exact partition paths containing incompatible schemas and recommended schema evolution strategies for Apache Iceberg or Delta Lake tables.

## Installation

### Any Agent

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

### Codex

```bash
npx skills add agentskillexchange/skills --skill parquet-schema-extractor-for-s3 -a codex
```

### OpenClaw

```bash
clawhub install parquet-schema-extractor-for-s3
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parquet-schema-extractor-for-s3/)
