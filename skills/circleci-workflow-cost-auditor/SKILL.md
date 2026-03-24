---
name: "CircleCI Workflow Cost Auditor"
description: "Audits CircleCI workflow spend using the CircleCI Insights API and machine-type pricing tables. Identifies jobs running on oversized resource classes and recommends downgrades using historical CPU/memory utilization from the pipeline telemetry endpoint. Produces a cost breakdown by project, branch, and executor type."
category: "CI/CD Integrations"
framework: "OpenClaw"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/circleci-workflow-cost-auditor/"
tool_ecosystem:
  tool: "circleci"
  github_stars: 842
  npm_weekly_downloads: 0
  github_repo: "circleci/circleci-docs"
  license: "Unknown"
  maintained: true
---

# CircleCI Workflow Cost Auditor

Audits CircleCI workflow spend using the CircleCI Insights API and machine-type pricing tables. Identifies jobs running on oversized resource classes and recommends downgrades using historical CPU/memory utilization from the pipeline telemetry endpoint. Produces a cost breakdown by project, branch, and executor type.

## Installation

### Any Agent (npx)
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

| | |
|---|---|
| **Category** | CI/CD Integrations |
| **Framework** | OpenClaw |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [circleci](https://github.com/circleci/circleci-docs) — ⭐ 842 · Unknown |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-workflow-cost-auditor/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
