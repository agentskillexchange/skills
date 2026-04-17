---
name: GitLab Pipeline DAG Optimizer
description: Analyzes GitLab CI/CD pipeline YAML using the GitLab Pipelines API to
  detect bottlenecks and restructure directed acyclic graph (DAG) dependencies. Integrates
  with gitlab-runner exec and the Merge Request Approvals API for automated gate checks.
category: CI/CD Integrations
framework: OpenClaw
verification: security_reviewed
source: https://github.com/gitlabhq/gitlabhq
tool_ecosystem:
  github_repo: gitlabhq/gitlabhq
  github_stars: 24298
  tool: gitlabhq
  maintained: true
---
# GitLab Pipeline DAG Optimizer
Analyzes GitLab CI/CD pipeline YAML using the GitLab Pipelines API to detect bottlenecks and restructure directed acyclic graph (DAG) dependencies. Integrates with gitlab-runner exec and the Merge Request Approvals API for automated gate checks.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gitlab-pipeline-dag-optimizer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/gitlab-pipeline-dag-optimizer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-pipeline-dag-optimizer/)
