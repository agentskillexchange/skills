---
title: "PagerDuty On-Call Escalation Checker"
description: "Queries PagerDuty to show who is currently on-call for each escalation policy, surfaces unacknowledged incidents, and identifies schedule coverage gaps for the next 7 days. Useful for handoff checks and pre-weekend coverage audits. Read-only skill."
verification: listed
source: "https://agentskillexchange.com/skills/pagerduty-on-call-escalation-checker-2/"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Claude Code"
---

# PagerDuty On-Call Escalation Checker

Queries PagerDuty to show who is currently on-call for each escalation policy, surfaces unacknowledged incidents, and identifies schedule coverage gaps for the next 7 days. Useful for handoff checks and pre-weekend coverage audits. Read-only skill.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-on-call-escalation-checker-2/)
