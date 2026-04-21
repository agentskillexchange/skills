---
title: "Helm Chart Diff &amp; Upgrade Manager"
slug: "helm-chart-diff-upgrade-manager"
description: "Uses helm-diff to compute a human-readable diff between deployed and candidate chart versions before upgrade. Automatically bumps image tags by querying the OCI registry, then executes helm upgrade &#8211;atomic with configurable rollback timeouts. Sends upgrade status to PagerDuty or Datadog."
verification: security_reviewed
source: "https://github.com/helm/helm"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "helm/helm"
  github_stars: 29693
---

# Helm Chart Diff &amp; Upgrade Manager

Uses helm-diff to compute a human-readable diff between deployed and candidate chart versions before upgrade. Automatically bumps image tags by querying the OCI registry, then executes helm upgrade &#8211;atomic with configurable rollback timeouts. Sends upgrade status to PagerDuty or Datadog.

## Installation

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/helm-chart-diff-upgrade-manager/)
