---
title: Salesforce Bulk API Sync Agent
description: Synchronize large datasets with Salesforce CRM using the Bulk API 2.0
  endpoint optimized for operations exceeding 2,000 records. This skill manages the
  complete bulk job lifecycle from creation through monitoring to result retrieval.
  Authentication uses the OAuth 2.0 JWT bearer flow with a connected app certificate
  for server-to-server integration without user interaction. The jsforce library provides
  the JavaScript interface for all Salesforce API operations. Bulk operations support
  CSV-based ingest for insert, update, upsert, and delete operations on any standard
  or custom Salesforce object. Jobs are created via POST /services/data/vXX.0/jobs/ingest
  with configurable batch sizes and column delimiter settings. The skill monitors
  job progress by polling the job status endpoint, handles partial failures by parsing
  the failed results CSV, and automatically retries failed records with exponential
  backoff. Query operations use Bulk API 2.0 query jobs for extracting large result
  sets with automatic locator-based pagination. Field mapping configuration supports
  transformation rules for data type conversion, default values, and external ID matching
  for upsert operations.
verification: security_reviewed
source: https://agentskillexchange.com/skills/salesforce-bulk-api-sync-agent/
category:
- Integrations &amp; Connectors
framework:
- Codex
---

# Salesforce Bulk API Sync Agent

Synchronize large datasets with Salesforce CRM using the Bulk API 2.0 endpoint optimized for operations exceeding 2,000 records. This skill manages the complete bulk job lifecycle from creation through monitoring to result retrieval. Authentication uses the OAuth 2.0 JWT bearer flow with a connected app certificate for server-to-server integration without user interaction. The jsforce library provides the JavaScript interface for all Salesforce API operations. Bulk operations support CSV-based ingest for insert, update, upsert, and delete operations on any standard or custom Salesforce object. Jobs are created via POST /services/data/vXX.0/jobs/ingest with configurable batch sizes and column delimiter settings. The skill monitors job progress by polling the job status endpoint, handles partial failures by parsing the failed results CSV, and automatically retries failed records with exponential backoff. Query operations use Bulk API 2.0 query jobs for extracting large result sets with automatic locator-based pagination. Field mapping configuration supports transformation rules for data type conversion, default values, and external ID matching for upsert operations.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/salesforce-bulk-api-sync-agent/)
