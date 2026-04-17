---
title: "GitLab CI Pipeline Migrator"
description: "The GitLab CI Pipeline Migrator skill automates the conversion of GitLab CI/CD pipeline configurations to GitHub Actions workflow format. It uses the gitlab-ci-local parser to fully resolve .gitlab-ci.yml files including extends, anchors, and include directives.\nThe migration engine maps GitLab CI concepts to GitHub Actions equivalents: stages become job dependency chains with needs keywords, services become service containers, artifacts become upload/download-artifact actions, and cache configurations become actions/cache entries with matching key patterns.\nYAML AST transformations preserve comments and formatting where possible, using the yaml library CST parser for structure-aware modifications. The skill handles complex GitLab features including DAG pipelines, parallel matrix jobs, rules-based conditional execution, and multi-project pipeline triggers.\nVariable mapping converts GitLab CI predefined variables (CI_COMMIT_SHA, CI_PIPELINE_ID) to GitHub Actions equivalents (github.sha, github.run_id). The migrator generates a compatibility report identifying features that require manual intervention, such as GitLab-specific API integrations and container registry authentication differences."
verification: security_reviewed
source: "https://github.com/gitlabhq/gitlabhq"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "gitlabhq/gitlabhq"
  github_stars: 24298
---

# GitLab CI Pipeline Migrator

The GitLab CI Pipeline Migrator skill automates the conversion of GitLab CI/CD pipeline configurations to GitHub Actions workflow format. It uses the gitlab-ci-local parser to fully resolve .gitlab-ci.yml files including extends, anchors, and include directives.
The migration engine maps GitLab CI concepts to GitHub Actions equivalents: stages become job dependency chains with needs keywords, services become service containers, artifacts become upload/download-artifact actions, and cache configurations become actions/cache entries with matching key patterns.
YAML AST transformations preserve comments and formatting where possible, using the yaml library CST parser for structure-aware modifications. The skill handles complex GitLab features including DAG pipelines, parallel matrix jobs, rules-based conditional execution, and multi-project pipeline triggers.
Variable mapping converts GitLab CI predefined variables (CI_COMMIT_SHA, CI_PIPELINE_ID) to GitHub Actions equivalents (github.sha, github.run_id). The migrator generates a compatibility report identifying features that require manual intervention, such as GitLab-specific API integrations and container registry authentication differences.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gitlab-ci-pipeline-migrator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/gitlab-ci-pipeline-migrator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-pipeline-migrator/)
