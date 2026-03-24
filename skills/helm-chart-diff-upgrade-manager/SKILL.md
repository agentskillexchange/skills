---
name: "Helm Chart Diff & Upgrade Manager"
description: "Uses helm-diff to compute a human-readable diff between deployed and candidate chart versions before upgrade. Automatically bumps image tags by querying the OCI registry, then executes helm upgrade –atomic with configurable rollback timeouts. Sends upgrade status to PagerDuty or Datadog."
category: "CI/CD Integrations"
framework: "MCP-compatible"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/helm-chart-diff-upgrade-manager/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "helm"  # from ase_tool_match
  github_stars: 29603  # from ase_github_stars (integer, not string)
  github_repo: "helm/helm"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Helm Chart Diff & Upgrade Manager

Uses helm-diff to compute a human-readable diff between deployed and candidate chart versions before upgrade. Automatically bumps image tags by querying the OCI registry, then executes helm upgrade –atomic with configurable rollback timeouts. Sends upgrade status to PagerDuty or Datadog.

## Overview

Uses helm-diff to compute a human-readable diff between deployed and candidate chart versions before upgrade. Automatically bumps image tags by querying the OCI registry, then executes helm upgrade –atomic with configurable rollback timeouts. Sends upgrade status to PagerDuty or Datadog.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill helm-chart-diff-upgrade-manager
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill helm-chart-diff-upgrade-manager -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill helm-chart-diff-upgrade-manager -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill helm-chart-diff-upgrade-manager -a codex
```

### OpenClaw

```bash
clawhub install helm-chart-diff-upgrade-manager
```

## Source

- Marketplace: https://agentskillexchange.com/skills/helm-chart-diff-upgrade-manager/
