---
name: "Datadog Incident Runbook Runner"
description: "Fetches an active Datadog incident, retrieves associated monitors and dashboards, pulls the last 30 minutes of metric data, and walks through a runbook checklist with automated triage steps. Reduces mean time to diagnosis by surfacing signal without dashboard navigation."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: verified_metadata
rating: 4.5
reviews: 54
creator: "Nathan Brooks"
creator_handle: "@nbrooks"
creator_verified: false
source: "https://agentskillexchange.com/skills/datadog-incident-runbook-runner-2/"
---
# Datadog Incident Runbook Runner

Fetches an active Datadog incident, retrieves associated monitors and dashboards, pulls the last 30 minutes of metric data, and walks through a runbook checklist with automated triage steps. Reduces mean time to diagnosis by surfacing signal without dashboard navigation.

## Installation

### Any agent (npx skills)

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

### OpenClaw

```bash
clawhub install datadog-incident-runbook-runner-2
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill datadog-incident-runbook-runner-2 -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | OpenClaw |
| Verification | Verified Metadata |
| Rating | 4.5/5 (54 reviews) |

## Creator

**Nathan Brooks**
- Profile: [@nbrooks](https://agentskillexchange.com/browse-skills/?creator=nbrooks)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-incident-runbook-runner-2/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
