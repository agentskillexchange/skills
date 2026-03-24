---
name: "Incident Postmortem Generator"
description: "Generates structured incident postmortems by aggregating data from PagerDuty incidents API, Slack channel history, and Grafana dashboard snapshots. Produces blameless postmortem documents following the Google SRE template format."
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/incident-postmortem-generator/"
tool_ecosystem:
  tool: "pagerduty"
  github_stars: 69
  npm_weekly_downloads: 210829
  github_repo: "PagerDuty/pdjs"
  license: "Apache-2.0"
  maintained: false
---

# Incident Postmortem Generator

Generates structured incident postmortems by aggregating data from PagerDuty incidents API, Slack channel history, and Grafana dashboard snapshots. Produces blameless postmortem documents following the Google SRE template format.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill incident-postmortem-generator
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill incident-postmortem-generator -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill incident-postmortem-generator -a cursor
```

### OpenClaw
```bash
clawhub install incident-postmortem-generator
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill incident-postmortem-generator -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | ChatGPT Agents |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [pagerduty](https://github.com/PagerDuty/pdjs) — ⭐ 69 · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/incident-postmortem-generator/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
