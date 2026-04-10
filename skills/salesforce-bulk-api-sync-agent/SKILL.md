---
title: "Salesforce Bulk API Sync Agent"
description: "Perform high-volume data synchronization with Salesforce using the Bulk API 2.0 for CSV-based upsert, delete, and query operations. Handles OAuth 2.0 JWT bearer flow authentication via jsforce."
slug: "salesforce-bulk-api-sync-agent"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/salesforce-bulk-api-sync-agent/"
---

# Salesforce Bulk API Sync Agent

Perform high-volume data synchronization with Salesforce using the Bulk API 2.0 for CSV-based upsert, delete, and query operations. Handles OAuth 2.0 JWT bearer flow authentication via jsforce.

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
clawhub install salesforce-bulk-api-sync-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Synchronize large datasets with Salesforce CRM using the Bulk API 2.0 endpoint optimized for operations exceeding 2,000 records. This skill manages the complete bulk job lifecycle from creation through monitoring to result retrieval.
Authentication uses the OAuth 2.0 JWT bearer flow with a connected app certificate for server-to-server integration without user interaction. The jsforce library provides the JavaScript interface for all Salesforce API operations.
Bulk operations support CSV-based ingest for insert, update, upsert, and delete operations on any standard or custom Salesforce object. Jobs are created via POST /services/data/vXX.0/jobs/ingest with configurable batch sizes and column delimiter settings.
The skill monitors job progress by polling the job status endpoint, handles partial failures by parsing the failed results CSV, and automatically retries failed records with exponential backoff. Query operations use Bulk API 2.0 query jobs for extracting large result sets with automatic locator-based pagination.
Field mapping configuration supports transformation rules for data type conversion, default values, and external ID matching for upsert operations.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/salesforce-bulk-api-sync-agent/)
