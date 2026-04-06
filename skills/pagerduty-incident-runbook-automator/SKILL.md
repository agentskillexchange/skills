---
name: PagerDuty Incident Runbook Automator
description: Automates incident response runbooks using the PagerDuty Events API v2
  and REST API. Manages incident creation, escalation policies, and automated diagnostics
  triggered by alert severity.
category: "Runbooks &amp; Diagnostics"
framework: Gemini
verification: security_reviewed
source: "https://agentskillexchange.com/skills/pagerduty-incident-runbook-automator/"
---
# PagerDuty Incident Runbook Automator

Automates incident response runbooks using the PagerDuty Events API v2 and REST API. Manages incident creation, escalation policies, and automated diagnostics triggered by alert severity.

The PagerDuty Incident Runbook Automator skill integrates with the PagerDuty Events API v2 (events.pagerduty.com/v2/enqueue) and REST API (api.pagerduty.com) to automate incident response workflows. It creates incidents via the Events API with routing_key, event_action (trigger, acknowledge, resolve), and severity levels (critical, error, warning, info).

The skill manages incident lifecycle through REST API endpoints: POST /incidents for manual creation, PUT /incidents/{id} for status updates and reassignment, POST /incidents/{id}/notes for timeline annotations, and GET /incidents/{id}/log_entries for audit trail retrieval. It configures escalation policies using /escalation_policies with multi-level escalation rules and timeout-based progression.

Key capabilities include automated runbook execution triggered by webhook events (incident.trigger, incident.acknowledge), integration with monitoring tools via Events API v2 change events and alert grouping (time-based, intelligent, content-based), service dependency mapping through /service_dependencies for impact analysis, and response play automation with /response_plays for coordinated team mobilization. The automator also supports maintenance window management, on-call schedule rotation queries via /oncalls, and status page integration for external communication during incidents.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-runbook-automator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-runbook-automator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-runbook-automator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-runbook-automator -a codex
```

### OpenClaw

```bash
clawhub install pagerduty-incident-runbook-automator
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-runbook-automator/)
