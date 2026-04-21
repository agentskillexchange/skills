---
title: "CircleCI Workflow Cost Auditor"
slug: "circleci-workflow-cost-auditor"
description: "Audits CircleCI workflow spend using the CircleCI Insights API and machine-type pricing tables. Identifies jobs running on oversized resource classes and recommends downgrades using historical CPU/memory utilization from the pipeline telemetry endpoint. Produces a cost breakdown by project, branch, and executor type."
verification: security_reviewed
source: "https://github.com/circleci/circleci-docs"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "circleci/circleci-docs"
  github_stars: 843
---

# CircleCI Workflow Cost Auditor

Audits CircleCI workflow spend using the CircleCI Insights API and machine-type pricing tables. Identifies jobs running on oversized resource classes and recommends downgrades using historical CPU/memory utilization from the pipeline telemetry endpoint. Produces a cost breakdown by project, branch, and executor type.

## Installation

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-workflow-cost-auditor/)
