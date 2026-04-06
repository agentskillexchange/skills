---
name: CircleCI Workflow Cost Auditor
description: Audits CircleCI workflow spend using the CircleCI Insights API and machine-type
  pricing tables. Identifies jobs running on oversized resource classes and recommends
  downgrades using historical CPU/memory utilization from the pipeline telemetry endpoint.
  Produces a cost breakdown by project, branch, and executor type.
category: CI/CD Integrations
framework: OpenClaw
verification: security_reviewed
source: "https://agentskillexchange.com/skills/circleci-workflow-cost-auditor/"
---
# CircleCI Workflow Cost Auditor

Audits CircleCI workflow spend using the CircleCI Insights API and machine-type pricing tables. Identifies jobs running on oversized resource classes and recommends downgrades using historical CPU/memory utilization from the pipeline telemetry endpoint. Produces a cost breakdown by project, branch, and executor type.

This skill authenticates with the CircleCI API v2 (circleci.com/api/v2) using a personal API token and fetches workflow run metrics via the Insights endpoint. It correlates job names, executor resource classes, and durations to compute estimated spend using CircleCI published credit rates. Machine, Docker, and Windows executors are all analyzed separately. The skill queries the pipeline parameters API to identify branches with unusually high trigger frequency and flags them for throttling. A full cost-by-project breakdown is generated in Markdown and optionally exported as a CSV artifact via the CircleCI Artifacts API. Supports org-level audit across multiple projects using the CircleCI organization pipeline list endpoint.

## Installation

### Any Agent

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

### Codex

```bash
npx skills add agentskillexchange/skills --skill circleci-workflow-cost-auditor -a codex
```

### OpenClaw

```bash
clawhub install circleci-workflow-cost-auditor
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-workflow-cost-auditor/)
