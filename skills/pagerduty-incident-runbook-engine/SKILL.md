---
name: "PagerDuty Incident Runbook Engine"
description: "Generates automated incident response runbooks triggered by PagerDuty webhooks via the PagerDuty Events API v2. Integrates with Datadog API and AWS CloudWatch for diagnostic data collection during incidents."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: security_reviewed
source: "https://github.com/PagerDuty/pdjs"
tool_ecosystem:
  tool: pagerduty
  github_stars: 69
  npm_weekly_downloads: 210829
  github_repo: PagerDuty/pdjs
  license: Apache-2.0
  maintained: false
---

# PagerDuty Incident Runbook Engine

Generates automated incident response runbooks triggered by PagerDuty webhooks via the PagerDuty Events API v2. Integrates with Datadog API and AWS CloudWatch for diagnostic data collection during incidents.

## Overview

The PagerDuty Incident Runbook Engine creates automated diagnostic workflows triggered by PagerDuty incident events. It processes PagerDuty webhook payloads via the Events API v2, extracts alert metadata, and executes diagnostic runbook steps based on the triggering service and severity level.

The skill integrates with the Datadog API to fetch relevant metric snapshots, log patterns, and APM traces during incident triage. It queries AWS CloudWatch using the AWS SDK for recent alarm state changes, ECS task status, and RDS performance insights related to the incident scope.

Runbook templates are parameterized with service-specific diagnostic commands including kubectl cluster status checks, database connection pool metrics via pg_stat_activity, Redis memory analysis through redis-cli info, and Elasticsearch cluster health queries. The engine generates structured incident timelines with correlated metrics, creates Confluence pages via the Atlassian REST API for post-incident documentation, and updates PagerDuty incident notes with diagnostic findings through the PagerDuty REST API.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-runbook-engine
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-runbook-engine -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-runbook-engine -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-runbook-engine -a codex
```

### OpenClaw

```bash
clawhub install pagerduty-incident-runbook-engine
```

## Source

- Marketplace: https://agentskillexchange.com/skills/pagerduty-incident-runbook-engine/
