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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-pipeline-composer-2/)
