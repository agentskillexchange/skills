---
title: "PagerDuty Incident Runbook Linker"
description: "Automatically links PagerDuty incidents to relevant runbooks using the PagerDuty Events API v2 and service directory. Matches incident alerts to runbook tags via Elasticsearch fuzzy queries."
verification: security_reviewed
source: "https://github.com/PagerDuty/pdjs"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "pagerduty/pdjs"
  github_stars: 69
---

# PagerDuty Incident Runbook Linker

The PagerDuty Incident Runbook Linker bridges the gap between alerting and response by automatically associating PagerDuty incidents with relevant operational runbooks. It uses the PagerDuty REST API v2 to monitor incident creation events and extract service context, alert descriptions, and urgency levels. Runbook matching uses Elasticsearch fuzzy queries against a runbook index built from Confluence, Notion, or Markdown documentation repositories. The skill maintains a mapping between PagerDuty services, escalation policies, and runbook collections. When an incident fires, it posts the top-matched runbook links as incident notes and updates the incident custom fields with runbook metadata. Integration with the PagerDuty Events API v2 allows enriching alerts with runbook links before they create incidents. The skill tracks runbook effectiveness by correlating MTTR with runbook usage, identifying which runbooks lead to fastest resolution times and which need updating.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-runbook-linker/)
