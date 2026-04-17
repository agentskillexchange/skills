---
title: "CircleCI Orb Pipeline Agent"
description: "The CircleCI Orb Pipeline Agent creates and optimizes CircleCI pipelines using config.yml v2.1 syntax, the CircleCI API v2 (circleci.com/api/v2/project, /pipeline, /workflow), and reusable Orbs from the CircleCI Orb Registry. It generates efficient pipeline configurations with proper resource allocation.\nThe agent leverages CircleCI Orbs for common tasks including circleci/node, circleci/python, circleci/docker, circleci/aws-cli, and circleci/kubernetes. It configures orb commands, jobs, and executors with version pinning and vulnerability scanning through orb source inspection.\nTest splitting is optimized via circleci tests split –split-by=timings with historical timing data to balance parallel containers. The agent configures resource_class selection (small, medium, large, xlarge) based on job requirements and cost analysis via the API.\nDynamic configuration through setup workflows enables monorepo path filtering, conditional job execution, and generated config patterns. The agent manages pipeline parameters, contexts for secret management, and scheduled pipeline triggers. Performance optimization includes Docker layer caching, workspace persistence across jobs, and test result aggregation for flaky test detection."
verification: security_reviewed
source: "https://github.com/circleci/circleci-docs"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "circleci/circleci-docs"
  github_stars: 843
---

# CircleCI Orb Pipeline Agent

The CircleCI Orb Pipeline Agent creates and optimizes CircleCI pipelines using config.yml v2.1 syntax, the CircleCI API v2 (circleci.com/api/v2/project, /pipeline, /workflow), and reusable Orbs from the CircleCI Orb Registry. It generates efficient pipeline configurations with proper resource allocation.
The agent leverages CircleCI Orbs for common tasks including circleci/node, circleci/python, circleci/docker, circleci/aws-cli, and circleci/kubernetes. It configures orb commands, jobs, and executors with version pinning and vulnerability scanning through orb source inspection.
Test splitting is optimized via circleci tests split –split-by=timings with historical timing data to balance parallel containers. The agent configures resource_class selection (small, medium, large, xlarge) based on job requirements and cost analysis via the API.
Dynamic configuration through setup workflows enables monorepo path filtering, conditional job execution, and generated config patterns. The agent manages pipeline parameters, contexts for secret management, and scheduled pipeline triggers. Performance optimization includes Docker layer caching, workspace persistence across jobs, and test result aggregation for flaky test detection.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/circleci-orb-pipeline-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/circleci-orb-pipeline-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-pipeline-agent/)
