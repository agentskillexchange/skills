---
title: PagerDuty Incident Runbook Linker
description: The PagerDuty Incident Runbook Linker bridges the gap between alerting
  and response by automatically associating PagerDuty incidents with relevant operational
  runbooks. It uses the PagerDuty REST API v2 to monitor incident creation events
  and extract service context, alert descriptions, and urgency levels. Runbook matching
  uses Elasticsearch fuzzy queries against a runbook index built from Confluence,
  Notion, or Markdown documentation repositories. The skill maintains a mapping between
  PagerDuty services, escalation policies, and runbook collections. When an incident
  fires, it posts the top-matched runbook links as incident notes and updates the
  incident custom fields with runbook metadata. Integration with the PagerDuty Events
  API v2 allows enriching alerts with runbook links before they create incidents.
  The skill tracks runbook effectiveness by correlating MTTR with runbook usage, identifying
  which runbooks lead to fastest resolution times and which need updating.
verification: security_reviewed
source: https://agentskillexchange.com/skills/pagerduty-incident-runbook-linker/
category:
- Monitoring &amp; Alerts
framework:
- OpenClaw
---

# PagerDuty Incident Runbook Linker

The PagerDuty Incident Runbook Linker bridges the gap between alerting and response by automatically associating PagerDuty incidents with relevant operational runbooks. It uses the PagerDuty REST API v2 to monitor incident creation events and extract service context, alert descriptions, and urgency levels. Runbook matching uses Elasticsearch fuzzy queries against a runbook index built from Confluence, Notion, or Markdown documentation repositories. The skill maintains a mapping between PagerDuty services, escalation policies, and runbook collections. When an incident fires, it posts the top-matched runbook links as incident notes and updates the incident custom fields with runbook metadata. Integration with the PagerDuty Events API v2 allows enriching alerts with runbook links before they create incidents. The skill tracks runbook effectiveness by correlating MTTR with runbook usage, identifying which runbooks lead to fastest resolution times and which need updating.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-runbook-linker/)
