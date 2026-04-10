---
title: "New Relic SLO Compliance Monitor"
description: "Tracks SLO compliance using the New Relic NerdGraph GraphQL API and NRQL queries. Calculates error budgets, burn rates, and generates compliance reports with Slack notifications via Incoming Webhooks."
slug: "new-relic-slo-compliance-monitor"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/new-relic-slo-compliance-monitor/"
---

# New Relic SLO Compliance Monitor

Tracks SLO compliance using the New Relic NerdGraph GraphQL API and NRQL queries. Calculates error budgets, burn rates, and generates compliance reports with Slack notifications via Incoming Webhooks.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install new-relic-slo-compliance-monitor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The New Relic SLO Compliance Monitor continuously tracks service level objective compliance by querying New Relic through the NerdGraph GraphQL API. It constructs NRQL queries to calculate availability, latency percentiles, and throughput metrics against defined SLO targets. Error budget consumption is tracked in real-time with configurable alert thresholds for budget burn rate acceleration. The agent supports multi-window burn rate alerting following Google SRE best practices with 1-hour, 6-hour, and 30-day evaluation windows. Compliance reports are generated with historical trend charts showing SLO attainment over configurable time periods. When error budgets approach exhaustion, the agent sends detailed notifications via Slack Incoming Webhooks including current burn rate, time until budget depletion, and top error contributors. Integration with New Relic Workloads enables entity-level SLO tracking across service groups. The tool maintains SLO definitions as code in YAML format for version-controlled SLO management.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/new-relic-slo-compliance-monitor/)
