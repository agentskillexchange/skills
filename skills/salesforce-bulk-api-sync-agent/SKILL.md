---
title: "Salesforce Bulk API Sync Agent"
description: "Perform high-volume data synchronization with Salesforce using the Bulk API 2.0 for CSV-based upsert, delete, and query operations. Handles OAuth 2.0 JWT bearer flow authentication via jsforce."
verification: security_reviewed
source: "https://github.com/jsforce/jsforce"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "jsforce/jsforce"
  github_stars: 1453
  npm_package: "jsforce"
  npm_weekly_downloads: 936641
---

# Salesforce Bulk API Sync Agent

Synchronize large datasets with Salesforce CRM using the Bulk API 2.0 endpoint optimized for operations exceeding 2,000 records. This skill manages the complete bulk job lifecycle from creation through monitoring to result retrieval.

Authentication uses the OAuth 2.0 JWT bearer flow with a connected app certificate for server-to-server integration without user interaction. The jsforce library provides the JavaScript interface for all Salesforce API operations.

Bulk operations support CSV-based ingest for insert, update, upsert, and delete operations on any standard or custom Salesforce object. Jobs are created via POST /services/data/vXX.0/jobs/ingest with configurable batch sizes and column delimiter settings.

The skill monitors job progress by polling the job status endpoint, handles partial failures by parsing the failed results CSV, and automatically retries failed records with exponential backoff. Query operations use Bulk API 2.0 query jobs for extracting large result sets with automatic locator-based pagination.

Field mapping configuration supports transformation rules for data type conversion, default values, and external ID matching for upsert operations.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/salesforce-bulk-api-sync-agent/)
