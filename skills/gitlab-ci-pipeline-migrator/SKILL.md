---
title: GitLab CI Pipeline Migrator
description: 'The GitLab CI Pipeline Migrator skill automates the conversion of GitLab
  CI/CD pipeline configurations to GitHub Actions workflow format. It uses the gitlab-ci-local
  parser to fully resolve .gitlab-ci.yml files including extends, anchors, and include
  directives. The migration engine maps GitLab CI concepts to GitHub Actions equivalents:
  stages become job dependency chains with needs keywords, services become service
  containers, artifacts become upload/download-artifact actions, and cache configurations
  become actions/cache entries with matching key patterns. YAML AST transformations
  preserve comments and formatting where possible, using the yaml library CST parser
  for structure-aware modifications. The skill handles complex GitLab features including
  DAG pipelines, parallel matrix jobs, rules-based conditional execution, and multi-project
  pipeline triggers. Variable mapping converts GitLab CI predefined variables (CI_COMMIT_SHA,
  CI_PIPELINE_ID) to GitHub Actions equivalents (github.sha, github.run_id). The migrator
  generates a compatibility report identifying features that require manual intervention,
  such as GitLab-specific API integrations and container registry authentication differences.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/gitlab-ci-pipeline-migrator/
category:
- CI/CD Integrations
framework:
- Claude Code
---

# GitLab CI Pipeline Migrator

The GitLab CI Pipeline Migrator skill automates the conversion of GitLab CI/CD pipeline configurations to GitHub Actions workflow format. It uses the gitlab-ci-local parser to fully resolve .gitlab-ci.yml files including extends, anchors, and include directives. The migration engine maps GitLab CI concepts to GitHub Actions equivalents: stages become job dependency chains with needs keywords, services become service containers, artifacts become upload/download-artifact actions, and cache configurations become actions/cache entries with matching key patterns. YAML AST transformations preserve comments and formatting where possible, using the yaml library CST parser for structure-aware modifications. The skill handles complex GitLab features including DAG pipelines, parallel matrix jobs, rules-based conditional execution, and multi-project pipeline triggers. Variable mapping converts GitLab CI predefined variables (CI_COMMIT_SHA, CI_PIPELINE_ID) to GitHub Actions equivalents (github.sha, github.run_id). The migrator generates a compatibility report identifying features that require manual intervention, such as GitLab-specific API integrations and container registry authentication differences.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-pipeline-migrator/)
