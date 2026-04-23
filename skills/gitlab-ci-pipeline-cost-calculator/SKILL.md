---
title: "GitLab CI Pipeline Cost Calculator"
description: "Calculates CI/CD spend using the GitLab REST API v4 pipelines and jobs endpoints. Tracks runner minutes by project, estimates cost per pipeline via GitLab compute minute pricing, and identifies expensive jobs for optimization."
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

# GitLab CI Pipeline Cost Calculator

Calculates CI/CD spend using the GitLab REST API v4 pipelines and jobs endpoints. Tracks runner minutes by project, estimates cost per pipeline via GitLab compute minute pricing, and identifies expensive jobs for optimization.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/gitlab-ci-pipeline-cost-calculator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gitlab-ci-pipeline-cost-calculator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/gitlab-ci-pipeline-cost-calculator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-pipeline-cost-calculator/)
