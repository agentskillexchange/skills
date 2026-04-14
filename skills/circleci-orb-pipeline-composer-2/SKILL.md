---
title: "CircleCI Orb Pipeline Composer"
description: "Composes multi-stage CircleCI pipelines using reusable Orbs and the CircleCI v2 API. Supports dynamic config generation with setup workflows and pipeline parameters for monorepo deployments."
verification: security_reviewed
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-pipeline-composer-2/)
