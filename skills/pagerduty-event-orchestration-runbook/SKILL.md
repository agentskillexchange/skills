---
title: "PagerDuty Event Orchestration Runbook"
slug: "pagerduty-event-orchestration-runbook"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
source: "https://developer.pagerduty.com/"
---

# PagerDuty Event Orchestration Runbook

Builds incident runbooks around the PagerDuty Events API v2, Incidents API, and Response Plays so agents can classify alerts, enrich context, and drive consistent handoffs. Useful when noisy monitoring signals need a repeatable escalation flow instead of ad hoc human triage.

## Installation

Choose the method that fits your setup:

1. Clone or download this repo and copy the skill folder into your local skills directory.
2. Install from the Agent Skill Exchange repo with your preferred Git workflow.
3. Add the skill folder as a git submodule if you manage skills as dependencies.
4. Copy the files manually into a local custom-skills directory for testing.
5. Use any marketplace or sync tooling you already have for pulling ASE skills.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-event-orchestration-runbook/)
