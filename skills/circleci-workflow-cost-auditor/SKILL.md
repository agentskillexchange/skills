---
title: "CircleCI Workflow Cost Auditor"
description: "This skill authenticates with the CircleCI API v2 (circleci.com/api/v2) using a personal API token and fetches workflow run metrics via the Insights endpoint. It correlates job names, executor resource classes, and durations to compute estimated spend using CircleCI published credit rates. Machine, Docker, and Windows executors are all analyzed separately. The skill queries the pipeline parameters API to identify branches with unusually high trigger frequency and flags them for throttling. A full cost-by-project breakdown is generated in Markdown and optionally exported as a CSV artifact via the CircleCI Artifacts API. Supports org-level audit across multiple projects using the CircleCI organization pipeline list endpoint."
source: "https://github.com/circleci/circleci-docs"
verification: "security_reviewed"
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

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-workflow-cost-auditor/)
