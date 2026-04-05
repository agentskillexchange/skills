---
name: "GitLab Pipeline Orchestrator"
description: "Automates GitLab CI/CD pipeline creation using the GitLab Pipelines API and .gitlab-ci.yml DSL. Manages multi-stage builds with artifact caching via the GitLab Artifacts API and triggers downstream pipelines through bridge jobs."
category: "CI/CD Integrations"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/gitlab-pipeline-orchestrator/"
---
# GitLab Pipeline Orchestrator

Automates GitLab CI/CD pipeline creation using the GitLab Pipelines API and .gitlab-ci.yml DSL. Manages multi-stage builds with artifact caching via the GitLab Artifacts API and triggers downstream pipelines through bridge jobs.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gitlab-pipeline-orchestrator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gitlab-pipeline-orchestrator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gitlab-pipeline-orchestrator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gitlab-pipeline-orchestrator -a codex
```

### OpenClaw

```bash
clawhub install gitlab-pipeline-orchestrator
```

## Details

The GitLab Pipeline Orchestrator skill provides comprehensive automation for GitLab CI/CD workflows. It leverages the GitLab Pipelines API v4 to programmatically create, trigger, and monitor pipeline runs across multiple projects. The skill generates optimized .gitlab-ci.yml configurations with proper stage ordering, dependency management, and parallel job execution. It integrates with the GitLab Artifacts API to configure intelligent caching strategies that reduce build times by up to 60%. Bridge jobs enable cross-project pipeline triggering for monorepo and microservice architectures. The skill supports dynamic child pipelines using the trigger:include pattern, environment-specific deployments with manual approval gates, and auto-scaling runners configuration. It also handles merge request pipelines with detached mode, security scanning integration via GitLab SAST/DAST templates, and deployment freezes during critical periods.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-pipeline-orchestrator/)
