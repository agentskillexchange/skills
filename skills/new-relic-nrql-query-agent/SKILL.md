---
title: "New Relic NRQL Query Agent"
description: "Executes NRQL queries against New Relic’s GraphQL NerdGraph API for application performance monitoring. Generates automated SLA reports with percentile latency breakdowns and error budget calculations."
verification: "security_reviewed"
source: "https://docs.newrelic.com/docs/nrql/get-started/introduction-nrql-new-relics-query-language/"
category:
  - "Monitoring & Alerts"
framework:
  - "Custom Agents"
---

# New Relic NRQL Query Agent

The New Relic NRQL Query Agent skill connects to New Relic’s NerdGraph GraphQL API to execute NRQL (New Relic Query Language) queries for application performance analysis. It handles authentication via User API keys, supports cross-account querying, and manages query pagination for large result sets.

The skill provides pre-built NRQL templates for common APM scenarios including transaction percentile analysis (P50/P95/P99), error rate trending with TIMESERIES faceting, and Apdex score monitoring. Custom queries support all NRQL clauses including FACET, SINCE, UNTIL, COMPARE WITH, and subqueries.

Automated SLA reporting generates PDF documents using Puppeteer with embedded charts rendered via Chart.js. Reports include latency percentile breakdowns, throughput trends, error categorization by type and transaction, and error budget burn-down calculations based on configurable SLO targets. The skill can schedule recurring reports via cron and deliver them through email using SendGrid or to Slack channels via the Slack Web API.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/new-relic-nrql-query-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/new-relic-nrql-query-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/new-relic-nrql-query-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/new-relic-nrql-query-agent/)
