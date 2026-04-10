---
title: "PagerDuty Incident Runbook"
description: "Responds to PagerDuty incidents via the PagerDuty Events API v2 and REST API. Automatically executes diagnostic runbooks based on service and alert routing keys, and posts resolution notes back to the incident timeline."
slug: "pagerduty-incident-runbook"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/pagerduty-incident-runbook/"
---

# PagerDuty Incident Runbook

Responds to PagerDuty incidents via the PagerDuty Events API v2 and REST API. Automatically executes diagnostic runbooks based on service and alert routing keys, and posts resolution notes back to the incident timeline.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install pagerduty-incident-runbook
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The PagerDuty Incident Runbook agent integrates with PagerDuty via the Events API v2 and REST API (/incidents, /services, /escalation_policies) to automate incident response workflows. When triggered by a PagerDuty webhook, it identifies the affected service and matches it to a pre-configured diagnostic runbook.
The agent executes runbook steps sequentially: gathering system metrics, checking service health endpoints, querying log aggregation APIs (Elasticsearch, Datadog), and running connectivity tests. Each step’s output is captured and posted as a timeline note on the PagerDuty incident via POST /incidents/{id}/notes.
For known failure patterns, the agent can escalate to automated remediation: restarting services via SSH, scaling infrastructure through cloud provider APIs, or toggling feature flags. It respects escalation policies and notifies on-call engineers when automated remediation fails. Supports custom severity mappings, maintenance window awareness, and integration with Statuspage for public communication during outages.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-runbook/)
