---
name: CircleCI Workflow Cost Auditor
description: Audits CircleCI workflow spend using the CircleCI Insights API and machine-type
  pricing tables. Identifies jobs running on oversized resource classes and recommends
  downgrades using historical CPU/memory utilization from the pipeline telemetry endpoint.
  Produces a cost breakdown by project, branch, and executor type.
verification: security_reviewed
source: https://agentskillexchange.com/skills/circleci-workflow-cost-auditor/
category:
- CI/CD Integrations
framework:
- OpenClaw
---
# CircleCI Workflow Cost Auditor

This skill authenticates with the CircleCI API v2 (circleci.com/api/v2) using a personal API token and fetches workflow run metrics via the Insights endpoint. It correlates job names, executor resource classes, and durations to compute estimated spend using CircleCI published credit rates. Machine, Docker, and Windows executors are all analyzed separately. The skill queries the pipeline parameters API to identify branches with unusually high trigger frequency and flags them for throttling. A full cost-by-project breakdown is generated in Markdown and optionally exported as a CSV artifact via the CircleCI Artifacts API. Supports org-level audit across multiple projects using the CircleCI organization pipeline list endpoint.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-workflow-cost-auditor/)
