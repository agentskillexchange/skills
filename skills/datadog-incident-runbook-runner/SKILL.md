---
name: Datadog Incident Runbook Runner
description: Fetches an active Datadog incident, retrieves its associated monitors and dashboards, pulls the last 30 minutes of metric data for affected services, and walks through a predefined runbook checklist with automated triage steps. Reduces mean time to diagnosis.
category: Runbooks &amp; Diagnostics
framework: Any Agent
verification: listed
rating: 4.6
reviews: 31
source: https://agentskillexchange.com/skill/datadog-incident-runbook-runner/
---

# Datadog Incident Runbook Runner

Fetches an active Datadog incident, retrieves its associated monitors and dashboards, pulls the last 30 minutes of metric data for affected services, and walks through a predefined runbook checklist with automated triage steps. Reduces mean time to diagnosis.

## Overview

Fetches an active Datadog incident, retrieves its associated monitors and dashboards, pulls the last 30 minutes of metric data for affected services, and walks through a predefined runbook checklist with automated triage steps. Reduces mean time to diagnosis.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill datadog-incident-runbook-runner
```

### OpenClaw

```bash
clawhub install datadog-incident-runbook-runner
```

### Claude Code

```bash
claude mcp add datadog-incident-runbook-runner
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/datadog-incident-runbook-runner/) for detailed installation instructions.

## Verification

- **Status**: listed
- **Category**: Runbooks &amp; Diagnostics
- **Framework**: Any Agent
- **Rating**: 4.6/5 (31 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/datadog-incident-runbook-runner/)
