---
title: GitLab CI Pipeline Debugger
description: Debugs failed GitLab CI/CD pipelines by parsing .gitlab-ci.yml and fetching
  job logs via GitLab REST API v4. Identifies runner misconfigurations, artifact dependency
  issues, and suggests targeted fixes.
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

# GitLab CI Pipeline Debugger

Debugs failed GitLab CI/CD pipelines by parsing .gitlab-ci.yml and fetching job logs via GitLab REST API v4. Identifies runner misconfigurations, artifact dependency issues, and suggests targeted fixes.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/gitlab-ci-pipeline-debugger/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gitlab-ci-pipeline-debugger
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/gitlab-ci-pipeline-debugger`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-pipeline-debugger/)
