---
title: "Salesforce Bulk API Data Loader"
description: "Performs high-volume data operations using the Salesforce Bulk API 2.0. Creates ingest jobs with createJob(), uploads CSV batches, and monitors job status via getJobInfo() for millions of records."
slug: "salesforce-bulk-api-data-loader"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/salesforce-bulk-api-data-loader/"
---

# Salesforce Bulk API Data Loader

Performs high-volume data operations using the Salesforce Bulk API 2.0. Creates ingest jobs with createJob(), uploads CSV batches, and monitors job status via getJobInfo() for millions of records.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install salesforce-bulk-api-data-loader
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Salesforce Bulk API Data Loader handles large-scale data migration and synchronization using Salesforce’s Bulk API 2.0. It creates ingest and query jobs for operations on millions of records with automatic batching and retry logic.
The skill uses jsforce to authenticate via OAuth 2.0 JWT Bearer flow, then creates bulk jobs with connection.bulk2.createJob() specifying object, operation (insert/update/upsert/delete), and external ID fields. CSV data is uploaded in chunks respecting the 150MB per job limit.
Real-time job monitoring via getJobInfo() tracks records processed, failed, and remaining. The agent automatically retrieves failed records from getFailedResults() and generates error reports with field-level validation details. Supports both serial and parallel processing modes, with serial mode for dependent record hierarchies. Includes SOQL query jobs for bulk data extraction with locator-based pagination.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/salesforce-bulk-api-data-loader/)
