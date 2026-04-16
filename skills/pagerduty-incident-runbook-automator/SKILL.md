---
title: "PagerDuty Incident Runbook Automator"
description: "Automates incident response runbooks using the PagerDuty Events API v2 and REST API. Manages incident creation, escalation policies, and automated diagnostics triggered by alert severity."
verification: "security_reviewed"
source: "https://github.com/PagerDuty/pdjs"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Gemini"
---

# PagerDuty Incident Runbook Automator

The PagerDuty Incident Runbook Automator skill integrates with the PagerDuty Events API v2 (events.pagerduty.com/v2/enqueue) and REST API (api.pagerduty.com) to automate incident response workflows. It creates incidents via the Events API with routing_key, event_action (trigger, acknowledge, resolve), and severity levels (critical, error, warning, info).


The skill manages incident lifecycle through REST API endpoints: POST /incidents for manual creation, PUT /incidents/{id} for status updates and reassignment, POST /incidents/{id}/notes for timeline annotations, and GET /incidents/{id}/log_entries for audit trail retrieval. It configures escalation policies using /escalation_policies with multi-level escalation rules and timeout-based progression.


Key capabilities include automated runbook execution triggered by webhook events (incident.trigger, incident.acknowledge), integration with monitoring tools via Events API v2 change events and alert grouping (time-based, intelligent, content-based), service dependency mapping through /service_dependencies for impact analysis, and response play automation with /response_plays for coordinated team mobilization. The automator also supports maintenance window management, on-call schedule rotation queries via /oncalls, and status page integration for external communication during incidents.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-runbook-automator/)
