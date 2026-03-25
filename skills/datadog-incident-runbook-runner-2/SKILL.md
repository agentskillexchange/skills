---
name: "Datadog Incident Runbook Runner"
description: "Fetches an active Datadog incident, retrieves associated monitors and dashboards, pulls the last 30 minutes of metric data, and walks through a runbook checklist with automated triage steps. Reduces mean time to diagnosis by surfacing signal without dashboard navigation."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/datadog-incident-runbook-runner-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "datadog"  # from ase_tool_match
  github_stars: 787  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 6043057  # from ase_npm_downloads
  github_repo: "DataDog/dd-trace-js"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Datadog Incident Runbook Runner

Fetches an active Datadog incident, retrieves associated monitors and dashboards, pulls the last 30 minutes of metric data, and walks through a runbook checklist with automated triage steps. Reduces mean time to diagnosis by surfacing signal without dashboard navigation.

## Overview

Fetches an active Datadog incident, retrieves associated monitors and dashboards, pulls the last 30 minutes of metric data, and walks through a runbook checklist with automated triage steps. Reduces mean time to diagnosis by surfacing signal without dashboard navigation.

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

- Marketplace: https://agentskillexchange.com/skills/datadog-incident-runbook-runner-2/
