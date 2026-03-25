---
name: "PagerDuty Incident Escalator"
description: "Manages PagerDuty incident lifecycle using the PagerDuty REST API v2 /incidents endpoint. Automates escalation policies, merges related incidents, and generates postmortem templates from incident timelines."
category: "Monitoring & Alerts"
framework: "ChatGPT Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/pagerduty-incident-escalator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "pagerduty"  # from ase_tool_match
  github_stars: 69  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 210829  # from ase_npm_downloads
  github_repo: "PagerDuty/pdjs"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: false  # from ase_tool_maintained
---

# PagerDuty Incident Escalator

Manages PagerDuty incident lifecycle using the PagerDuty REST API v2 /incidents endpoint. Automates escalation policies, merges related incidents, and generates postmortem templates from incident timelines.

## Overview

The PagerDuty Incident Escalator skill automates incident management through the PagerDuty REST API v2. It creates incidents via POST /incidents with proper urgency levels, escalation_policy references, and service associations. The skill monitors incident status transitions using GET /incidents with status filters and date_range parameters. Related incidents are automatically detected through title similarity scoring and merged via PUT /incidents merge to reduce alert fatigue. Escalation policy management uses the /escalation_policies endpoint to dynamically adjust on-call rotations based on incident severity and team availability queried from /oncalls. The skill generates postmortem templates by reconstructing incident timelines from log_entries with full context. Priority classification leverages /priorities to map business impact to PagerDuty priority levels (P1-P5). Response play automation triggers predefined response procedures for critical incidents. Integration with services and integrations endpoints enables automatic incident creation from monitoring tool webhooks. Analytics data from /analytics/metrics/incidents provides mean-time-to-acknowledge and mean-time-to-resolve metrics for continuous improvement tracking.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-escalator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-escalator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-escalator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-escalator -a codex
```

### OpenClaw

```bash
clawhub install pagerduty-incident-escalator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/pagerduty-incident-escalator/
