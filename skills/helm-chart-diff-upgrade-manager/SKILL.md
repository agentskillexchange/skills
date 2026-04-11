---
title: "Helm Chart Diff & Upgrade Manager"
slug: "helm-chart-diff-upgrade-manager"
description: "Uses helm-diff to compute a human-readable diff between deployed and candidate chart versions before upgrade. Automatically bumps image tags by querying the OCI registry, then executes helm upgrade –atomic with configurable rollback timeouts. Sends upgrade status to PagerDuty or Datadog."
category: "CI/CD Integrations"
framework: "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/helm-chart-diff-upgrade-manager/"
---

# Helm Chart Diff & Upgrade Manager

Uses helm-diff to compute a human-readable diff between deployed and candidate chart versions before upgrade. Automatically bumps image tags by querying the OCI registry, then executes helm upgrade –atomic with configurable rollback timeouts. Sends upgrade status to PagerDuty or Datadog.

## Installation

Choose the setup path that fits your environment:

1. Clone or download this skill into your skills directory.
2. Install it through your agent platform's skill manager if supported.
3. Add it as a Git submodule or vendored folder in your repo.
4. Copy the files into a local custom skills/workspace directory.
5. Pull it from the Agent Skill Exchange catalog or this GitHub repo.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/helm-chart-diff-upgrade-manager/)
