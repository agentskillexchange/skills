---
title: "PagerDuty Incident Runbook Linker"
description: "Automatically links PagerDuty incidents to relevant runbooks using the PagerDuty Events API v2 and service directory. Matches incident alerts to runbook tags via Elasticsearch fuzzy queries."
verification: security_reviewed
source: "https://github.com/PagerDuty/pdjs"
category:
  - "Monitoring & Alerts"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "pagerduty/pdjs"
  github_stars: 69
---

# PagerDuty Incident Runbook Linker

The PagerDuty Incident Runbook Linker bridges the gap between alerting and response by automatically associating PagerDuty incidents with relevant operational runbooks. It uses the PagerDuty REST API v2 to monitor incident creation events and extract service context, alert descriptions, and urgency levels. Runbook matching uses Elasticsearch fuzzy queries against a runbook index built from Confluence, Notion, or Markdown documentation repositories. The skill maintains a mapping between PagerDuty services, escalation policies, and runbook collections. When an incident fires, it posts the top-matched runbook links as incident notes and updates the incident custom fields with runbook metadata. Integration with the PagerDuty Events API v2 allows enriching alerts with runbook links before they create incidents. The skill tracks runbook effectiveness by correlating MTTR with runbook usage, identifying which runbooks lead to fastest resolution times and which need updating.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/pagerduty-incident-runbook-linker
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/pagerduty-incident-runbook-linker` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-runbook-linker/)
