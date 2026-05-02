---
title: "GitLab CI Template Library"
description: "Creates reusable GitLab CI/CD template libraries using include:template and extends keywords. Manages pipeline configurations with rules:changes path filtering, needs DAG dependencies, and Auto DevOps customization via CI/CD variables."
verification: "security_reviewed"
source: "https://github.com/gitlabhq/gitlabhq"
category:
  - "CI/CD Integrations"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "gitlabhq/gitlabhq"
  github_stars: 24298
---

# GitLab CI Template Library

The GitLab CI Template Library skill creates and manages reusable CI/CD template collections for GitLab pipelines. It generates .gitlab-ci.yml configurations using the include:template directive for referencing shared templates and the extends keyword for job inheritance patterns.

This skill builds template libraries organized in GitLab project repositories with proper versioning using Git tags. Templates use rules:changes for path-based pipeline filtering, ensuring jobs only run when relevant files are modified. It configures DAG dependencies using the needs keyword for parallel stage execution.

For monorepo support, the skill generates parent-child pipeline architectures using trigger:include with dynamic child pipeline generation via generate_ci_config scripts. It handles multi-project pipelines with cross-project trigger configurations and artifact passing between upstream and downstream projects.

Advanced capabilities include Auto DevOps customization through CI/CD variables, cache configuration with per-branch key strategies, GitLab Container Registry integration for Docker builds using kaniko, review app environments with dynamic URLs, and release job configuration for automated changelog generation using release-cli.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/gitlab-ci-template-library/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gitlab-ci-template-library
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/gitlab-ci-template-library`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-template-library/)
