---
title: New Relic SLO Compliance Monitor
description: The New Relic SLO Compliance Monitor continuously tracks service level
  objective compliance by querying New Relic through the NerdGraph GraphQL API. It
  constructs NRQL queries to calculate availability, latency percentiles, and throughput
  metrics against defined SLO targets. Error budget consumption is tracked in real-time
  with configurable alert thresholds for budget burn rate acceleration. The agent
  supports multi-window burn rate alerting following Google SRE best practices with
  1-hour, 6-hour, and 30-day evaluation windows. Compliance reports are generated
  with historical trend charts showing SLO attainment over configurable time periods.
  When error budgets approach exhaustion, the agent sends detailed notifications via
  Slack Incoming Webhooks including current burn rate, time until budget depletion,
  and top error contributors. Integration with New Relic Workloads enables entity-level
  SLO tracking across service groups. The tool maintains SLO definitions as code in
  YAML format for version-controlled SLO management.
verification: security_reviewed
source: https://agentskillexchange.com/skills/new-relic-slo-compliance-monitor/
category:
- Monitoring &amp; Alerts
framework:
- ChatGPT Agents
---

# New Relic SLO Compliance Monitor

The New Relic SLO Compliance Monitor continuously tracks service level objective compliance by querying New Relic through the NerdGraph GraphQL API. It constructs NRQL queries to calculate availability, latency percentiles, and throughput metrics against defined SLO targets. Error budget consumption is tracked in real-time with configurable alert thresholds for budget burn rate acceleration. The agent supports multi-window burn rate alerting following Google SRE best practices with 1-hour, 6-hour, and 30-day evaluation windows. Compliance reports are generated with historical trend charts showing SLO attainment over configurable time periods. When error budgets approach exhaustion, the agent sends detailed notifications via Slack Incoming Webhooks including current burn rate, time until budget depletion, and top error contributors. Integration with New Relic Workloads enables entity-level SLO tracking across service groups. The tool maintains SLO definitions as code in YAML format for version-controlled SLO management.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/new-relic-slo-compliance-monitor/)
