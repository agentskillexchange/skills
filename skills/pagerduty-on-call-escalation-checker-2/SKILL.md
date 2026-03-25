---
name: "PagerDuty On-Call Escalation Checker"
description: "Queries PagerDuty to show who is currently on-call for each escalation policy, surfaces unacknowledged incidents, and identifies schedule coverage gaps for the next 7 days. Useful for handoff checks and pre-weekend coverage audits. Read-only skill."
category: "Runbooks & Diagnostics"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/pagerduty-on-call-escalation-checker-2/"
tool_ecosystem:
  tool: "pagerduty"
  github_stars: 69
  npm_weekly_downloads: 210829
  github_repo: "PagerDuty/pdjs"
  license: "Apache-2.0"
  maintained: false
---

# PagerDuty On-Call Escalation Checker

Queries PagerDuty to show who is currently on-call for each escalation policy, surfaces unacknowledged incidents, and identifies schedule coverage gaps for the next 7 days. Useful for handoff checks and pre-weekend coverage audits. Read-only skill.

## Overview

**PagerDuty On-Call Escalation Checker** is built around PagerDuty incident response platform. The underlying ecosystem is represented by `PagerDuty/pdjs` (69+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like incidents, escalation policies, schedules, services, responders, analytics and preserving the operational context that matters for real tasks.

For incident response, the skill uses pagerduty APIs to pull the exact monitors, traces, schedules, or logs that matter, reducing dashboard hopping and making it easier to produce a handoff-quality timeline. The original use case is clear: Queries PagerDuty to show who is currently on-call for each escalation policy, surfaces unacknowledged incidents, and identifies schedule coverage gaps for the next 7 days. Useful for handoff checks and pre-weekend coverage audits. Read-only skill. The implementation typically relies on incidents, escalation policies, schedules, services, responders, analytics, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses incidents, escalation policies, schedules, services, responders, analytics instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as on-call checks, incident routing, and response coordination.

As a runbook-style skill, the value is not just tool access but operational sequencing: check the right signals first, reduce alert noise, and produce a summary that another engineer can act on immediately. Key integration points include on-call checks, incident routing, and response coordination. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pagerduty-on-call-escalation-checker-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pagerduty-on-call-escalation-checker-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pagerduty-on-call-escalation-checker-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pagerduty-on-call-escalation-checker-2 -a codex
```

### OpenClaw

```bash
clawhub install pagerduty-on-call-escalation-checker-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/pagerduty-on-call-escalation-checker-2/
