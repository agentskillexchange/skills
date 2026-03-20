---
name: Helm Chart Diff & Upgrade Manager
description: Uses helm-diff to compute a human-readable diff between deployed and candidate chart versions before upgrade. Automatically bumps image tags by querying the OCI registry, then executes helm upgrade --atomic with configurable rollback timeouts. Sends upgrade status to PagerDuty or Datadog.
category: CI/CD Integrations
framework: Any Agent
verification: verified_metadata
rating: 4.7
reviews: 60
source: https://agentskillexchange.com/skill/helm-chart-diff-upgrade-manager/
---

# Helm Chart Diff & Upgrade Manager

Uses helm-diff to compute a human-readable diff between deployed and candidate chart versions before upgrade. Automatically bumps image tags by querying the OCI registry, then executes helm upgrade --atomic with configurable rollback timeouts. Sends upgrade status to PagerDuty or Datadog.

## Overview

Uses helm-diff to compute a human-readable diff between deployed and candidate chart versions before upgrade. Automatically bumps image tags by querying the OCI registry, then executes helm upgrade --atomic with configurable rollback timeouts. Sends upgrade status to PagerDuty or Datadog.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill helm-chart-diff-upgrade-manager
```

### OpenClaw

```bash
clawhub install helm-chart-diff-upgrade-manager
```

### Claude Code

```bash
claude mcp add helm-chart-diff-upgrade-manager
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/helm-chart-diff-upgrade-manager/) for detailed installation instructions.

## Verification

- **Status**: verified_metadata
- **Category**: CI/CD Integrations
- **Framework**: Any Agent
- **Rating**: 4.7/5 (60 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/helm-chart-diff-upgrade-manager/)
