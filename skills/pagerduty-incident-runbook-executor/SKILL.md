---
title: "PagerDuty Incident Runbook Executor"
description: "Automatically executes diagnostic runbooks when PagerDuty incidents trigger, using the PagerDuty Events v2 API and Rundeck API. Attaches diagnostic output as incident notes and suggests remediation actions."
verification: "security_reviewed"
source: "https://github.com/PagerDuty/pdjs"
category:
  - "Runbooks & Diagnostics"
framework:
  - "OpenClaw"
---

# PagerDuty Incident Runbook Executor

The PagerDuty Incident Runbook Executor skill bridges alerting and automated diagnostics by connecting PagerDuty incidents to executable runbooks. When an incident triggers via the PagerDuty Events v2 API webhook, the skill matches the incident service and urgency to appropriate diagnostic runbooks stored in Rundeck. It executes targeted diagnostic jobs through the Rundeck API, capturing command outputs, log snippets, and metric snapshots. Results are formatted as structured incident notes and posted back to PagerDuty via the Incidents API. The skill supports conditional runbook chaining — if initial diagnostics indicate a specific failure mode, follow-up runbooks execute automatically. Includes escalation logic that pages additional responders when diagnostics reveal critical issues. Generates post-incident summaries with timeline reconstruction and root cause suggestions. Supports custom runbooks defined in YAML with parameterized steps and approval gates for destructive actions.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-runbook-executor/)
