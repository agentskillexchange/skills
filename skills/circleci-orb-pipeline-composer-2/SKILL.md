---
title: "CircleCI Orb Pipeline Composer"
description: "Composes multi-stage CircleCI pipelines using reusable Orbs and the CircleCI v2 API. Supports dynamic config generation with setup workflows and pipeline parameters for monorepo deployments."
verification: "security_reviewed"
source: "https://github.com/circleci/circleci-docs"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "circleci/circleci-docs"
  github_stars: 843
---

# CircleCI Orb Pipeline Composer

The CircleCI Orb Pipeline Composer skill generates optimized CircleCI pipeline configurations by leveraging the CircleCI v2 API and the Orb registry. It creates multi-stage workflows that compose reusable Orbs for common tasks like Docker image building (circleci/docker), AWS deployments (circleci/aws-cli), and Kubernetes rollouts (circleci/kubernetes). The skill supports dynamic configuration through setup workflows, enabling monorepo projects to selectively trigger downstream pipelines based on changed paths using the path-filtering orb. It configures pipeline parameters for environment-specific builds, implements workspace persistence between jobs, and sets up approval gates for production deployments. The composer validates configurations against the CircleCI config schema, checks Orb version compatibility, and generates pipeline parameter maps for API-triggered runs via the CircleCI Pipeline Trigger API endpoint.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/circleci-orb-pipeline-composer-2/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/circleci-orb-pipeline-composer-2
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/circleci-orb-pipeline-composer-2`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-pipeline-composer-2/)
