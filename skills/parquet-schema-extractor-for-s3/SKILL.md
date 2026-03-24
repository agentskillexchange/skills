---
name: "Parquet Schema Extractor for S3"
description: "Extracts and validates Parquet file schemas from Amazon S3 using the PyArrow library and AWS S3 SDK (boto3). Compares schemas across multiple partitions to detect schema drift and incompatible type changes. Outputs a schema diff report with partition paths and affected column details."
category: "Data Extraction & Transformation"
framework: "Gemini"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/parquet-schema-extractor-for-s3/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "parquet"  # from ase_tool_match
  github_stars: 387  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 146943  # from ase_npm_downloads
  github_repo: "ironSource/parquetjs"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: false  # from ase_tool_maintained
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

- Marketplace: https://agentskillexchange.com/skills/parquet-schema-extractor-for-s3/
