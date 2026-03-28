---
name: "Grafana Unified Alerting Manager"
description: "Manages Grafana Unified Alerting rules, contact points, and notification policies via the Grafana HTTP API. Supports alert rule provisioning and silence management across multiple Grafana instances."
category: "Monitoring & Alerts"
framework: "Cursor"
verification: security_reviewed
source: "https://github.com/grafana/grafana"
tool_ecosystem:
  tool: grafana
  github_stars: 72796
  github_repo: grafana/grafana
  license: AGPL-3.0
  maintained: true
---

# Grafana Unified Alerting Manager

Manages Grafana Unified Alerting rules, contact points, and notification policies via the Grafana HTTP API. Supports alert rule provisioning and silence management across multiple Grafana instances.

## Overview

The Grafana Unified Alerting Manager skill provides full lifecycle management of alerting configurations across Grafana instances using the Grafana Alerting HTTP API. It creates and updates alert rules with PromQL, LogQL, or SQL expressions, configures contact points for email, Slack, PagerDuty, and webhook receivers, and manages notification policies with label-based routing trees. The skill supports alert rule provisioning via the Provisioning API for GitOps workflows, silence creation and expiry management, and mute timing configurations for maintenance windows. Features include bulk rule import/export in JSON and YAML formats, alert rule testing with sample data evaluation, and cross-instance rule synchronization for high-availability Grafana deployments. Integrates with Grafana OnCall API for escalation chain management.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill grafana-unified-alerting-manager
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill grafana-unified-alerting-manager -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill grafana-unified-alerting-manager -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill grafana-unified-alerting-manager -a codex
```

### OpenClaw

```bash
clawhub install grafana-unified-alerting-manager
```

## Source

- Marketplace: https://agentskillexchange.com/skills/grafana-unified-alerting-manager/
