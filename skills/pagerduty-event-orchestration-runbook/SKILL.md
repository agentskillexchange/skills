---
name: "PagerDuty Event Orchestration Runbook"
description: "Builds incident runbooks around the PagerDuty Events API v2, Incidents API, and Response Plays so agents can classify alerts, enrich context, and drive consistent handoffs. Useful when noisy monitoring signals need a repeatable escalation flow instead of ad hoc human triage."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/pagerduty-event-orchestration-runbook/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "pagerduty"  # from ase_tool_match
  github_stars: 69  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 210829  # from ase_npm_downloads
  github_repo: "PagerDuty/pdjs"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: false  # from ase_tool_maintained
---

# PagerDuty Event Orchestration Runbook

Builds incident runbooks around the PagerDuty Events API v2, Incidents API, and Response Plays so agents can classify alerts, enrich context, and drive consistent handoffs. Useful when noisy monitoring signals need a repeatable escalation flow instead of ad hoc human triage.

## Overview

PagerDuty Event Orchestration Runbook is for teams that want their agents to react to production incidents in a disciplined way instead of improvising from alert to alert. It works with real PagerDuty surfaces such as the Events API v2, Event Orchestration routing rules, the Incidents API, and Response Plays. That combination makes it practical for translating raw telemetry into routed incidents, attaching the right urgency, and kicking off the same follow-up steps every time a known failure pattern appears.

The skill is especially useful when alerts arrive from multiple systems with inconsistent payloads. It can normalize source data, map events to service-specific escalation paths, and check whether a responder workflow should page immediately or just create a lower-noise incident with enrichment. Because Response Plays and incident actions are part of the workflow, the runbook can also standardize stakeholder notifications, remediation notes, and links to relevant dashboards or logs.

Use this skill when you need reproducible incident handling for on-call teams, cleaner escalation logic, and fewer judgment calls in the first minutes of an operational event.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pagerduty-event-orchestration-runbook
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pagerduty-event-orchestration-runbook -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pagerduty-event-orchestration-runbook -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pagerduty-event-orchestration-runbook -a codex
```

### OpenClaw

```bash
clawhub install pagerduty-event-orchestration-runbook
```

## Source

- Marketplace: https://agentskillexchange.com/skills/pagerduty-event-orchestration-runbook/
