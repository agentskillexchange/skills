---
name: "PagerDuty On-Call Escalation Checker"
description: "Queries PagerDuty to show who is currently on-call for each escalation policy, surfaces any unacknowledged incidents, and identifies schedule coverage gaps for the next 7 days. Useful for handoff checks and pre-weekend coverage audits. Read-only skill."
category: "Runbooks & Diagnostics"
framework: "Claude Code"
verification: listed
rating: 4.7
reviews: 45
creator: "Raj Gupta"
creator_handle: "@rajgupta"
creator_verified: true
source: "https://agentskillexchange.com/skills/pagerduty-on-call-escalation-checker/"
---
# PagerDuty On-Call Escalation Checker

Queries PagerDuty to show who is currently on-call for each escalation policy, surfaces any unacknowledged incidents, and identifies schedule coverage gaps for the next 7 days. Useful for handoff checks and pre-weekend coverage audits. Read-only skill.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill pagerduty-on-call-escalation-checker
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pagerduty-on-call-escalation-checker -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pagerduty-on-call-escalation-checker -a cursor
```

### OpenClaw

```bash
clawhub install pagerduty-on-call-escalation-checker
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pagerduty-on-call-escalation-checker -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Claude Code |
| Verification | Listed |
| Rating | 4.7/5 (45 reviews) |

## Creator

**Raj Gupta** (Verified Creator ✓)
- Profile: [@rajgupta](https://agentskillexchange.com/browse-skills/?creator=rajgupta)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/pagerduty-on-call-escalation-checker/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
