---
title: "Salesforce CRM Sync Agent"
description: "Bidirectional Salesforce integration using jsforce library and the Salesforce REST API. Performs SOQL queries via connection.query(), bulk upserts through connection.sobject().upsertBulk(), and subscribes to Platform Events using connection.streaming.topic() for real-time data sync."
verification: security_reviewed
source: "https://github.com/jsforce/jsforce"
category:
  - "Integrations & Connectors"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "jsforce/jsforce"
  github_stars: 1453
  npm_package: "jsforce"
  npm_weekly_downloads: 936641
  license: "MIT"
---

# Salesforce CRM Sync Agent

The Salesforce CRM Sync Agent provides deep bidirectional integration with Salesforce using the jsforce library. It supports OAuth 2.0 authentication flows including JWT Bearer for server-to-server and Web Server flow for user-delegated access.

Data querying leverages SOQL through connection.query() with automatic pagination via queryMore(). The agent supports complex queries across standard objects (Account, Contact, Opportunity, Lead, Case) and custom objects, including relationship queries and aggregate functions. SOSL search is available for cross-object full-text search.

For data synchronization, the skill uses connection.sobject().create(), update(), and upsert() for single-record operations, and bulk API v2 via connection.bulk2 for high-volume operations supporting CSV and JSON formats. Bulk jobs handle insert, update, upsert, and delete operations with configurable batch sizes and concurrency limits.

Real-time event processing uses Salesforce Platform Events and Change Data Capture. The agent subscribes via connection.streaming.topic() using CometD protocol, processing events like AccountChangeEvent and custom__e events for instant sync. Additional features include metadata API access for schema introspection, Apex REST callout invocation, and Salesforce Files API for document attachment management.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/salesforce-crm-sync-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/salesforce-crm-sync-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/salesforce-crm-sync-agent/)
