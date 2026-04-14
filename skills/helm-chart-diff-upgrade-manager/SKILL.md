---
title: "Helm Chart Diff & Upgrade Manager"
description: "Uses helm-diff to compute a human-readable diff between deployed and candidate chart versions before upgrade. Automatically bumps image tags by querying the OCI registry, then executes helm upgrade &#8211;atomic with configurable rollback timeouts. Sends upgrade status to PagerDuty or Datadog."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/helm-chart-diff-upgrade-manager/"
category:
  - "CI/CD Integrations"
framework:
  - "MCP"
---
# Helm Chart Diff & Upgrade Manager

Uses helm-diff to compute a human-readable diff between deployed and candidate chart versions before upgrade. Automatically bumps image tags by querying the OCI registry, then executes helm upgrade &#8211;atomic with configurable rollback timeouts. Sends upgrade status to PagerDuty or Datadog.

## Installation

You can install this skill in a few common ways:

1. Browse and install from Agent Skill Exchange in the UI if your client supports it.
2. Install from a local skill folder by copying it into your skills directory.
3. Add it as a git submodule or vendor it into your shared skills repo.
4. Fetch it with your preferred skill or package workflow if the upstream project publishes one.
5. Follow the upstream project documentation for manual setup and dependencies.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/helm-chart-diff-upgrade-manager/)
