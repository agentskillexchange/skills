---
name: CircleCI Pipeline Optimizer
description: Interfaces with CircleCI API v2 /pipeline and /workflow endpoints to
  analyze build performance. Identifies slow jobs via timing data, recommends Docker
  layer caching, and generates optimized .circleci/config.yml with parallelism settings.
category: CI/CD Integrations
framework: ChatGPT Agents
verification: security_reviewed
source: https://github.com/circleci/circleci-docs
tool_ecosystem:
  github_repo: circleci/circleci-docs
  github_stars: 843
  tool: circleci-docs
  maintained: true
---
# CircleCI Pipeline Optimizer
Interfaces with CircleCI API v2 /pipeline and /workflow endpoints to analyze build performance. Identifies slow jobs via timing data, recommends Docker layer caching, and generates optimized .circleci/config.yml with parallelism settings.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/circleci-pipeline-optimizer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/circleci-pipeline-optimizer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-pipeline-optimizer/)
