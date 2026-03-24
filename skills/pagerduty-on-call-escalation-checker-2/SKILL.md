---
name: "PagerDuty On-Call Escalation Checker"
description: "Queries PagerDuty to show who is currently on-call for each escalation policy, surfaces unacknowledged incidents, and identifies schedule coverage gaps for the next 7 days. Useful for handoff checks and pre-weekend coverage audits. Read-only skill."
category: "Runbooks & Diagnostics"
framework: "Claude Code"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
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

## Installation

### Any Agent (npx)
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

### OpenClaw
```bash
clawhub install pagerduty-on-call-escalation-checker-2
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill pagerduty-on-call-escalation-checker-2 -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Claude Code |
| **Verification** | 📋 Listed |
| **Tool** | [pagerduty](https://github.com/PagerDuty/pdjs) — ⭐ 69 · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-on-call-escalation-checker-2/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
