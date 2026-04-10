---
title: "CircleCI Orb Pipeline Composer"
description: "Composes multi-stage CircleCI pipelines using reusable Orbs and the CircleCI v2 API. Supports dynamic config generation with setup workflows and pipeline parameters for monorepo deployments."
slug: "circleci-orb-pipeline-composer-2"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/circleci-orb-pipeline-composer-2/"
---

# CircleCI Orb Pipeline Composer

Composes multi-stage CircleCI pipelines using reusable Orbs and the CircleCI v2 API. Supports dynamic config generation with setup workflows and pipeline parameters for monorepo deployments.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install circleci-orb-pipeline-composer-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The CircleCI Orb Pipeline Composer skill generates optimized CircleCI pipeline configurations by leveraging the CircleCI v2 API and the Orb registry. It creates multi-stage workflows that compose reusable Orbs for common tasks like Docker image building (circleci/docker), AWS deployments (circleci/aws-cli), and Kubernetes rollouts (circleci/kubernetes). The skill supports dynamic configuration through setup workflows, enabling monorepo projects to selectively trigger downstream pipelines based on changed paths using the path-filtering orb. It configures pipeline parameters for environment-specific builds, implements workspace persistence between jobs, and sets up approval gates for production deployments. The composer validates configurations against the CircleCI config schema, checks Orb version compatibility, and generates pipeline parameter maps for API-triggered runs via the CircleCI Pipeline Trigger API endpoint.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-pipeline-composer-2/)
