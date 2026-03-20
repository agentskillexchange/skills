---
name: CircleCI Workflow Cost Auditor
description: Audits CircleCI workflow spend using the CircleCI Insights API and machine-type pricing tables. Identifies jobs running on oversized resource classes and recommends downgrades using historical CPU/memory utilization from the pipeline telemetry endpoint. Produces a cost breakdown by project, branch, and executor type.
category: CI/CD Integrations
framework: Any Agent
verification: security_reviewed
rating: 4.6
reviews: 11
source: https://agentskillexchange.com/skill/circleci-workflow-cost-auditor/
---

# CircleCI Workflow Cost Auditor

Audits CircleCI workflow spend using the CircleCI Insights API and machine-type pricing tables. Identifies jobs running on oversized resource classes and recommends downgrades using historical CPU/memory utilization from the pipeline telemetry endpoint. Produces a cost breakdown by project, branch, and executor type.

## Overview

Audits CircleCI workflow spend using the CircleCI Insights API and machine-type pricing tables. Identifies jobs running on oversized resource classes and recommends downgrades using historical CPU/memory utilization from the pipeline telemetry endpoint. Produces a cost breakdown by project, branch, and executor type.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill circleci-workflow-cost-auditor
```

### OpenClaw

```bash
clawhub install circleci-workflow-cost-auditor
```

### Claude Code

```bash
claude mcp add circleci-workflow-cost-auditor
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/circleci-workflow-cost-auditor/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: CI/CD Integrations
- **Framework**: Any Agent
- **Rating**: 4.6/5 (11 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/circleci-workflow-cost-auditor/)
