---
title: "New Relic SLO Compliance Monitor"
description: "The New Relic SLO Compliance Monitor continuously tracks service level objective compliance by querying New Relic through the NerdGraph GraphQL API. It constructs NRQL queries to calculate availability, latency percentiles, and throughput metrics against defined SLO targets. Error budget consumption is tracked in real-time with configurable alert thresholds for budget burn rate acceleration. The agent supports multi-window burn rate alerting following Google SRE best practices with 1-hour, 6-hour, and 30-day evaluation windows. Compliance reports are generated with historical trend charts showing SLO attainment over configurable time periods. When error budgets approach exhaustion, the agent sends detailed notifications via Slack Incoming Webhooks including current burn rate, time until budget depletion, and top error contributors. Integration with New Relic Workloads enables entity-level SLO tracking across service groups. The tool maintains SLO definitions as code in YAML format for version-controlled SLO management."
source: "https://agentskillexchange.com/skills/new-relic-slo-compliance-monitor/"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "ChatGPT Agents"
---

# New Relic SLO Compliance Monitor

The New Relic SLO Compliance Monitor continuously tracks service level objective compliance by querying New Relic through the NerdGraph GraphQL API. It constructs NRQL queries to calculate availability, latency percentiles, and throughput metrics against defined SLO targets. Error budget consumption is tracked in real-time with configurable alert thresholds for budget burn rate acceleration. The agent supports multi-window burn rate alerting following Google SRE best practices with 1-hour, 6-hour, and 30-day evaluation windows. Compliance reports are generated with historical trend charts showing SLO attainment over configurable time periods. When error budgets approach exhaustion, the agent sends detailed notifications via Slack Incoming Webhooks including current burn rate, time until budget depletion, and top error contributors. Integration with New Relic Workloads enables entity-level SLO tracking across service groups. The tool maintains SLO definitions as code in YAML format for version-controlled SLO management.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/new-relic-slo-compliance-monitor/)
