---
title: "New Relic SLO Compliance Monitor"
description: "Tracks SLO compliance using the New Relic NerdGraph GraphQL API and NRQL queries. Calculates error budgets, burn rates, and generates compliance reports with Slack notifications via Incoming Webhooks."
verification: "security_reviewed"
source: "https://docs.newrelic.com/"
category:
  - "Monitoring & Alerts"
framework:
  - "ChatGPT Agents"
---

# New Relic SLO Compliance Monitor

The New Relic SLO Compliance Monitor continuously tracks service level objective compliance by querying New Relic through the NerdGraph GraphQL API. It constructs NRQL queries to calculate availability, latency percentiles, and throughput metrics against defined SLO targets. Error budget consumption is tracked in real-time with configurable alert thresholds for budget burn rate acceleration. The agent supports multi-window burn rate alerting following Google SRE best practices with 1-hour, 6-hour, and 30-day evaluation windows. Compliance reports are generated with historical trend charts showing SLO attainment over configurable time periods. When error budgets approach exhaustion, the agent sends detailed notifications via Slack Incoming Webhooks including current burn rate, time until budget depletion, and top error contributors. Integration with New Relic Workloads enables entity-level SLO tracking across service groups. The tool maintains SLO definitions as code in YAML format for version-controlled SLO management.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/new-relic-slo-compliance-monitor/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/new-relic-slo-compliance-monitor
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/new-relic-slo-compliance-monitor`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/new-relic-slo-compliance-monitor/)
