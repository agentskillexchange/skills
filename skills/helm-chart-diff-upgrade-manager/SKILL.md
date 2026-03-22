---
name: "Helm Chart Diff & Upgrade Manager"
description: "Uses helm-diff to compute a human-readable diff between deployed and candidate chart versions before upgrade. Automatically bumps image tags by querying the OCI registry, then executes helm upgrade –atomic with configurable rollback timeouts. Sends upgrade status to PagerDuty or Datadog."
category: "CI/CD Integrations"
framework: "MCP-compatible"
verification: verified_metadata
rating: 4.7
reviews: 60
creator: Yuki Tanaka
creator_handle: yukitanaka
creator_verified: true
source: https://agentskillexchange.com/skill/helm-chart-diff-upgrade-manager/
---

# Helm Chart Diff & Upgrade Manager

Uses helm-diff to compute a human-readable diff between deployed and candidate chart versions before upgrade. Automatically bumps image tags by querying the OCI registry, then executes helm upgrade –atomic with configurable rollback timeouts. Sends upgrade status to PagerDuty or Datadog.

## Installation

### Any agent (npx skills)

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

### OpenClaw

```bash
clawhub install helm-chart-diff-upgrade-manager
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill helm-chart-diff-upgrade-manager -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | CI/CD Integrations |
| Framework | MCP-compatible |
| Verification | Verified Metadata |
| Rating | 4.7/5 (60 reviews) |

## Creator

**Yuki Tanaka** (Verified Creator ✓)
- Profile: [@yukitanaka](https://agentskillexchange.com/browse-skills/?creator=yukitanaka)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/helm-chart-diff-upgrade-manager/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
