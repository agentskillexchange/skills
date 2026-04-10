---
name: New Relic NRQL Query Agent
description: Executes NRQL queries against New Relic&#8217;s GraphQL NerdGraph API
  for application performance monitoring. Generates automated SLA reports with percentile
  latency breakdowns and error budget calculations.
verification: security_reviewed
source: https://agentskillexchange.com/skills/new-relic-nrql-query-agent/
category:
- Monitoring &amp; Alerts
framework:
- Custom Agents
---
# New Relic NRQL Query Agent

The New Relic NRQL Query Agent skill connects to New Relic's NerdGraph GraphQL API to execute NRQL (New Relic Query Language) queries for application performance analysis. It handles authentication via User API keys, supports cross-account querying, and manages query pagination for large result sets.
The skill provides pre-built NRQL templates for common APM scenarios including transaction percentile analysis (P50/P95/P99), error rate trending with TIMESERIES faceting, and Apdex score monitoring. Custom queries support all NRQL clauses including FACET, SINCE, UNTIL, COMPARE WITH, and subqueries.
Automated SLA reporting generates PDF documents using Puppeteer with embedded charts rendered via Chart.js. Reports include latency percentile breakdowns, throughput trends, error categorization by type and transaction, and error budget burn-down calculations based on configurable SLO targets. The skill can schedule recurring reports via cron and deliver them through email using SendGrid or to Slack channels via the Slack Web API.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/new-relic-nrql-query-agent/)
