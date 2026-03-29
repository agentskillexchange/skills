---
name: "GitLab CI Auto DevOps Configurator"
description: "Configures GitLab CI/CD pipelines using .gitlab-ci.yml with Auto DevOps templates, includes, and the GitLab Container Registry. Manages multi-project pipelines and environment-specific deployments."
category: "CI/CD Integrations"
framework: "Claude Agents"
verification: security_reviewed
source: "https://github.com/gitlabhq/gitlabhq"
tool_ecosystem:
  tool: gitlab
  github_stars: 24278
  github_repo: gitlabhq/gitlabhq
  maintained: true
---
# GitLab CI Auto DevOps Configurator

Configures GitLab CI/CD pipelines using .gitlab-ci.yml with Auto DevOps templates, includes, and the GitLab Container Registry. Manages multi-project pipelines and environment-specific deployments.

## Overview

The GitLab CI Auto DevOps Configurator skill generates .gitlab-ci.yml configurations using GitLab CI/CD syntax including stages, jobs, rules, artifacts, and cache directives. It leverages Auto DevOps templates (include: template: Auto-DevOps.gitlab-ci.yml) and GitLab-maintained CI templates for common languages and frameworks.

The skill configures job definitions with script blocks, before_script/after_script hooks, image specifications for Docker executors, and services for dependency containers (postgres, redis, elasticsearch). It manages variables at project, group, and instance levels with protected and masked options. Cache configuration uses key-based strategies with cache:paths and cache:policy for build artifact reuse.

Advanced features include multi-project pipeline triggers using trigger:project, parent-child pipelines with trigger:include, DAG (Directed Acyclic Graph) dependencies using needs for optimized execution order, and rules-based job control replacing only/except with flexible conditions. The configurator supports GitLab Container Registry integration (CI_REGISTRY_IMAGE), review app deployment with environment:url and environment:on_stop, SAST/DAST security scanning template inclusion, and GitLab Pages deployment configuration for static site hosting.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-auto-devops-configurator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-auto-devops-configurator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-auto-devops-configurator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-auto-devops-configurator -a codex
```

### OpenClaw

```bash
clawhub install gitlab-ci-auto-devops-configurator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-auto-devops-configurator/)
