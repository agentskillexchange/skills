---
name: GitLab CI Pipeline Dependency Tracer
description: Traces job dependency chains in GitLab CI pipelines using the GitLab
  Jobs API and pipeline graph endpoints. Detects bottleneck stages that block parallel
  execution and suggests DAG refactoring. Integrates with the GitLab Merge Requests
  API to post optimization reports as MR comments.
category: CI/CD Integrations
framework: Codex
verification: security_reviewed
source: https://github.com/gitlabhq/gitlabhq
tool_ecosystem:
  github_repo: gitlabhq/gitlabhq
  github_stars: 24298
  tool: gitlabhq
  maintained: true
---
# GitLab CI Pipeline Dependency Tracer
Traces job dependency chains in GitLab CI pipelines using the GitLab Jobs API and pipeline graph endpoints. Detects bottleneck stages that block parallel execution and suggests DAG refactoring. Integrates with the GitLab Merge Requests API to post optimization reports as MR comments.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gitlab-ci-pipeline-dependency-tracer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/gitlab-ci-pipeline-dependency-tracer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-pipeline-dependency-tracer/)
