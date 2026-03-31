---
name: "Datadog Incident Runbook Runner"
description: "Fetches an active Datadog incident, retrieves associated monitors and dashboards, pulls the last 30 minutes of metric data, and walks through a runbook checklist with automated triage steps. Reduces mean time to diagnosis by surfacing signal without dashboard navigation."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/datadog-incident-runbook-runner-2/"
---
# Datadog Incident Runbook Runner

Fetches an active Datadog incident, retrieves associated monitors and dashboards, pulls the last 30 minutes of metric data, and walks through a runbook checklist with automated triage steps. Reduces mean time to diagnosis by surfacing signal without dashboard navigation.

## Overview

Datadog Incident Runbook Runner is built around Datadog observability platform. The underlying ecosystem is represented by `DataDog/dd-trace-js` (787+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like metrics API, monitors, logs, dashboards, traces, incidents and preserving the operational context that matters for real tasks.

For incident response, the skill uses datadog APIs to pull the exact monitors, traces, schedules, or logs that matter, reducing dashboard hopping and making it easier to produce a handoff-quality timeline. The original use case is clear: Fetches an active Datadog incident, retrieves associated monitors and dashboards, pulls the last 30 minutes of metric data, and walks through a runbook checklist with automated triage steps. Reduces mean time to diagnosis by surfacing signal without dashboard navigation. The implementation typically relies on metrics API, monitors, logs, dashboards, traces, incidents, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

- Accesses metrics API, monitors, logs, dashboards, traces, incidents instead of scraping a UI, which makes runs easier to audit and retry.

- Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

- Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

- Fits into broader integration points such as incident response, APM, alerting, and operational dashboards.

As a runbook-style skill, the value is not just tool access but operational sequencing: check the right signals first, reduce alert noise, and produce a summary that another engineer can act on immediately. Key integration points include incident response, APM, alerting, and operational dashboards. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill datadog-incident-runbook-runner-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill datadog-incident-runbook-runner-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill datadog-incident-runbook-runner-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill datadog-incident-runbook-runner-2 -a codex
```

### OpenClaw

```bash
clawhub install datadog-incident-runbook-runner-2
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-incident-runbook-runner-2/)
