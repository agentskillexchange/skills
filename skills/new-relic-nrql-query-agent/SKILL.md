---
name: "New Relic NRQL Query Agent"
description: "Executes NRQL queries against New Relic’s GraphQL NerdGraph API for application performance monitoring. Generates automated SLA reports with percentile latency breakdowns and error budget calculations."
category: "Monitoring & Alerts"
framework: "Custom Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/new-relic-nrql-query-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "slack"  # from ase_tool_match
  github_stars: 2899  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 2433529  # from ase_npm_downloads
  github_repo: "slackapi/bolt-js"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# New Relic NRQL Query Agent

Executes NRQL queries against New Relic’s GraphQL NerdGraph API for application performance monitoring. Generates automated SLA reports with percentile latency breakdowns and error budget calculations.

## Overview

The New Relic NRQL Query Agent skill connects to New Relic’s NerdGraph GraphQL API to execute NRQL (New Relic Query Language) queries for application performance analysis. It handles authentication via User API keys, supports cross-account querying, and manages query pagination for large result sets.

The skill provides pre-built NRQL templates for common APM scenarios including transaction percentile analysis (P50/P95/P99), error rate trending with TIMESERIES faceting, and Apdex score monitoring. Custom queries support all NRQL clauses including FACET, SINCE, UNTIL, COMPARE WITH, and subqueries.

Automated SLA reporting generates PDF documents using Puppeteer with embedded charts rendered via Chart.js. Reports include latency percentile breakdowns, throughput trends, error categorization by type and transaction, and error budget burn-down calculations based on configurable SLO targets. The skill can schedule recurring reports via cron and deliver them through email using SendGrid or to Slack channels via the Slack Web API.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill new-relic-nrql-query-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill new-relic-nrql-query-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill new-relic-nrql-query-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill new-relic-nrql-query-agent -a codex
```

### OpenClaw

```bash
clawhub install new-relic-nrql-query-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/new-relic-nrql-query-agent/
