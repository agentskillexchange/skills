---
title: "Datadog Incident Runbook Runner"
description: "Fetches an active Datadog incident, retrieves associated monitors and dashboards, pulls the last 30 minutes of metric data, and walks through a runbook checklist with automated triage steps. Reduces mean time to diagnosis by surfacing signal without dashboard navigation."
verification: security_reviewed
source: "https://github.com/DataDog/dd-trace-js"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
---

# Datadog Incident Runbook Runner

Fetches an active Datadog incident, retrieves associated monitors and dashboards, pulls the last 30 minutes of metric data, and walks through a runbook checklist with automated triage steps. Reduces mean time to diagnosis by surfacing signal without dashboard navigation.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/datadog-incident-runbook-runner-2/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/datadog-incident-runbook-runner-2
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/datadog-incident-runbook-runner-2`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-incident-runbook-runner-2/)
