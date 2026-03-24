---
name: "CircleCI Workflow Cost Auditor"
description: "Audits CircleCI workflow spend using the CircleCI Insights API and machine-type pricing tables. Identifies jobs running on oversized resource classes and recommends downgrades using historical CPU/memory utilization from the pipeline telemetry endpoint. Produces a cost breakdown by project, branch, and executor type."
category: "CI/CD Integrations"
framework: "OpenClaw"
verification: security_reviewed
rating: 4.6
reviews: 11
creator: "Yuki Tanaka"
creator_handle: "@yukitanaka"
creator_verified: true
source: "https://agentskillexchange.com/skills/circleci-workflow-cost-auditor/"
---
# CircleCI Workflow Cost Auditor

Audits CircleCI workflow spend using the CircleCI Insights API and machine-type pricing tables. Identifies jobs running on oversized resource classes and recommends downgrades using historical CPU/memory utilization from the pipeline telemetry endpoint. Produces a cost breakdown by project, branch, and executor type.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill circleci-workflow-cost-auditor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill circleci-workflow-cost-auditor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill circleci-workflow-cost-auditor -a cursor
```

### OpenClaw

```bash
clawhub install circleci-workflow-cost-auditor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill circleci-workflow-cost-auditor -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | CI/CD Integrations |
| Framework | OpenClaw |
| Verification | Security Reviewed |
| Rating | 4.6/5 (11 reviews) |

## Creator

**Yuki Tanaka** (Verified Creator ✓)
- Profile: [@yukitanaka](https://agentskillexchange.com/browse-skills/?creator=yukitanaka)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/circleci-workflow-cost-auditor/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
