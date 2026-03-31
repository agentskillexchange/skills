---
name: "Prometheus AlertManager Router"
description: "Configures and manages Prometheus AlertManager routing trees and silences via the AlertManager HTTP API. Supports PagerDuty, OpsGenie, and Slack receiver configuration with inhibition rules."
category: "Monitoring &amp; Alerts"
framework: "Cursor"
verification: security_reviewed
source: "https://github.com/prometheus/prometheus"
tool_ecosystem:
  tool: prometheus
  github_repo: prometheus/prometheus
  github_stars: 63306
  license: Apache-2.0
  maintained: true
---
# Prometheus AlertManager Router

Configures and manages Prometheus AlertManager routing trees and silences via the AlertManager HTTP API. Supports PagerDuty, OpsGenie, and Slack receiver configuration with inhibition rules.

## Overview

The Prometheus AlertManager Router skill provides intelligent alert routing and management through the AlertManager HTTP API. It enables agents to programmatically create, modify, and debug complex routing trees that determine how alerts flow from Prometheus to notification receivers like PagerDuty, OpsGenie, Slack, and email.

Key features include routing tree visualization and validation before applying changes, automatic silence creation during maintenance windows with scheduled expiry, and inhibition rule management to suppress dependent alerts when root-cause alerts are already firing. The skill can analyze alert group patterns to suggest routing optimizations.

It supports match and match_re label-based routing, continue flags for multi-receiver fan-out, group_by/group_wait/group_interval tuning for alert batching, and receiver template customization using Go template syntax. Integration with Prometheus's /api/v1/rules endpoint enables correlation between recording rules, alerting rules, and their AlertManager routing destinations for end-to-end observability pipeline verification.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-router
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-router -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-router -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-router -a codex
```

### OpenClaw

```bash
clawhub install prometheus-alertmanager-router
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-router/)
