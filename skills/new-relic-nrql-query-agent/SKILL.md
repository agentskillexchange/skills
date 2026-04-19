---
title: "New Relic NRQL Query Agent"
description: "The New Relic NRQL Query Agent skill connects to New Relic&#8217;s NerdGraph GraphQL API to execute NRQL (New Relic Query Language) queries for application performance analysis. It handles authentication via User API keys, supports cross-account querying, and manages query pagination for large result sets. The skill provides pre-built NRQL templates for common APM scenarios including transaction percentile analysis (P50/P95/P99), error rate trending with TIMESERIES faceting, and Apdex score monitoring. Custom queries support all NRQL clauses including FACET, SINCE, UNTIL, COMPARE WITH, and subqueries. Automated SLA reporting generates PDF documents using Puppeteer with embedded charts rendered via Chart.js. Reports include latency percentile breakdowns, throughput trends, error categorization by type and transaction, and error budget burn-down calculations based on configurable SLO targets. The skill can schedule recurring reports via cron and deliver them through email using SendGrid or to Slack channels via the Slack Web API."
source: "https://agentskillexchange.com/skills/new-relic-nrql-query-agent/"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Custom Agents"
---

# New Relic NRQL Query Agent

The New Relic NRQL Query Agent skill connects to New Relic&#8217;s NerdGraph GraphQL API to execute NRQL (New Relic Query Language) queries for application performance analysis. It handles authentication via User API keys, supports cross-account querying, and manages query pagination for large result sets. The skill provides pre-built NRQL templates for common APM scenarios including transaction percentile analysis (P50/P95/P99), error rate trending with TIMESERIES faceting, and Apdex score monitoring. Custom queries support all NRQL clauses including FACET, SINCE, UNTIL, COMPARE WITH, and subqueries. Automated SLA reporting generates PDF documents using Puppeteer with embedded charts rendered via Chart.js. Reports include latency percentile breakdowns, throughput trends, error categorization by type and transaction, and error budget burn-down calculations based on configurable SLO targets. The skill can schedule recurring reports via cron and deliver them through email using SendGrid or to Slack channels via the Slack Web API.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/new-relic-nrql-query-agent/)
