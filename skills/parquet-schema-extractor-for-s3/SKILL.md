---
name: Parquet Schema Extractor for S3
description: Extracts and validates Parquet file schemas from Amazon S3 using the PyArrow library and AWS S3 SDK (boto3). Compares schemas across multiple partitions to detect schema drift and incompatible type ch
category: Data Extraction & Transformation
framework: Gemini
verification: security_reviewed
rating: 4.9
reviews: 52
source: https://agentskillexchange.com/skill/parquet-schema-extractor-for-s3/
---

# Parquet Schema Extractor for S3

Extracts and validates Parquet file schemas from Amazon S3 using the PyArrow library and AWS S3 SDK (boto3). Compares schemas across multiple partitions to detect schema drift and incompatible type changes. Outputs a schema diff report with partition paths and affected column details.

## Overview

This skill uses boto3 to list objects in an S3 prefix and downloads Parquet file footers using range requests (GetObject with Range header) to avoid full file downloads. PyArrow is used to parse the Parquet metadata footer and extract the schema including field names, data types, and nullable flags. The skill compares schemas across partition directories by hashing schema fingerprints and flagging deviations. Type compatibility checks follow Arrow type promotion rules to identify breaking changes (e.g., INT32 to STRING conversions). Schema history is optionally stored in an AWS DynamoDB table for drift tracking across daily pipeline runs. Output includes a Markdown schema diff report with the exact partition paths containing incompatible schemas and recommended schema evolution strategies for Apache Iceberg or Delta Lake tables.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill parquet-schema-extractor-for-s3
```

### OpenClaw

```bash
openclaw install parquet-schema-extractor-for-s3
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | Data Extraction & Transformation |
| Framework | Gemini |
| Verification | Security Reviewed |
| Rating | ⭐⭐⭐⭐ 4.9/5.0 (52 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/parquet-schema-extractor-for-s3/)*
