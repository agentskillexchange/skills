---
name: "Salesforce CRM Sync Agent"
description: "Bidirectional Salesforce integration using jsforce library and the Salesforce REST API. Performs SOQL queries via connection.query(), bulk upserts through connection.sobject().upsertBulk(), and subscribes to Platform Events using connection.streaming.topic() for real-time data sync."
category: "Integrations & Connectors"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/salesforce-crm-sync-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "salesforce"  # from ase_tool_match
  github_stars: 1452  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 804753  # from ase_npm_downloads
  github_repo: "jsforce/jsforce"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Salesforce CRM Sync Agent

Bidirectional Salesforce integration using jsforce library and the Salesforce REST API. Performs SOQL queries via connection.query(), bulk upserts through connection.sobject().upsertBulk(), and subscribes to Platform Events using connection.streaming.topic() for real-time data sync.

## Overview

The Salesforce CRM Sync Agent provides deep bidirectional integration with Salesforce using the jsforce library. It supports OAuth 2.0 authentication flows including JWT Bearer for server-to-server and Web Server flow for user-delegated access.

Data querying leverages SOQL through connection.query() with automatic pagination via queryMore(). The agent supports complex queries across standard objects (Account, Contact, Opportunity, Lead, Case) and custom objects, including relationship queries and aggregate functions. SOSL search is available for cross-object full-text search.

For data synchronization, the skill uses connection.sobject().create(), update(), and upsert() for single-record operations, and bulk API v2 via connection.bulk2 for high-volume operations supporting CSV and JSON formats. Bulk jobs handle insert, update, upsert, and delete operations with configurable batch sizes and concurrency limits.

Real-time event processing uses Salesforce Platform Events and Change Data Capture. The agent subscribes via connection.streaming.topic() using CometD protocol, processing events like AccountChangeEvent and custom__e events for instant sync. Additional features include metadata API access for schema introspection, Apex REST callout invocation, and Salesforce Files API for document attachment management.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill salesforce-crm-sync-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill salesforce-crm-sync-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill salesforce-crm-sync-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill salesforce-crm-sync-agent -a codex
```

### OpenClaw

```bash
clawhub install salesforce-crm-sync-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/salesforce-crm-sync-agent/
