---
title: "Parquet Schema Extractor for S3"
description: "Extracts and validates Parquet file schemas from Amazon S3 using the PyArrow library and AWS S3 SDK (boto3). Compares schemas across multiple partitions to detect schema drift and incompatible type changes. Outputs a schema diff report with partition paths and affected column details."
verification: "security_reviewed"
source: "https://github.com/ironSource/parquetjs"
category:
  - "Data Extraction & Transformation"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "ironsource/parquetjs"
  github_stars: 387
  npm_package: "parquetjs"
  npm_weekly_downloads: 170660
---

# Parquet Schema Extractor for S3

This skill uses boto3 to list objects in an S3 prefix and downloads Parquet file footers using range requests (GetObject with Range header) to avoid full file downloads. PyArrow is used to parse the Parquet metadata footer and extract the schema including field names, data types, and nullable flags. The skill compares schemas across partition directories by hashing schema fingerprints and flagging deviations. Type compatibility checks follow Arrow type promotion rules to identify breaking changes (e.g., INT32 to STRING conversions). Schema history is optionally stored in an AWS DynamoDB table for drift tracking across daily pipeline runs. Output includes a Markdown schema diff report with the exact partition paths containing incompatible schemas and recommended schema evolution strategies for Apache Iceberg or Delta Lake tables.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/parquet-schema-extractor-for-s3/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/parquet-schema-extractor-for-s3
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/parquet-schema-extractor-for-s3`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parquet-schema-extractor-for-s3/)
