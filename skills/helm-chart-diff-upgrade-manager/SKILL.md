---
title: "Helm Chart Diff & Upgrade Manager"
description: "Uses helm-diff to compute a human-readable diff between deployed and candidate chart versions before upgrade. Automatically bumps image tags by querying the OCI registry, then executes helm upgrade –atomic with configurable rollback timeouts. Sends upgrade status to PagerDuty or Datadog."
verification: security_reviewed
source: "https://github.com/helm/helm"
category:
  - "CI/CD Integrations"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "helm/helm"
  github_stars: 29693
  license: "Apache-2.0"
---

# Helm Chart Diff & Upgrade Manager

Uses helm-diff to compute a human-readable diff between deployed and candidate chart versions before upgrade. Automatically bumps image tags by querying the OCI registry, then executes helm upgrade –atomic with configurable rollback timeouts. Sends upgrade status to PagerDuty or Datadog.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/helm-chart-diff-upgrade-manager
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/helm-chart-diff-upgrade-manager` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/helm-chart-diff-upgrade-manager/)
