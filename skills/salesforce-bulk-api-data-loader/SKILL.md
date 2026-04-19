---
title: "Salesforce Bulk API Data Loader"
description: "The Salesforce Bulk API Data Loader handles large-scale data migration and synchronization using Salesforce&#8217;s Bulk API 2.0. It creates ingest and query jobs for operations on millions of records with automatic batching and retry logic. The skill uses jsforce to authenticate via OAuth 2.0 JWT Bearer flow, then creates bulk jobs with connection.bulk2.createJob() specifying object, operation (insert/update/upsert/delete), and external ID fields. CSV data is uploaded in chunks respecting the 150MB per job limit. Real-time job monitoring via getJobInfo() tracks records processed, failed, and remaining. The agent automatically retrieves failed records from getFailedResults() and generates error reports with field-level validation details. Supports both serial and parallel processing modes, with serial mode for dependent record hierarchies. Includes SOQL query jobs for bulk data extraction with locator-based pagination."
source: "https://github.com/jsforce/jsforce"
verification: "security_reviewed"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "jsforce/jsforce"
  github_stars: 1453
  npm_package: "jsforce"
  npm_weekly_downloads: 936641
---

# Salesforce Bulk API Data Loader

The Salesforce Bulk API Data Loader handles large-scale data migration and synchronization using Salesforce&#8217;s Bulk API 2.0. It creates ingest and query jobs for operations on millions of records with automatic batching and retry logic. The skill uses jsforce to authenticate via OAuth 2.0 JWT Bearer flow, then creates bulk jobs with connection.bulk2.createJob() specifying object, operation (insert/update/upsert/delete), and external ID fields. CSV data is uploaded in chunks respecting the 150MB per job limit. Real-time job monitoring via getJobInfo() tracks records processed, failed, and remaining. The agent automatically retrieves failed records from getFailedResults() and generates error reports with field-level validation details. Supports both serial and parallel processing modes, with serial mode for dependent record hierarchies. Includes SOQL query jobs for bulk data extraction with locator-based pagination.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/salesforce-bulk-api-data-loader/)
