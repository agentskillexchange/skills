---
title: "GitLab CI Auto DevOps Configurator"
description: "Configures GitLab CI/CD pipelines using .gitlab-ci.yml with Auto DevOps templates, includes, and the GitLab Container Registry. Manages multi-project pipelines and environment-specific deployments."
verification: "security_reviewed"
source: "https://github.com/gitlabhq/gitlabhq"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "gitlabhq/gitlabhq"
  github_stars: 24298
---

# GitLab CI Auto DevOps Configurator

The GitLab CI Auto DevOps Configurator skill generates .gitlab-ci.yml configurations using GitLab CI/CD syntax including stages, jobs, rules, artifacts, and cache directives. It leverages Auto DevOps templates (include: template: Auto-DevOps.gitlab-ci.yml) and GitLab-maintained CI templates for common languages and frameworks.

The skill configures job definitions with script blocks, before_script/after_script hooks, image specifications for Docker executors, and services for dependency containers (postgres, redis, elasticsearch). It manages variables at project, group, and instance levels with protected and masked options. Cache configuration uses key-based strategies with cache:paths and cache:policy for build artifact reuse.

Advanced features include multi-project pipeline triggers using trigger:project, parent-child pipelines with trigger:include, DAG (Directed Acyclic Graph) dependencies using needs for optimized execution order, and rules-based job control replacing only/except with flexible conditions. The configurator supports GitLab Container Registry integration (CI_REGISTRY_IMAGE), review app deployment with environment:url and environment:on_stop, SAST/DAST security scanning template inclusion, and GitLab Pages deployment configuration for static site hosting.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-auto-devops-configurator/)
