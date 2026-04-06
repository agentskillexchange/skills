---
name: PagerDuty Incident Runbook Executor
description: Automatically executes diagnostic runbooks when PagerDuty incidents trigger,
  using the PagerDuty Events v2 API and Rundeck API. Attaches diagnostic output as
  incident notes and suggests remediation actions.
category: "Runbooks &amp; Diagnostics"
framework: OpenClaw
verification: security_reviewed
source: "https://agentskillexchange.com/skills/pagerduty-incident-runbook-executor/"
---
# PagerDuty Incident Runbook Executor

Automatically executes diagnostic runbooks when PagerDuty incidents trigger, using the PagerDuty Events v2 API and Rundeck API. Attaches diagnostic output as incident notes and suggests remediation actions.

The PagerDuty Incident Runbook Executor skill bridges alerting and automated diagnostics by connecting PagerDuty incidents to executable runbooks. When an incident triggers via the PagerDuty Events v2 API webhook, the skill matches the incident service and urgency to appropriate diagnostic runbooks stored in Rundeck. It executes targeted diagnostic jobs through the Rundeck API, capturing command outputs, log snippets, and metric snapshots. Results are formatted as structured incident notes and posted back to PagerDuty via the Incidents API. The skill supports conditional runbook chaining — if initial diagnostics indicate a specific failure mode, follow-up runbooks execute automatically. Includes escalation logic that pages additional responders when diagnostics reveal critical issues. Generates post-incident summaries with timeline reconstruction and root cause suggestions. Supports custom runbooks defined in YAML with parameterized steps and approval gates for destructive actions.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-runbook-executor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-runbook-executor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-runbook-executor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-runbook-executor -a codex
```

### OpenClaw

```bash
clawhub install pagerduty-incident-runbook-executor
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-runbook-executor/)
