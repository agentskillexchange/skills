---
title: "Helm Chart Diff & Upgrade Manager"
slug: "helm-chart-diff-upgrade-manager"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/helm-chart-diff-upgrade-manager/"
category:
  - "CI/CD Integrations"
framework:
  - "MCP"
---
# Helm Chart Diff & Upgrade Manager

Uses helm-diff to compute a human-readable diff between deployed and candidate chart versions before upgrade. Automatically bumps image tags by querying the OCI registry, then executes helm upgrade &#8211;atomic with configurable rollback timeouts. Sends upgrade status to PagerDuty or Datadog.

## Installation

Choose the method that fits your setup:

1. Install from Agent Skill Exchange
2. Clone or download the upstream project
3. Install with the upstream package manager
4. Add the skill to your local skills directory
5. Follow the upstream documentation for environment-specific setup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/helm-chart-diff-upgrade-manager/)
