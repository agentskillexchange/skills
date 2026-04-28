---
title: Salesforce CRM Sync Agent
description: Bidirectional Salesforce integration using jsforce library and the Salesforce
  REST API. Performs SOQL queries via connection.query(), bulk upserts through connection.sobject().upsertBulk(),
  and subscribes to Platform Events using connection.streaming.topic() for real-time
  data sync.
verification: security_reviewed
source: https://github.com/jsforce/jsforce
category:
- Integrations & Connectors
framework:
- Cursor
tool_ecosystem:
  github_repo: jsforce/jsforce
  github_stars: 1453
  npm_package: jsforce
  npm_weekly_downloads: 936641
---

# Salesforce CRM Sync Agent

Bidirectional Salesforce integration using jsforce library and the Salesforce REST API. Performs SOQL queries via connection.query(), bulk upserts through connection.sobject().upsertBulk(), and subscribes to Platform Events using connection.streaming.topic() for real-time data sync.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/salesforce-crm-sync-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/salesforce-crm-sync-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/salesforce-crm-sync-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/salesforce-crm-sync-agent/)
