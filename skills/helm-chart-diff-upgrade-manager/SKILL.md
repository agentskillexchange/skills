---
title: "Helm Chart Diff & Upgrade Manager"
slug: "helm-chart-diff-upgrade-manager"
description: "Uses helm-diff to compute a human-readable diff between deployed and candidate chart versions before upgrade. Automatically bumps image tags by querying the OCI registry, then executes helm upgrade –atomic with configurable rollback timeouts. Sends upgrade status to PagerDuty or Datadog."
verification: verified
source: "https://github.com/helm/helm"
category: "CI/CD Integrations"
framework: "MCP"
tool_ecosystem:
  github_repo: "helm/helm"
  github_stars: 29693
---
# Helm Chart Diff &amp; Upgrade Manager

Uses helm-diff to compute a human-readable diff between deployed and candidate chart versions before upgrade. Automatically bumps image tags by querying the OCI registry, then executes helm upgrade &#8211;atomic with configurable rollback timeouts. Sends upgrade status to PagerDuty or Datadog.

## Installation

1. Clone this skill repository.
2. Open this skill folder.
3. Review prerequisites and setup needs.
4. Install required dependencies.
5. Run and test in your environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/helm-chart-diff-upgrade-manager/)
