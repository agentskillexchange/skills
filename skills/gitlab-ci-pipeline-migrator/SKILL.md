---
title: "GitLab CI Pipeline Migrator"
description: "The GitLab CI Pipeline Migrator skill automates the conversion of GitLab CI/CD pipeline configurations to GitHub Actions workflow format. It uses the gitlab-ci-local parser to fully resolve .gitlab-ci.yml files including extends, anchors, and include directives. The migration engine maps GitLab CI concepts to GitHub Actions equivalents: stages become job dependency chains with needs keywords, services become service containers, artifacts become upload/download-artifact actions, and cache configurations become actions/cache entries with matching key patterns. YAML AST transformations preserve comments and formatting where possible, using the yaml library CST parser for structure-aware modifications. The skill handles complex GitLab features including DAG pipelines, parallel matrix jobs, rules-based conditional execution, and multi-project pipeline triggers. Variable mapping converts GitLab CI predefined variables (CI_COMMIT_SHA, CI_PIPELINE_ID) to GitHub Actions equivalents (github.sha, github.run_id). The migrator generates a compatibility report identifying features that require manual intervention, such as GitLab-specific API integrations and container registry authentication differences."
source: "https://github.com/gitlabhq/gitlabhq"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "gitlabhq/gitlabhq"
  github_stars: 24298
---

# GitLab CI Pipeline Migrator

The GitLab CI Pipeline Migrator skill automates the conversion of GitLab CI/CD pipeline configurations to GitHub Actions workflow format. It uses the gitlab-ci-local parser to fully resolve .gitlab-ci.yml files including extends, anchors, and include directives. The migration engine maps GitLab CI concepts to GitHub Actions equivalents: stages become job dependency chains with needs keywords, services become service containers, artifacts become upload/download-artifact actions, and cache configurations become actions/cache entries with matching key patterns. YAML AST transformations preserve comments and formatting where possible, using the yaml library CST parser for structure-aware modifications. The skill handles complex GitLab features including DAG pipelines, parallel matrix jobs, rules-based conditional execution, and multi-project pipeline triggers. Variable mapping converts GitLab CI predefined variables (CI_COMMIT_SHA, CI_PIPELINE_ID) to GitHub Actions equivalents (github.sha, github.run_id). The migrator generates a compatibility report identifying features that require manual intervention, such as GitLab-specific API integrations and container registry authentication differences.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-pipeline-migrator/)
