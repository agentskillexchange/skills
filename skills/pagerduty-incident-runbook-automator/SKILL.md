---
title: "PagerDuty Incident Runbook Automator"
description: "The PagerDuty Incident Runbook Automator skill integrates with the PagerDuty Events API v2 (events.pagerduty.com/v2/enqueue) and REST API (api.pagerduty.com) to automate incident response workflows. It creates incidents via the Events API with routing_key, event_action (trigger, acknowledge, resolve), and severity levels (critical, error, warning, info).\nThe skill manages incident lifecycle through REST API endpoints: POST /incidents for manual creation, PUT /incidents/{id} for status updates and reassignment, POST /incidents/{id}/notes for timeline annotations, and GET /incidents/{id}/log_entries for audit trail retrieval. It configures escalation policies using /escalation_policies with multi-level escalation rules and timeout-based progression.\nKey capabilities include automated runbook execution triggered by webhook events (incident.trigger, incident.acknowledge), integration with monitoring tools via Events API v2 change events and alert grouping (time-based, intelligent, content-based), service dependency mapping through /service_dependencies for impact analysis, and response play automation with /response_plays for coordinated team mobilization. The automator also supports maintenance window management, on-call schedule rotation queries via /oncalls, and status page integration for external communication during incidents."
verification: security_reviewed
source: "https://github.com/PagerDuty/pdjs"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "pagerduty/pdjs"
  github_stars: 69
---

# PagerDuty Incident Runbook Automator

The PagerDuty Incident Runbook Automator skill integrates with the PagerDuty Events API v2 (events.pagerduty.com/v2/enqueue) and REST API (api.pagerduty.com) to automate incident response workflows. It creates incidents via the Events API with routing_key, event_action (trigger, acknowledge, resolve), and severity levels (critical, error, warning, info).
The skill manages incident lifecycle through REST API endpoints: POST /incidents for manual creation, PUT /incidents/{id} for status updates and reassignment, POST /incidents/{id}/notes for timeline annotations, and GET /incidents/{id}/log_entries for audit trail retrieval. It configures escalation policies using /escalation_policies with multi-level escalation rules and timeout-based progression.
Key capabilities include automated runbook execution triggered by webhook events (incident.trigger, incident.acknowledge), integration with monitoring tools via Events API v2 change events and alert grouping (time-based, intelligent, content-based), service dependency mapping through /service_dependencies for impact analysis, and response play automation with /response_plays for coordinated team mobilization. The automator also supports maintenance window management, on-call schedule rotation queries via /oncalls, and status page integration for external communication during incidents.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/pagerduty-incident-runbook-automator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/pagerduty-incident-runbook-automator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-runbook-automator/)
