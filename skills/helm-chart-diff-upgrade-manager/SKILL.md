---
name: "helm-chart-diff-upgrade-manager"
description: "Uses helm-diff to compute a human-readable diff between deployed and candidate chart versions before upgrade. Automatically bumps image tags by querying the OCI registry, then executes helm upgrade –atomic with configurable rollback timeouts. Sends upgrade status to PagerDuty or Datadog."
category: "CI/CD Integrations"
framework: "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/helm-chart-diff-upgrade-manager/"
---

# Helm Chart Diff & Upgrade Manager

Uses helm-diff to compute a human-readable diff between deployed and candidate chart versions before upgrade. Automatically bumps image tags by querying the OCI registry, then executes helm upgrade –atomic with configurable rollback timeouts. Sends upgrade status to PagerDuty or Datadog.

## Installation

You can install this skill using one of these common methods:

1. **ClawHub** — install from the marketplace if available.
2. **Git clone** — clone the skill folder into your local skills directory.
3. **Download ZIP** — download and extract the skill files manually.
4. **Copy files** — copy the skill directory into your agent skills path.
5. **Package manager / upstream installer** — use the original project installer if the source provides one.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/helm-chart-diff-upgrade-manager/)
