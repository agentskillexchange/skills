---
name: "Salesforce Bulk API Data Loader"
description: "Performs high-volume data operations using the Salesforce Bulk API 2.0. Creates ingest jobs with createJob(), uploads CSV batches, and monitors job status via getJobInfo() for millions of records."
category: "Data Extraction & Transformation"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/salesforce-bulk-api-data-loader/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "salesforce"  # from ase_tool_match
  github_stars: 1452  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 804753  # from ase_npm_downloads
  github_repo: "jsforce/jsforce"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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

- Marketplace: https://agentskillexchange.com/skills/salesforce-bulk-api-data-loader/
