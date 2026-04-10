---
title: "PagerDuty Event Orchestration Runbook"
description: "Builds incident runbooks around the PagerDuty Events API v2, Incidents API, and Response Plays so agents can classify alerts, enrich context, and drive consistent handoffs. Useful when noisy monitoring signals need a repeatable escalation flow instead of ad hoc human triage."
slug: "pagerduty-event-orchestration-runbook"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://developer.pagerduty.com/"
---

# PagerDuty Event Orchestration Runbook

Builds incident runbooks around the PagerDuty Events API v2, Incidents API, and Response Plays so agents can classify alerts, enrich context, and drive consistent handoffs. Useful when noisy monitoring signals need a repeatable escalation flow instead of ad hoc human triage.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install pagerduty-event-orchestration-runbook
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

PagerDuty Event Orchestration Runbook is for teams that want their agents to react to production incidents in a disciplined way instead of improvising from alert to alert. It works with real PagerDuty surfaces such as the Events API v2, Event Orchestration routing rules, the Incidents API, and Response Plays. That combination makes it practical for translating raw telemetry into routed incidents, attaching the right urgency, and kicking off the same follow-up steps every time a known failure pattern appears.
The skill is especially useful when alerts arrive from multiple systems with inconsistent payloads. It can normalize source data, map events to service-specific escalation paths, and check whether a responder workflow should page immediately or just create a lower-noise incident with enrichment. Because Response Plays and incident actions are part of the workflow, the runbook can also standardize stakeholder notifications, remediation notes, and links to relevant dashboards or logs.
Use this skill when you need reproducible incident handling for on-call teams, cleaner escalation logic, and fewer judgment calls in the first minutes of an operational event.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-event-orchestration-runbook/)
