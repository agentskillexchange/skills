---
title: PagerDuty Incident Runbook Automator
description: 'The PagerDuty Incident Runbook Automator skill integrates with the PagerDuty
  Events API v2 (events.pagerduty.com/v2/enqueue) and REST API (api.pagerduty.com)
  to automate incident response workflows. It creates incidents via the Events API
  with routing_key, event_action (trigger, acknowledge, resolve), and severity levels
  (critical, error, warning, info). The skill manages incident lifecycle through REST
  API endpoints: POST /incidents for manual creation, PUT /incidents/{id} for status
  updates and reassignment, POST /incidents/{id}/notes for timeline annotations, and
  GET /incidents/{id}/log_entries for audit trail retrieval. It configures escalation
  policies using /escalation_policies with multi-level escalation rules and timeout-based
  progression. Key capabilities include automated runbook execution triggered by webhook
  events (incident.trigger, incident.acknowledge), integration with monitoring tools
  via Events API v2 change events and alert grouping (time-based, intelligent, content-based),
  service dependency mapping through /service_dependencies for impact analysis, and
  response play automation with /response_plays for coordinated team mobilization.
  The automator also supports maintenance window management, on-call schedule rotation
  queries via /oncalls, and status page integration for external communication during
  incidents.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/pagerduty-incident-runbook-automator/
category:
- Runbooks &amp; Diagnostics
framework:
- Gemini
---

# PagerDuty Incident Runbook Automator

The PagerDuty Incident Runbook Automator skill integrates with the PagerDuty Events API v2 (events.pagerduty.com/v2/enqueue) and REST API (api.pagerduty.com) to automate incident response workflows. It creates incidents via the Events API with routing_key, event_action (trigger, acknowledge, resolve), and severity levels (critical, error, warning, info). The skill manages incident lifecycle through REST API endpoints: POST /incidents for manual creation, PUT /incidents/{id} for status updates and reassignment, POST /incidents/{id}/notes for timeline annotations, and GET /incidents/{id}/log_entries for audit trail retrieval. It configures escalation policies using /escalation_policies with multi-level escalation rules and timeout-based progression. Key capabilities include automated runbook execution triggered by webhook events (incident.trigger, incident.acknowledge), integration with monitoring tools via Events API v2 change events and alert grouping (time-based, intelligent, content-based), service dependency mapping through /service_dependencies for impact analysis, and response play automation with /response_plays for coordinated team mobilization. The automator also supports maintenance window management, on-call schedule rotation queries via /oncalls, and status page integration for external communication during incidents.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-runbook-automator/)
