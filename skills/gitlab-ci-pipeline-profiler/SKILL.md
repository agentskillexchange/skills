---
name: GitLab CI Pipeline Profiler
description: Profiles GitLab CI/CD pipeline execution times using the GitLab REST
  API v4 /projects/:id/pipelines endpoint. Identifies slow jobs, inefficient artifact
  passing, and cache miss patterns across pipeline history.
category: CI/CD Integrations
framework: Custom Agents
verification: security_reviewed
source: https://github.com/gitlabhq/gitlabhq
tool_ecosystem:
  github_repo: gitlabhq/gitlabhq
  github_stars: 24298
  tool: gitlabhq
  maintained: true
---
# GitLab CI Pipeline Profiler
Profiles GitLab CI/CD pipeline execution times using the GitLab REST API v4 /projects/:id/pipelines endpoint. Identifies slow jobs, inefficient artifact passing, and cache miss patterns across pipeline history.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gitlab-ci-pipeline-profiler
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/gitlab-ci-pipeline-profiler` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-pipeline-profiler/)
