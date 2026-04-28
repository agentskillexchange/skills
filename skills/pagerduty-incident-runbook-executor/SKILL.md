---
title: "PagerDuty Incident Runbook Executor"
description: "Automatically executes diagnostic runbooks when PagerDuty incidents trigger, using the PagerDuty Events v2 API and Rundeck API. Attaches diagnostic output as incident notes and suggests remediation actions."
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

# PagerDuty Incident Runbook Executor

Automatically executes diagnostic runbooks when PagerDuty incidents trigger, using the PagerDuty Events v2 API and Rundeck API. Attaches diagnostic output as incident notes and suggests remediation actions.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/pagerduty-incident-runbook-executor/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/pagerduty-incident-runbook-executor
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/pagerduty-incident-runbook-executor`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-runbook-executor/)
