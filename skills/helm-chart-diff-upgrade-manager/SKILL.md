---
name: "Helm Chart Diff & Upgrade Manager"
slug: "helm-chart-diff-upgrade-manager"
description: "Uses helm-diff to compute a human-readable diff between deployed and candidate chart versions before upgrade. Automatically bumps image tags by querying the OCI registry, then executes helm upgrade --atomic with configurable rollback timeouts. Sends upgrade status to PagerDuty or Datadog."
github_stars: 29693
verification: "security_reviewed"
source: "https://github.com/helm/helm"
category: "CI/CD Integrations"
framework: "MCP"
tool_ecosystem:
  github_repo: "helm/helm"
  github_stars: 29693
---

# Helm Chart Diff & Upgrade Manager

Uses helm-diff to compute a human-readable diff between deployed and candidate chart versions before upgrade. Automatically bumps image tags by querying the OCI registry, then executes helm upgrade --atomic with configurable rollback timeouts. Sends upgrade status to PagerDuty or Datadog.

## Installation

Use the upstream install or setup path that matches your environment:
- [Homebrew](https://brew.sh/) users can use brew install helm.

Basic usage or getting-started notes:
- Find and use [popular software packaged as Helm Charts](https://artifacthub.io/packages/search?kind=0) to run in Kubernetes
- Helm runs on your laptop, CI/CD, or wherever you want it to run.
- Binary downloads of the Helm client can be found on [the Releases page](https://github.com/helm/helm/releases/latest).

- Source: https://github.com/helm/helm
- Extracted from upstream docs: https://raw.githubusercontent.com/helm/helm/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/helm-chart-diff-upgrade-manager/)
