---
title: "PagerDuty Incident Runbook Executor"
description: "The PagerDuty Incident Runbook Executor skill bridges alerting and automated diagnostics by connecting PagerDuty incidents to executable runbooks. When an incident triggers via the PagerDuty Events v2 API webhook, the skill matches the incident service and urgency to appropriate diagnostic runbooks stored in Rundeck. It executes targeted diagnostic jobs through the Rundeck API, capturing command outputs, log snippets, and metric snapshots. Results are formatted as structured incident notes and posted back to PagerDuty via the Incidents API. The skill supports conditional runbook chaining — if initial diagnostics indicate a specific failure mode, follow-up runbooks execute automatically. Includes escalation logic that pages additional responders when diagnostics reveal critical issues. Generates post-incident summaries with timeline reconstruction and root cause suggestions. Supports custom runbooks defined in YAML with parameterized steps and approval gates for destructive actions."
verification: security_reviewed
source: "https://github.com/PagerDuty/pdjs"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "pagerduty/pdjs"
  github_stars: 69
---

# PagerDuty Incident Runbook Executor

The PagerDuty Incident Runbook Executor skill bridges alerting and automated diagnostics by connecting PagerDuty incidents to executable runbooks. When an incident triggers via the PagerDuty Events v2 API webhook, the skill matches the incident service and urgency to appropriate diagnostic runbooks stored in Rundeck. It executes targeted diagnostic jobs through the Rundeck API, capturing command outputs, log snippets, and metric snapshots. Results are formatted as structured incident notes and posted back to PagerDuty via the Incidents API. The skill supports conditional runbook chaining — if initial diagnostics indicate a specific failure mode, follow-up runbooks execute automatically. Includes escalation logic that pages additional responders when diagnostics reveal critical issues. Generates post-incident summaries with timeline reconstruction and root cause suggestions. Supports custom runbooks defined in YAML with parameterized steps and approval gates for destructive actions.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/pagerduty-incident-runbook-executor
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/pagerduty-incident-runbook-executor` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-runbook-executor/)
