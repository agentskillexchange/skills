---
title: "PagerDuty Incident Runbook Linker"
description: "Automatically links PagerDuty incidents to relevant runbooks using the PagerDuty Events API v2 and service directory. Matches incident alerts to runbook tags via Elasticsearch fuzzy queries."
verification: security_reviewed
source: "https://github.com/PagerDuty/pdjs"
category:
  - "Monitoring & Alerts"
framework:
  - "OpenClaw"
---

# PagerDuty Incident Runbook Linker

Automatically links PagerDuty incidents to relevant runbooks using the PagerDuty Events API v2 and service directory. Matches incident alerts to runbook tags via Elasticsearch fuzzy queries.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/pagerduty-incident-runbook-linker/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/pagerduty-incident-runbook-linker
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/pagerduty-incident-runbook-linker`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-runbook-linker/)
