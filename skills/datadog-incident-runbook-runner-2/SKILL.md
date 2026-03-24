---
name: "Datadog Incident Runbook Runner"
description: "Fetches an active Datadog incident, retrieves associated monitors and dashboards, pulls the last 30 minutes of metric data, and walks through a runbook checklist with automated triage steps. Reduces mean time to diagnosis by surfacing signal without dashboard navigation."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/datadog-incident-runbook-runner-2/"
tool_ecosystem:
  tool: "datadog"
  github_stars: 787
  npm_weekly_downloads: 6043057
  github_repo: "DataDog/dd-trace-js"
  license: "NOASSERTION"
  maintained: true
---

# Datadog Incident Runbook Runner

Fetches an active Datadog incident, retrieves associated monitors and dashboards, pulls the last 30 minutes of metric data, and walks through a runbook checklist with automated triage steps. Reduces mean time to diagnosis by surfacing signal without dashboard navigation.

## Installation

### Any Agent (npx)
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

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | OpenClaw |
| **Verification** | 📋 Listed |
| **Tool** | [datadog](https://github.com/DataDog/dd-trace-js) — ⭐ 787 · NOASSERTION |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-incident-runbook-runner-2/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
