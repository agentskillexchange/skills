---
title: GitLab CI Pipeline Migrator
description: Converts GitLab CI .gitlab-ci.yml pipelines to GitHub Actions workflows
  using the gitlab-ci-local parser and YAML AST transformations. Maps GitLab stages,
  services, and artifacts to equivalent GitHub Actions syntax.
verification: security_reviewed
source: https://github.com/gitlabhq/gitlabhq
category:
- CI/CD Integrations
framework:
- Claude Code
tool_ecosystem:
  github_repo: gitlabhq/gitlabhq
  github_stars: 24298
---

# GitLab CI Pipeline Migrator

Converts GitLab CI .gitlab-ci.yml pipelines to GitHub Actions workflows using the gitlab-ci-local parser and YAML AST transformations. Maps GitLab stages, services, and artifacts to equivalent GitHub Actions syntax.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/gitlab-ci-pipeline-migrator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gitlab-ci-pipeline-migrator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/gitlab-ci-pipeline-migrator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-pipeline-migrator/)
