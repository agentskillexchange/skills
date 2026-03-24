---
name: "PagerDuty On-Call Escalation Checker"
description: "Queries PagerDuty to show who is currently on-call for each escalation policy, surfaces unacknowledged incidents, and identifies schedule coverage gaps for the next 7 days. Useful for handoff checks and pre-weekend coverage audits. Read-only skill."
category: "Runbooks & Diagnostics"
framework: "Claude Code"
verification: security_reviewed
rating: 4.2
reviews: 66
creator: "James Whitfield"
creator_handle: "@jwhitfield"
creator_verified: true
source: "https://agentskillexchange.com/skills/pagerduty-on-call-escalation-checker-2/"
---
# PagerDuty On-Call Escalation Checker

Queries PagerDuty to show who is currently on-call for each escalation policy, surfaces unacknowledged incidents, and identifies schedule coverage gaps for the next 7 days. Useful for handoff checks and pre-weekend coverage audits. Read-only skill.

## Installation

### Any agent (npx skills)

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

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Claude Code |
| Verification | Security Reviewed |
| Rating | 4.2/5 (66 reviews) |

## Creator

**James Whitfield** (Verified Creator ✓)
- Profile: [@jwhitfield](https://agentskillexchange.com/browse-skills/?creator=jwhitfield)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/pagerduty-on-call-escalation-checker-2/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
