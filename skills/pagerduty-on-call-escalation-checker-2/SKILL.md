---
title: "PagerDuty On-Call Escalation Checker"
description: "Queries PagerDuty to show who is currently on-call for each escalation policy, surfaces unacknowledged incidents, and identifies schedule coverage gaps for the next 7 days. Useful for handoff checks and pre-weekend coverage audits. Read-only skill."
verification: security_reviewed
source: "https://github.com/PagerDuty/pdjs"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Code"
---

# PagerDuty On-Call Escalation Checker

Queries PagerDuty to show who is currently on-call for each escalation policy, surfaces unacknowledged incidents, and identifies schedule coverage gaps for the next 7 days. Useful for handoff checks and pre-weekend coverage audits. Read-only skill.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/pagerduty-on-call-escalation-checker-2
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/pagerduty-on-call-escalation-checker-2` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-on-call-escalation-checker-2/)
