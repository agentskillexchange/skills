---
title: "CircleCI Pipeline Optimizer"
description: "Interfaces with CircleCI API v2 /pipeline and /workflow endpoints to analyze build performance. Identifies slow jobs via timing data, recommends Docker layer caching, and generates optimized .circleci/config.yml with parallelism settings."
verification: security_reviewed
source: "https://github.com/circleci/circleci-docs"
category:
  - "CI/CD Integrations"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "circleci/circleci-docs"
  github_stars: 843
---

# CircleCI Pipeline Optimizer

The CircleCI Pipeline Optimizer connects to the CircleCI API v2 to analyze pipeline performance and identify optimization opportunities. It queries /pipeline/{pipeline-id}/workflow to map workflow structures, then fetches job details via /workflow/{id}/job to extract timing breakdowns for each step. The agent identifies bottlenecks by comparing step durations across recent runs and flagging jobs that consistently exceed expected execution times. It analyzes Docker image pull times and recommends Docker Layer Caching (DLC) for custom images, calculates optimal parallelism values based on test splitting data from circleci tests split, and suggests resource class upgrades where CPU/memory constraints cause slowdowns. The optimizer generates updated .circleci/config.yml configurations with proper orb references, workspace persistence for artifact sharing between jobs, and conditional workflow execution using pipeline parameters and when/unless clauses. It also evaluates cache hit rates and recommends key rotation strategies.

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
