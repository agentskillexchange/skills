---
name: "Salesforce Bulk API Data Loader"
description: "Performs high-volume data operations using the Salesforce Bulk API 2.0. Creates ingest jobs with createJob(), uploads CSV batches, and monitors job status via getJobInfo() for millions of records."
category: "Data Extraction & Transformation"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/salesforce-bulk-api-data-loader/"
---
# Salesforce Bulk API Data Loader

Performs high-volume data operations using the Salesforce Bulk API 2.0. Creates ingest jobs with createJob(), uploads CSV batches, and monitors job status via getJobInfo() for millions of records.

## Overview

The Salesforce Bulk API Data Loader handles large-scale data migration and synchronization using Salesforce’s Bulk API 2.0. It creates ingest and query jobs for operations on millions of records with automatic batching and retry logic.

The skill uses `jsforce` to authenticate via OAuth 2.0 JWT Bearer flow, then creates bulk jobs with `connection.bulk2.createJob()` specifying object, operation (insert/update/upsert/delete), and external ID fields. CSV data is uploaded in chunks respecting the 150MB per job limit.

Real-time job monitoring via `getJobInfo()` tracks records processed, failed, and remaining. The agent automatically retrieves failed records from `getFailedResults()` and generates error reports with field-level validation details. Supports both serial and parallel processing modes, with serial mode for dependent record hierarchies. Includes SOQL query jobs for bulk data extraction with locator-based pagination.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill salesforce-bulk-api-data-loader
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill salesforce-bulk-api-data-loader -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill salesforce-bulk-api-data-loader -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill salesforce-bulk-api-data-loader -a codex
```

### OpenClaw

```bash
clawhub install salesforce-bulk-api-data-loader
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/salesforce-bulk-api-data-loader/)
