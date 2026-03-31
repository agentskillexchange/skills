---
name: "Prometheus AlertManager Bridge"
description: "Connects to Prometheus AlertManager API to query active alerts, silences, and alert groups. Parses PromQL alert rules and suggests runbook actions. Integrates with PagerDuty escalation policies."
category: "Monitoring &amp; Alerts"
framework: "OpenClaw"
verification: security_reviewed
source: "https://github.com/prometheus/prometheus"
tool_ecosystem:
  tool: prometheus
  github_repo: prometheus/prometheus
  github_stars: 63306
  license: Apache-2.0
  maintained: true
---
# Prometheus AlertManager Bridge

Connects to Prometheus AlertManager API to query active alerts, silences, and alert groups. Parses PromQL alert rules and suggests runbook actions. Integrates with PagerDuty escalation policies.

## Overview

The Prometheus AlertManager Bridge skill gives Claude direct access to your Prometheus AlertManager instance through its REST API (v2). It queries active alerts, manages silences, and retrieves alert group information for incident triage workflows.

When alerts fire, the skill retrieves full alert details including labels, annotations, generator URLs, and current status (firing, pending, resolved). It parses the underlying PromQL expressions from alert rules to explain what conditions triggered the alert in plain language.

The skill supports creating and expiring silences — useful for planned maintenance windows or acknowledged issues. It validates silence matchers against active alerts to confirm coverage. Alert group queries help identify correlated failures across services.

Integration with PagerDuty is built in: the skill reads escalation policies and on-call schedules to identify the right responder. It can acknowledge or resolve PagerDuty incidents and add notes with diagnostic findings. The skill also suggests runbook actions based on alert labels, matching against a configurable runbook directory for automated remediation steps. Designed for SRE teams managing Kubernetes clusters and microservice architectures.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-bridge
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-bridge -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-bridge -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-bridge -a codex
```

### OpenClaw

```bash
clawhub install prometheus-alertmanager-bridge
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-bridge/)
