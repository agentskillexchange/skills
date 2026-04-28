---
title: GitLab CI Pipeline Cost Estimator
description: Estimates CI/CD pipeline costs by querying the GitLab REST API v4 for
  job durations, runner types, and compute minutes. Maps shared vs self-hosted runner
  usage against GitLab pricing tiers.
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

# GitLab CI Pipeline Cost Estimator

Estimates CI/CD pipeline costs by querying the GitLab REST API v4 for job durations, runner types, and compute minutes. Maps shared vs self-hosted runner usage against GitLab pricing tiers.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/gitlab-ci-pipeline-cost-estimator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gitlab-ci-pipeline-cost-estimator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/gitlab-ci-pipeline-cost-estimator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-pipeline-cost-estimator/)
