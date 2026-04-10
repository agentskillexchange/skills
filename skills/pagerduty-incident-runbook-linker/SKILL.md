---
name: "PagerDuty Incident Runbook Linker"
description: "Automatically links PagerDuty incidents to relevant runbooks using the PagerDuty Events API v2 and service directory. Matches incident alerts to runbook tags via Elasticsearch fuzzy queries."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/pagerduty-incident-runbook-linker/"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "OpenClaw"
---

# PagerDuty Incident Runbook Linker

The PagerDuty Incident Runbook Linker bridges the gap between alerting and response by automatically associating PagerDuty incidents with relevant operational runbooks. It uses the PagerDuty REST API v2 to monitor incident creation events and extract service context, alert descriptions, and urgency levels. Runbook matching uses Elasticsearch fuzzy queries against a runbook index built from Confluence, Notion, or Markdown documentation repositories. The skill maintains a mapping between PagerDuty services, escalation policies, and runbook collections. When an incident fires, it posts the top-matched runbook links as incident notes and updates the incident custom fields with runbook metadata. Integration with the PagerDuty Events API v2 allows enriching alerts with runbook links before they create incidents. The skill tracks runbook effectiveness by correlating MTTR with runbook usage, identifying which runbooks lead to fastest resolution times and which need updating.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-runbook-linker/)
