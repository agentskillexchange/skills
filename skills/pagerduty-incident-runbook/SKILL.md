---
title: "PagerDuty Incident Runbook"
description: "Responds to PagerDuty incidents via the PagerDuty Events API v2 and REST API. Automatically executes diagnostic runbooks based on service and alert routing keys, and posts resolution notes back to the incident timeline."
verification: security_reviewed
source: "https://github.com/PagerDuty/pdjs"
category:
  - "Runbooks & Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "pagerduty/pdjs"
  github_stars: 69
---

# PagerDuty Incident Runbook

The PagerDuty Incident Runbook agent integrates with PagerDuty via the Events API v2 and REST API (/incidents, /services, /escalation_policies) to automate incident response workflows. When triggered by a PagerDuty webhook, it identifies the affected service and matches it to a pre-configured diagnostic runbook.

The agent executes runbook steps sequentially: gathering system metrics, checking service health endpoints, querying log aggregation APIs (Elasticsearch, Datadog), and running connectivity tests. Each step’s output is captured and posted as a timeline note on the PagerDuty incident via POST /incidents/{id}/notes.

For known failure patterns, the agent can escalate to automated remediation: restarting services via SSH, scaling infrastructure through cloud provider APIs, or toggling feature flags. It respects escalation policies and notifies on-call engineers when automated remediation fails. Supports custom severity mappings, maintenance window awareness, and integration with Statuspage for public communication during outages.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/pagerduty-incident-runbook
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/pagerduty-incident-runbook` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-runbook/)
