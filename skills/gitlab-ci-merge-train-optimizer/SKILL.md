---
title: "GitLab CI Merge Train Optimizer"
description: "Optimizes GitLab CI/CD merge trains via the GitLab REST API v4 (/api/v4/projects/{id}/merge_trains). Analyzes pipeline durations, identifies bottleneck stages, and recommends DAG-based job dependencies for parallel execution."
verification: security_reviewed
source: "https://github.com/gitlabhq/gitlabhq"
category:
  - "CI/CD Integrations"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "gitlabhq/gitlabhq"
  github_stars: 24298
---

# GitLab CI Merge Train Optimizer

Optimizes GitLab CI/CD merge trains via the GitLab REST API v4 (/api/v4/projects/{id}/merge_trains). Analyzes pipeline durations, identifies bottleneck stages, and recommends DAG-based job dependencies for parallel execution.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gitlab-ci-merge-train-optimizer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/gitlab-ci-merge-train-optimizer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-merge-train-optimizer/)
