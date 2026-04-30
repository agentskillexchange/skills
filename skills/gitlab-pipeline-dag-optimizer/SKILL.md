---
title: "GitLab Pipeline DAG Optimizer"
description: "Analyzes GitLab CI/CD pipeline YAML using the GitLab Pipelines API to detect bottlenecks and restructure directed acyclic graph (DAG) dependencies. Integrates with gitlab-runner exec and the Merge Request Approvals API for automated gate checks."
verification: "security_reviewed"
source: "https://github.com/gitlabhq/gitlabhq"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "gitlabhq/gitlabhq"
  github_stars: 24298
---

# GitLab Pipeline DAG Optimizer

Analyzes GitLab CI/CD pipeline YAML using the GitLab Pipelines API to detect bottlenecks and restructure directed acyclic graph (DAG) dependencies. Integrates with gitlab-runner exec and the Merge Request Approvals API for automated gate checks.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-pipeline-dag-optimizer/)
