---
title: "CircleCI Workflow Cost Auditor"
description: "Audits CircleCI workflow spend using the CircleCI Insights API and machine-type pricing tables. Identifies jobs running on oversized resource classes and recommends downgrades using historical CPU/memory utilization from the pipeline telemetry endpoint. Produces a cost breakdown by project, branch, and executor type."
verification: "security_reviewed"
source: "https://github.com/circleci/circleci-docs"
category:
  - "CI/CD Integrations"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "circleci/circleci-docs"
  github_stars: 843
---

# CircleCI Workflow Cost Auditor

This skill authenticates with the CircleCI API v2 (circleci.com/api/v2) using a personal API token and fetches workflow run metrics via the Insights endpoint. It correlates job names, executor resource classes, and durations to compute estimated spend using CircleCI published credit rates. Machine, Docker, and Windows executors are all analyzed separately. The skill queries the pipeline parameters API to identify branches with unusually high trigger frequency and flags them for throttling. A full cost-by-project breakdown is generated in Markdown and optionally exported as a CSV artifact via the CircleCI Artifacts API. Supports org-level audit across multiple projects using the CircleCI organization pipeline list endpoint.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/circleci-workflow-cost-auditor/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/circleci-workflow-cost-auditor
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/circleci-workflow-cost-auditor`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-workflow-cost-auditor/)
