---
name: "PagerDuty On-Call Escalation Checker"
description: "Queries PagerDuty to show who is currently on-call for each escalation policy, surfaces unacknowledged incidents, and identifies schedule coverage gaps for the next 7 days. Useful for handoff checks and pre-weekend coverage audits. Read-only skill."
category: "Runbooks & Diagnostics"
framework: "Claude Code"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/pagerduty-on-call-escalation-checker-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "pagerduty"  # from ase_tool_match
  github_stars: 69  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 210829  # from ase_npm_downloads
  github_repo: "PagerDuty/pdjs"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: false  # from ase_tool_maintained
---

# PagerDuty On-Call Escalation Checker

Queries PagerDuty to show who is currently on-call for each escalation policy, surfaces unacknowledged incidents, and identifies schedule coverage gaps for the next 7 days. Useful for handoff checks and pre-weekend coverage audits. Read-only skill.

## Overview

Queries PagerDuty to show who is currently on-call for each escalation policy, surfaces unacknowledged incidents, and identifies schedule coverage gaps for the next 7 days. Useful for handoff checks and pre-weekend coverage audits. Read-only skill.

## Installation

### Any Agent

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

### Codex

```bash
npx skills add agentskillexchange/skills --skill pagerduty-on-call-escalation-checker-2 -a codex
```

### OpenClaw

```bash
clawhub install pagerduty-on-call-escalation-checker-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/pagerduty-on-call-escalation-checker-2/
