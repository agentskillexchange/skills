---
title: "New Relic NRQL Query Agent"
description: "Executes NRQL queries against New Relic’s GraphQL NerdGraph API for application performance monitoring. Generates automated SLA reports with percentile latency breakdowns and error budget calculations."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/new-relic-nrql-query-agent/"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Custom Agents"
---

# New Relic NRQL Query Agent

The New Relic NRQL Query Agent skill connects to New Relic’s NerdGraph GraphQL API to execute NRQL (New Relic Query Language) queries for application performance analysis. It handles authentication via User API keys, supports cross-account querying, and manages query pagination for large result sets.

The skill provides pre-built NRQL templates for common APM scenarios including transaction percentile analysis (P50/P95/P99), error rate trending with TIMESERIES faceting, and Apdex score monitoring. Custom queries support all NRQL clauses including FACET, SINCE, UNTIL, COMPARE WITH, and subqueries.

Automated SLA reporting generates PDF documents using Puppeteer with embedded charts rendered via Chart.js. Reports include latency percentile breakdowns, throughput trends, error categorization by type and transaction, and error budget burn-down calculations based on configurable SLO targets. The skill can schedule recurring reports via cron and deliver them through email using SendGrid or to Slack channels via the Slack Web API.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/new-relic-nrql-query-agent/)
