---
title: "PagerDuty On-Call Escalation Checker"
description: "Queries PagerDuty to show who is currently on-call for each escalation policy, surfaces unacknowledged incidents, and identifies schedule coverage gaps for the next 7 days. Useful for handoff checks and pre-weekend coverage audits. Read-only skill."
verification: security_reviewed
source: "https://github.com/PagerDuty/pdjs"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Claude Code"
---

# PagerDuty On-Call Escalation Checker

Queries PagerDuty to show who is currently on-call for each escalation policy, surfaces unacknowledged incidents, and identifies schedule coverage gaps for the next 7 days. Useful for handoff checks and pre-weekend coverage audits. Read-only skill.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/pagerduty-on-call-escalation-checker-2/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/pagerduty-on-call-escalation-checker-2
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/pagerduty-on-call-escalation-checker-2`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-on-call-escalation-checker-2/)
