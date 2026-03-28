---
name: "PagerDuty Incident Runbook"
description: "Responds to PagerDuty incidents via the PagerDuty Events API v2 and REST API. Automatically executes diagnostic runbooks based on service and alert routing keys, and posts resolution notes back to the incident timeline."
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

# PagerDuty Incident Runbook

Responds to PagerDuty incidents via the PagerDuty Events API v2 and REST API. Automatically executes diagnostic runbooks based on service and alert routing keys, and posts resolution notes back to the incident timeline.

## Overview

The PagerDuty Incident Runbook agent integrates with PagerDuty via the Events API v2 and REST API (/incidents, /services, /escalation_policies) to automate incident response workflows. When triggered by a PagerDuty webhook, it identifies the affected service and matches it to a pre-configured diagnostic runbook.

The agent executes runbook steps sequentially: gathering system metrics, checking service health endpoints, querying log aggregation APIs (Elasticsearch, Datadog), and running connectivity tests. Each step’s output is captured and posted as a timeline note on the PagerDuty incident via POST /incidents/{id}/notes.

For known failure patterns, the agent can escalate to automated remediation: restarting services via SSH, scaling infrastructure through cloud provider APIs, or toggling feature flags. It respects escalation policies and notifies on-call engineers when automated remediation fails. Supports custom severity mappings, maintenance window awareness, and integration with Statuspage for public communication during outages.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-runbook
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-runbook -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-runbook -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-runbook -a codex
```

### OpenClaw

```bash
clawhub install pagerduty-incident-runbook
```

## Source

- Marketplace: https://agentskillexchange.com/skills/pagerduty-incident-runbook/
