---
title: CircleCI Workflow Cost Auditor
description: This skill authenticates with the CircleCI API v2 (circleci.com/api/v2)
  using a personal API token and fetches workflow run metrics via the Insights endpoint.
  It correlates job names, executor resource classes, and durations to compute estimated
  spend using CircleCI published credit rates. Machine, Docker, and Windows executors
  are all analyzed separately. The skill queries the pipeline parameters API to identify
  branches with unusually high trigger frequency and flags them for throttling. A
  full cost-by-project breakdown is generated in Markdown and optionally exported
  as a CSV artifact via the CircleCI Artifacts API. Supports org-level audit across
  multiple projects using the CircleCI organization pipeline list endpoint.
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

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-workflow-cost-auditor/)
