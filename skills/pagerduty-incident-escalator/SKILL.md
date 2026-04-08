---
title: PagerDuty Incident Escalator
description: The PagerDuty Incident Escalator skill automates incident management
  through the PagerDuty REST API v2. It creates incidents via POST /incidents with
  proper urgency levels, escalation_policy references, and service associations. The
  skill monitors incident status transitions using GET /incidents with status filters
  and date_range parameters. Related incidents are automatically detected through
  title similarity scoring and merged via PUT /incidents merge to reduce alert fatigue.
  Escalation policy management uses the /escalation_policies endpoint to dynamically
  adjust on-call rotations based on incident severity and team availability queried
  from /oncalls. The skill generates postmortem templates by reconstructing incident
  timelines from log_entries with full context. Priority classification leverages
  /priorities to map business impact to PagerDuty priority levels (P1-P5). Response
  play automation triggers predefined response procedures for critical incidents.
  Integration with services and integrations endpoints enables automatic incident
  creation from monitoring tool webhooks. Analytics data from /analytics/metrics/incidents
  provides mean-time-to-acknowledge and mean-time-to-resolve metrics for continuous
  improvement tracking.
verification: security_reviewed
source: https://agentskillexchange.com/skills/pagerduty-incident-escalator/
category:
- Monitoring &amp; Alerts
framework:
- ChatGPT Agents
---

# PagerDuty Incident Escalator

The PagerDuty Incident Escalator skill automates incident management through the PagerDuty REST API v2. It creates incidents via POST /incidents with proper urgency levels, escalation_policy references, and service associations. The skill monitors incident status transitions using GET /incidents with status filters and date_range parameters. Related incidents are automatically detected through title similarity scoring and merged via PUT /incidents merge to reduce alert fatigue. Escalation policy management uses the /escalation_policies endpoint to dynamically adjust on-call rotations based on incident severity and team availability queried from /oncalls. The skill generates postmortem templates by reconstructing incident timelines from log_entries with full context. Priority classification leverages /priorities to map business impact to PagerDuty priority levels (P1-P5). Response play automation triggers predefined response procedures for critical incidents. Integration with services and integrations endpoints enables automatic incident creation from monitoring tool webhooks. Analytics data from /analytics/metrics/incidents provides mean-time-to-acknowledge and mean-time-to-resolve metrics for continuous improvement tracking.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-escalator/)
