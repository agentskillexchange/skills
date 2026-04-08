---
title: "Helm Chart Diff & Upgrade Manager"
slug: "helm-chart-diff-upgrade-manager"
description: "Uses helm-diff to compute a human-readable diff between deployed and candidate chart versions before upgrade. Automatically bumps image tags by querying the OCI registry, then executes helm upgrade -atomic with configurable rollback timeouts. Sends upgrade status to PagerDuty or Datadog."
category:
  - "CI/CD Integrations"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/helm-chart-diff-upgrade-manager/"
---

# Helm Chart Diff & Upgrade Manager

Uses helm-diff to compute a human-readable diff between deployed and candidate chart versions before upgrade. Automatically bumps image tags by querying the OCI registry, then executes helm upgrade -atomic with configurable rollback timeouts. Sends upgrade status to PagerDuty or Datadog.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange catalog in your compatible client.
2. Clone or download this repository and copy the skill folder into your local skills directory.
3. Add it as a git submodule inside your skills collection.
4. Use a package or automation workflow that syncs skills from this repository.
5. Install directly from the original upstream project if you prefer to track source releases.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/helm-chart-diff-upgrade-manager/)
