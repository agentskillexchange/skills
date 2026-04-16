---
title: "Salesforce Bulk API Data Loader"
description: "Performs high-volume data operations using the Salesforce Bulk API 2.0. Creates ingest jobs with createJob(), uploads CSV batches, and monitors job status via getJobInfo() for millions of records."
verification: "security_reviewed"
source: "https://github.com/jsforce/jsforce"
category:
  - "Data Extraction & Transformation"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "jsforce/jsforce"
  github_stars: 1453
  ase_npm_package: "jsforce"
  npm_weekly_downloads: 936641
  license: "MIT"
---

# Salesforce Bulk API Data Loader

The Salesforce Bulk API Data Loader handles large-scale data migration and synchronization using Salesforce’s Bulk API 2.0. It creates ingest and query jobs for operations on millions of records with automatic batching and retry logic.


The skill uses jsforce to authenticate via OAuth 2.0 JWT Bearer flow, then creates bulk jobs with connection.bulk2.createJob() specifying object, operation (insert/update/upsert/delete), and external ID fields. CSV data is uploaded in chunks respecting the 150MB per job limit.


Real-time job monitoring via getJobInfo() tracks records processed, failed, and remaining. The agent automatically retrieves failed records from getFailedResults() and generates error reports with field-level validation details. Supports both serial and parallel processing modes, with serial mode for dependent record hierarchies. Includes SOQL query jobs for bulk data extraction with locator-based pagination.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/salesforce-bulk-api-data-loader/)
