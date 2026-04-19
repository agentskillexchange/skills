---
title: "GitLab CI Template Generator"
description: "The GitLab CI Template Generator skill produces comprehensive .gitlab-ci.yml configurations leveraging GitLab native CI/CD features and templates. It integrates the Auto DevOps template includes for standardized build-test-deploy stages, uses gcr.io/kaniko-project/executor for rootless container image building without Docker-in-Docker, and configures the SAST and DAST security scanning templates. The skill generates pipeline configurations with proper cache policies using cache:key:files for lock-file-based cache invalidation, artifacts:reports for code quality and test coverage reporting, and rules-based job inclusion replacing the deprecated only/except syntax. It handles environment-specific deployments with environment:url and environment:auto_stop_in for review app lifecycle management. Multi-project pipeline support includes trigger jobs with strategy:depend for downstream pipeline monitoring, bridge jobs for cross-project artifact dependencies, and parent-child pipelines using trigger:include for modular configuration. The skill also configures GitLab Releases API integration for automated release creation with release-cli and generates proper services configurations for integration testing with PostgreSQL, Redis, and Elasticsearch containers."
source: "https://github.com/gitlabhq/gitlabhq"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "gitlabhq/gitlabhq"
  github_stars: 24298
---

# GitLab CI Template Generator

The GitLab CI Template Generator skill produces comprehensive .gitlab-ci.yml configurations leveraging GitLab native CI/CD features and templates. It integrates the Auto DevOps template includes for standardized build-test-deploy stages, uses gcr.io/kaniko-project/executor for rootless container image building without Docker-in-Docker, and configures the SAST and DAST security scanning templates. The skill generates pipeline configurations with proper cache policies using cache:key:files for lock-file-based cache invalidation, artifacts:reports for code quality and test coverage reporting, and rules-based job inclusion replacing the deprecated only/except syntax. It handles environment-specific deployments with environment:url and environment:auto_stop_in for review app lifecycle management. Multi-project pipeline support includes trigger jobs with strategy:depend for downstream pipeline monitoring, bridge jobs for cross-project artifact dependencies, and parent-child pipelines using trigger:include for modular configuration. The skill also configures GitLab Releases API integration for automated release creation with release-cli and generates proper services configurations for integration testing with PostgreSQL, Redis, and Elasticsearch containers.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-template-generator/)
