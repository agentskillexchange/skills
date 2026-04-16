---
title: "GitLab CI Template Generator"
description: "Creates GitLab CI/CD pipeline templates using Auto DevOps components, Kaniko for container builds, and SAST/DAST security scanning. Supports multi-project pipelines with trigger and bridge jobs."
verification: "security_reviewed"
source: "https://github.com/gitlabhq/gitlabhq"
category:
  - "CI/CD Integrations"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "gitlabhq/gitlabhq"
  github_stars: 24298
---

# GitLab CI Template Generator

The GitLab CI Template Generator skill produces comprehensive .gitlab-ci.yml configurations leveraging GitLab native CI/CD features and templates. It integrates the Auto DevOps template includes for standardized build-test-deploy stages, uses gcr.io/kaniko-project/executor for rootless container image building without Docker-in-Docker, and configures the SAST and DAST security scanning templates.


The skill generates pipeline configurations with proper cache policies using cache:key:files for lock-file-based cache invalidation, artifacts:reports for code quality and test coverage reporting, and rules-based job inclusion replacing the deprecated only/except syntax. It handles environment-specific deployments with environment:url and environment:auto_stop_in for review app lifecycle management.


Multi-project pipeline support includes trigger jobs with strategy:depend for downstream pipeline monitoring, bridge jobs for cross-project artifact dependencies, and parent-child pipelines using trigger:include for modular configuration. The skill also configures GitLab Releases API integration for automated release creation with release-cli and generates proper services configurations for integration testing with PostgreSQL, Redis, and Elasticsearch containers.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-template-generator/)
