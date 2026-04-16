---
title: "Salesforce CRM Sync Agent"
description: "Bidirectional Salesforce integration using jsforce library and the Salesforce REST API. Performs SOQL queries via connection.query(), bulk upserts through connection.sobject().upsertBulk(), and subscribes to Platform Events using connection.streaming.topic() for real-time data sync."
verification: "security_reviewed"
source: "https://github.com/jsforce/jsforce"
category:
  - "Integrations & Connectors"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "jsforce/jsforce"
  github_stars: 1453
  ase_npm_package: "jsforce"
  npm_weekly_downloads: 936641
  license: "MIT"
---

# Salesforce CRM Sync Agent

The Salesforce CRM Sync Agent provides deep bidirectional integration with Salesforce using the jsforce library. It supports OAuth 2.0 authentication flows including JWT Bearer for server-to-server and Web Server flow for user-delegated access.


Data querying leverages SOQL through connection.query() with automatic pagination via queryMore(). The agent supports complex queries across standard objects (Account, Contact, Opportunity, Lead, Case) and custom objects, including relationship queries and aggregate functions. SOSL search is available for cross-object full-text search.


For data synchronization, the skill uses connection.sobject().create(), update(), and upsert() for single-record operations, and bulk API v2 via connection.bulk2 for high-volume operations supporting CSV and JSON formats. Bulk jobs handle insert, update, upsert, and delete operations with configurable batch sizes and concurrency limits.


Real-time event processing uses Salesforce Platform Events and Change Data Capture. The agent subscribes via connection.streaming.topic() using CometD protocol, processing events like AccountChangeEvent and custom__e events for instant sync. Additional features include metadata API access for schema introspection, Apex REST callout invocation, and Salesforce Files API for document attachment management.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/salesforce-crm-sync-agent/)
