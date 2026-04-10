---
title: "PagerDuty Incident Runbook Executor"
description: "Automatically executes diagnostic runbooks when PagerDuty incidents trigger, using the PagerDuty Events v2 API and Rundeck API. Attaches diagnostic output as incident notes and suggests remediation actions."
slug: "pagerduty-incident-runbook-executor"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/pagerduty-incident-runbook-executor/"
listed: true
---

# PagerDuty Incident Runbook Executor

Automatically executes diagnostic runbooks when PagerDuty incidents trigger, using the PagerDuty Events v2 API and Rundeck API. Attaches diagnostic output as incident notes and suggests remediation actions.

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
clawhub install pagerduty-incident-runbook-executor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The PagerDuty Incident Runbook Executor skill bridges alerting and automated diagnostics by connecting PagerDuty incidents to executable runbooks. When an incident triggers via the PagerDuty Events v2 API webhook, the skill matches the incident service and urgency to appropriate diagnostic runbooks stored in Rundeck. It executes targeted diagnostic jobs through the Rundeck API, capturing command outputs, log snippets, and metric snapshots. Results are formatted as structured incident notes and posted back to PagerDuty via the Incidents API. The skill supports conditional runbook chaining — if initial diagnostics indicate a specific failure mode, follow-up runbooks execute automatically. Includes escalation logic that pages additional responders when diagnostics reveal critical issues. Generates post-incident summaries with timeline reconstruction and root cause suggestions. Supports custom runbooks defined in YAML with parameterized steps and approval gates for destructive actions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-runbook-executor/)
