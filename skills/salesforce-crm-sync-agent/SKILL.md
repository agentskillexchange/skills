---
title: Salesforce CRM Sync Agent
description: The Salesforce CRM Sync Agent provides deep bidirectional integration
  with Salesforce using the jsforce library. It supports OAuth 2.0 authentication
  flows including JWT Bearer for server-to-server and Web Server flow for user-delegated
  access. Data querying leverages SOQL through connection.query() with automatic pagination
  via queryMore(). The agent supports complex queries across standard objects (Account,
  Contact, Opportunity, Lead, Case) and custom objects, including relationship queries
  and aggregate functions. SOSL search is available for cross-object full-text search.
  For data synchronization, the skill uses connection.sobject().create(), update(),
  and upsert() for single-record operations, and bulk API v2 via connection.bulk2
  for high-volume operations supporting CSV and JSON formats. Bulk jobs handle insert,
  update, upsert, and delete operations with configurable batch sizes and concurrency
  limits. Real-time event processing uses Salesforce Platform Events and Change Data
  Capture. The agent subscribes via connection.streaming.topic() using CometD protocol,
  processing events like AccountChangeEvent and custom__e events for instant sync.
  Additional features include metadata API access for schema introspection, Apex REST
  callout invocation, and Salesforce Files API for document attachment management.
verification: security_reviewed
source: https://agentskillexchange.com/skills/salesforce-crm-sync-agent/
category:
- Integrations &amp; Connectors
framework:
- Cursor
---

# Salesforce CRM Sync Agent

The Salesforce CRM Sync Agent provides deep bidirectional integration with Salesforce using the jsforce library. It supports OAuth 2.0 authentication flows including JWT Bearer for server-to-server and Web Server flow for user-delegated access. Data querying leverages SOQL through connection.query() with automatic pagination via queryMore(). The agent supports complex queries across standard objects (Account, Contact, Opportunity, Lead, Case) and custom objects, including relationship queries and aggregate functions. SOSL search is available for cross-object full-text search. For data synchronization, the skill uses connection.sobject().create(), update(), and upsert() for single-record operations, and bulk API v2 via connection.bulk2 for high-volume operations supporting CSV and JSON formats. Bulk jobs handle insert, update, upsert, and delete operations with configurable batch sizes and concurrency limits. Real-time event processing uses Salesforce Platform Events and Change Data Capture. The agent subscribes via connection.streaming.topic() using CometD protocol, processing events like AccountChangeEvent and custom__e events for instant sync. Additional features include metadata API access for schema introspection, Apex REST callout invocation, and Salesforce Files API for document attachment management.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/salesforce-crm-sync-agent/)
