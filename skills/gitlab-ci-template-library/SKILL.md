---
title: "GitLab CI Template Library"
description: "Creates reusable GitLab CI/CD template libraries using include:template and extends keywords. Manages pipeline configurations with rules:changes path filtering, needs DAG dependencies, and Auto DevOps customization via CI/CD variables."
verification: security_reviewed
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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-template-library/)
