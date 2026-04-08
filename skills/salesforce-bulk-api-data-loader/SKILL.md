---
title: Salesforce Bulk API Data Loader
description: The Salesforce Bulk API Data Loader handles large-scale data migration
  and synchronization using Salesforce’s Bulk API 2.0. It creates ingest and query
  jobs for operations on millions of records with automatic batching and retry logic.
  The skill uses jsforce to authenticate via OAuth 2.0 JWT Bearer flow, then creates
  bulk jobs with connection.bulk2.createJob() specifying object, operation (insert/update/upsert/delete),
  and external ID fields. CSV data is uploaded in chunks respecting the 150MB per
  job limit. Real-time job monitoring via getJobInfo() tracks records processed, failed,
  and remaining. The agent automatically retrieves failed records from getFailedResults()
  and generates error reports with field-level validation details. Supports both serial
  and parallel processing modes, with serial mode for dependent record hierarchies.
  Includes SOQL query jobs for bulk data extraction with locator-based pagination.
verification: security_reviewed
source: https://agentskillexchange.com/skills/salesforce-bulk-api-data-loader/
category:
- Data Extraction &amp; Transformation
framework:
- Claude Code
---

# Salesforce Bulk API Data Loader

The Salesforce Bulk API Data Loader handles large-scale data migration and synchronization using Salesforce’s Bulk API 2.0. It creates ingest and query jobs for operations on millions of records with automatic batching and retry logic. The skill uses jsforce to authenticate via OAuth 2.0 JWT Bearer flow, then creates bulk jobs with connection.bulk2.createJob() specifying object, operation (insert/update/upsert/delete), and external ID fields. CSV data is uploaded in chunks respecting the 150MB per job limit. Real-time job monitoring via getJobInfo() tracks records processed, failed, and remaining. The agent automatically retrieves failed records from getFailedResults() and generates error reports with field-level validation details. Supports both serial and parallel processing modes, with serial mode for dependent record hierarchies. Includes SOQL query jobs for bulk data extraction with locator-based pagination.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/salesforce-bulk-api-data-loader/)
