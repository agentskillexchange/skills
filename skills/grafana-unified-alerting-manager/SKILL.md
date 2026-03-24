---
name: "Grafana Unified Alerting Manager"
description: "Manages Grafana Unified Alerting rules, contact points, and notification policies via the Grafana HTTP API. Supports alert rule provisioning and silence management across multiple Grafana instances."
category: "Monitoring & Alerts"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/grafana-unified-alerting-manager/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "grafana"  # from ase_tool_match
  github_stars: 72784  # from ase_github_stars (integer, not string)
  github_repo: "grafana/grafana"  # from ase_github_repo
  license: "AGPL-3.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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
