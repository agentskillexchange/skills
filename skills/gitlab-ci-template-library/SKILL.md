---
title: "GitLab CI Template Library"
description: "Creates reusable GitLab CI/CD template libraries using include:template and extends keywords. Manages pipeline configurations with rules:changes path filtering, needs DAG dependencies, and Auto DevOps customization via CI/CD variables."
slug: "gitlab-ci-template-library"
category:
  - "CI/CD Integrations"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/gitlab-ci-template-library/"
---

# GitLab CI Template Library

Creates reusable GitLab CI/CD template libraries using include:template and extends keywords. Manages pipeline configurations with rules:changes path filtering, needs DAG dependencies, and Auto DevOps customization via CI/CD variables.

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
clawhub install gitlab-ci-template-library
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The GitLab CI Template Library skill creates and manages reusable CI/CD template collections for GitLab pipelines. It generates .gitlab-ci.yml configurations using the include:template directive for referencing shared templates and the extends keyword for job inheritance patterns.
This skill builds template libraries organized in GitLab project repositories with proper versioning using Git tags. Templates use rules:changes for path-based pipeline filtering, ensuring jobs only run when relevant files are modified. It configures DAG dependencies using the needs keyword for parallel stage execution.
For monorepo support, the skill generates parent-child pipeline architectures using trigger:include with dynamic child pipeline generation via generate_ci_config scripts. It handles multi-project pipelines with cross-project trigger configurations and artifact passing between upstream and downstream projects.
Advanced capabilities include Auto DevOps customization through CI/CD variables, cache configuration with per-branch key strategies, GitLab Container Registry integration for Docker builds using kaniko, review app environments with dynamic URLs, and release job configuration for automated changelog generation using release-cli.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-template-library/)
