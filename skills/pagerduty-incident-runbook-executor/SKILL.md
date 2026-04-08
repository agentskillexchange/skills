---
title: PagerDuty Incident Runbook Executor
description: The PagerDuty Incident Runbook Executor skill bridges alerting and automated
  diagnostics by connecting PagerDuty incidents to executable runbooks. When an incident
  triggers via the PagerDuty Events v2 API webhook, the skill matches the incident
  service and urgency to appropriate diagnostic runbooks stored in Rundeck. It executes
  targeted diagnostic jobs through the Rundeck API, capturing command outputs, log
  snippets, and metric snapshots. Results are formatted as structured incident notes
  and posted back to PagerDuty via the Incidents API. The skill supports conditional
  runbook chaining — if initial diagnostics indicate a specific failure mode, follow-up
  runbooks execute automatically. Includes escalation logic that pages additional
  responders when diagnostics reveal critical issues. Generates post-incident summaries
  with timeline reconstruction and root cause suggestions. Supports custom runbooks
  defined in YAML with parameterized steps and approval gates for destructive actions.
verification: security_reviewed
source: https://agentskillexchange.com/skills/pagerduty-incident-runbook-executor/
category:
- Runbooks &amp; Diagnostics
framework:
- OpenClaw
---

# PagerDuty Incident Runbook Executor

The PagerDuty Incident Runbook Executor skill bridges alerting and automated diagnostics by connecting PagerDuty incidents to executable runbooks. When an incident triggers via the PagerDuty Events v2 API webhook, the skill matches the incident service and urgency to appropriate diagnostic runbooks stored in Rundeck. It executes targeted diagnostic jobs through the Rundeck API, capturing command outputs, log snippets, and metric snapshots. Results are formatted as structured incident notes and posted back to PagerDuty via the Incidents API. The skill supports conditional runbook chaining — if initial diagnostics indicate a specific failure mode, follow-up runbooks execute automatically. Includes escalation logic that pages additional responders when diagnostics reveal critical issues. Generates post-incident summaries with timeline reconstruction and root cause suggestions. Supports custom runbooks defined in YAML with parameterized steps and approval gates for destructive actions.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-runbook-executor/)
