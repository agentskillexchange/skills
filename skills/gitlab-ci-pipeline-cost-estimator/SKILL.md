---
title: "GitLab CI Pipeline Cost Estimator"
description: "Estimates CI/CD pipeline costs by querying the GitLab REST API v4 for job durations, runner types, and compute minutes. Maps shared vs self-hosted runner usage against GitLab pricing tiers."
verification: security_reviewed
source: "https://github.com/gitlabhq/gitlabhq"
category:
  - "CI/CD Integrations"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "gitlabhq/gitlabhq"
  github_stars: 24298
---

# GitLab CI Pipeline Cost Estimator

Estimates CI/CD pipeline costs by querying the GitLab REST API v4 for job durations, runner types, and compute minutes. Maps shared vs self-hosted runner usage against GitLab pricing tiers.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gitlab-ci-pipeline-cost-estimator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/gitlab-ci-pipeline-cost-estimator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-pipeline-cost-estimator/)
