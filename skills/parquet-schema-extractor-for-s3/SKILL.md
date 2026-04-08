---
title: Parquet Schema Extractor for S3
description: This skill uses boto3 to list objects in an S3 prefix and downloads Parquet
  file footers using range requests (GetObject with Range header) to avoid full file
  downloads. PyArrow is used to parse the Parquet metadata footer and extract the
  schema including field names, data types, and nullable flags. The skill compares
  schemas across partition directories by hashing schema fingerprints and flagging
  deviations. Type compatibility checks follow Arrow type promotion rules to identify
  breaking changes (e.g., INT32 to STRING conversions). Schema history is optionally
  stored in an AWS DynamoDB table for drift tracking across daily pipeline runs. Output
  includes a Markdown schema diff report with the exact partition paths containing
  incompatible schemas and recommended schema evolution strategies for Apache Iceberg
  or Delta Lake tables.
verification: security_reviewed
source: https://agentskillexchange.com/skills/parquet-schema-extractor-for-s3/
category:
- Data Extraction &amp; Transformation
framework:
- Gemini
---

# Parquet Schema Extractor for S3

This skill uses boto3 to list objects in an S3 prefix and downloads Parquet file footers using range requests (GetObject with Range header) to avoid full file downloads. PyArrow is used to parse the Parquet metadata footer and extract the schema including field names, data types, and nullable flags. The skill compares schemas across partition directories by hashing schema fingerprints and flagging deviations. Type compatibility checks follow Arrow type promotion rules to identify breaking changes (e.g., INT32 to STRING conversions). Schema history is optionally stored in an AWS DynamoDB table for drift tracking across daily pipeline runs. Output includes a Markdown schema diff report with the exact partition paths containing incompatible schemas and recommended schema evolution strategies for Apache Iceberg or Delta Lake tables.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parquet-schema-extractor-for-s3/)
