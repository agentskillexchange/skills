---
title: "GitLab CI Pipeline Dependency Tracer"
description: "Traces job dependency chains in GitLab CI pipelines using the GitLab Jobs API and pipeline graph endpoints. Detects bottleneck stages that block parallel execution and suggests DAG refactoring. Integrates with the GitLab Merge Requests API to post optimization reports as MR comments."
verification: "security_reviewed"
source: "https://github.com/gitlabhq/gitlabhq"
category:
  - "CI/CD Integrations"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "gitlabhq/gitlabhq"
  github_stars: 24298
---

# GitLab CI Pipeline Dependency Tracer

Traces job dependency chains in GitLab CI pipelines using the GitLab Jobs API and pipeline graph endpoints. Detects bottleneck stages that block parallel execution and suggests DAG refactoring. Integrates with the GitLab Merge Requests API to post optimization reports as MR comments.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/gitlab-ci-pipeline-dependency-tracer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gitlab-ci-pipeline-dependency-tracer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/gitlab-ci-pipeline-dependency-tracer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-pipeline-dependency-tracer/)
