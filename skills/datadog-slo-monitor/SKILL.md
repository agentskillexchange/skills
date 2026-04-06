---
name: "Datadog SLO Monitor"
description: "Monitors Datadog Service Level Objectives and burn rate alerts via the Datadog API v2. Generates SLO compliance reports and triggers remediation workflows when error budgets are exhausted."
category: "Monitoring & Alerts"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/datadog-slo-monitor/"
---
# Datadog SLO Monitor

Monitors Datadog Service Level Objectives and burn rate alerts via the Datadog API v2. Generates SLO compliance reports and triggers remediation workflows when error budgets are exhausted.

The Datadog SLO Monitor skill continuously tracks Service Level Objectives defined in Datadog using the SLO API v2 endpoints. It calculates real-time burn rates across 5-minute, 1-hour, and 30-day windows to detect fast-burn and slow-burn scenarios. When error budgets approach exhaustion thresholds, the skill triggers configurable remediation workflows including automated rollbacks via deployment APIs, traffic shifting through load balancer configurations, and team notifications via Datadog Events. Features include SLO history export to CSV for compliance reporting, multi-SLO dashboard generation using Datadog Dashboards API, and integration with Datadog Monitors API for creating composite alert conditions. Supports custom burn rate alerting rules and weekly SLO digest summaries sent via email or Slack.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill datadog-slo-monitor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill datadog-slo-monitor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill datadog-slo-monitor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill datadog-slo-monitor -a codex
```

### OpenClaw

```bash
clawhub install datadog-slo-monitor
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-slo-monitor/)
