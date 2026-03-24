---
name: "New Relic SLO Compliance Monitor"
description: "Tracks SLO compliance using the New Relic NerdGraph GraphQL API and NRQL queries. Calculates error budgets, burn rates, and generates compliance reports with Slack notifications via Incoming Webhooks."
category: "Monitoring & Alerts"
framework: "ChatGPT Agents"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/new-relic-slo-compliance-monitor/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "slack"  # from ase_tool_match
  github_stars: 2900  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 2433529  # from ase_npm_downloads
  github_repo: "slackapi/bolt-js"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# New Relic SLO Compliance Monitor

Tracks SLO compliance using the New Relic NerdGraph GraphQL API and NRQL queries. Calculates error budgets, burn rates, and generates compliance reports with Slack notifications via Incoming Webhooks.

## Overview

The New Relic SLO Compliance Monitor continuously tracks service level objective compliance by querying New Relic through the NerdGraph GraphQL API. It constructs NRQL queries to calculate availability, latency percentiles, and throughput metrics against defined SLO targets. Error budget consumption is tracked in real-time with configurable alert thresholds for budget burn rate acceleration. The agent supports multi-window burn rate alerting following Google SRE best practices with 1-hour, 6-hour, and 30-day evaluation windows. Compliance reports are generated with historical trend charts showing SLO attainment over configurable time periods. When error budgets approach exhaustion, the agent sends detailed notifications via Slack Incoming Webhooks including current burn rate, time until budget depletion, and top error contributors. Integration with New Relic Workloads enables entity-level SLO tracking across service groups. The tool maintains SLO definitions as code in YAML format for version-controlled SLO management.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill new-relic-slo-compliance-monitor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill new-relic-slo-compliance-monitor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill new-relic-slo-compliance-monitor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill new-relic-slo-compliance-monitor -a codex
```

### OpenClaw

```bash
clawhub install new-relic-slo-compliance-monitor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/new-relic-slo-compliance-monitor/
