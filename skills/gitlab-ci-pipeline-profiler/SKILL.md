---
title: GitLab CI Pipeline Profiler
description: Profiles GitLab CI/CD pipeline execution times using the GitLab REST
  API v4 /projects/:id/pipelines endpoint. Identifies slow jobs, inefficient artifact
  passing, and cache miss patterns across pipeline history.
verification: security_reviewed
source: https://github.com/gitlabhq/gitlabhq
category:
- CI/CD Integrations
framework:
- Custom Agents
tool_ecosystem:
  github_repo: gitlabhq/gitlabhq
  github_stars: 24298
---

# GitLab CI Pipeline Profiler

Profiles GitLab CI/CD pipeline execution times using the GitLab REST API v4 /projects/:id/pipelines endpoint. Identifies slow jobs, inefficient artifact passing, and cache miss patterns across pipeline history.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/gitlab-ci-pipeline-profiler/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gitlab-ci-pipeline-profiler
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/gitlab-ci-pipeline-profiler`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-pipeline-profiler/)
