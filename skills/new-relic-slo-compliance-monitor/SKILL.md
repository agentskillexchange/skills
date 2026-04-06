---
name: New Relic SLO Compliance Monitor
description: Tracks SLO compliance using the New Relic NerdGraph GraphQL API and NRQL
  queries. Calculates error budgets, burn rates, and generates compliance reports
  with Slack notifications via Incoming Webhooks.
category: "Monitoring &amp; Alerts"
framework: ChatGPT Agents
verification: security_reviewed
source: "https://agentskillexchange.com/skills/new-relic-slo-compliance-monitor/"
---
# New Relic SLO Compliance Monitor

Tracks SLO compliance using the New Relic NerdGraph GraphQL API and NRQL queries. Calculates error budgets, burn rates, and generates compliance reports with Slack notifications via Incoming Webhooks.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/new-relic-slo-compliance-monitor/)
