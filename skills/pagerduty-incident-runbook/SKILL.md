---
name: PagerDuty Incident Runbook
description: Responds to PagerDuty incidents via the PagerDuty Events API v2 and REST
  API. Automatically executes diagnostic runbooks based on service and alert routing
  keys, and posts resolution notes back to the incident timeline.
category: Runbooks & Diagnostics
framework: OpenClaw
verification: security_reviewed
source: https://github.com/PagerDuty/pdjs
---
# PagerDuty Incident Runbook
Responds to PagerDuty incidents via the PagerDuty Events API v2 and REST API. Automatically executes diagnostic runbooks based on service and alert routing keys, and posts resolution notes back to the incident timeline.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/pagerduty-incident-runbook
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/pagerduty-incident-runbook` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-runbook/)
