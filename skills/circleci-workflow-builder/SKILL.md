---
title: "CircleCI Workflow Builder"
description: "Generates CircleCI config.yml workflows using the CircleCI Orbs SDK and Workflows API. Supports parallelism tuning with the CircleCI Test Splitting API and resource class optimization for Docker and machine executors."
verification: "security_reviewed"
source: "https://github.com/circleci/circleci-docs"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "circleci/circleci-docs"
  github_stars: 843
---

# CircleCI Workflow Builder

The CircleCI Workflow Builder skill automates the creation and optimization of CircleCI configuration files. It uses the CircleCI Orbs SDK to compose reusable configuration packages for common build patterns including Node.js, Python, Go, and Rust projects. The skill leverages the CircleCI Workflows API to design complex workflow graphs with fan-out/fan-in patterns, conditional execution using pipeline parameters, and scheduled triggers via cron expressions. Test splitting is optimized through the CircleCI Test Splitting API, distributing test suites across parallel containers based on timing data from previous runs. The skill configures appropriate resource classes for each job, balancing cost against build speed. It supports Docker layer caching, workspace persistence between jobs, and matrix job generation for cross-platform testing. Advanced features include dynamic configuration using setup workflows, custom orb development, and integration with CircleCI Insights API for build performance analytics.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-workflow-builder/)
