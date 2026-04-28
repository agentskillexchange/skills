---
title: "PagerDuty Incident Runbook Engine"
description: "Generates automated incident response runbooks triggered by PagerDuty webhooks via the PagerDuty Events API v2. Integrates with Datadog API and AWS CloudWatch for diagnostic data collection during incidents."
verification: security_reviewed
source: "https://github.com/PagerDuty/pdjs"
category:
  - "Runbooks & Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "pagerduty/pdjs"
  github_stars: 69
  license: "Apache-2.0"
---

# PagerDuty Incident Runbook Engine

Generates automated incident response runbooks triggered by PagerDuty webhooks via the PagerDuty Events API v2. Integrates with Datadog API and AWS CloudWatch for diagnostic data collection during incidents.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/pagerduty-incident-runbook-engine/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/pagerduty-incident-runbook-engine
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/pagerduty-incident-runbook-engine`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-runbook-engine/)
