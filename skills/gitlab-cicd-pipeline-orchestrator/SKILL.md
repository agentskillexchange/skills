---
name: "GitLab CI/CD Pipeline Orchestrator"
description: "Build and manage GitLab CI/CD pipelines using .gitlab-ci.yml and the GitLab REST API v4. Supports multi-project pipelines, DAG scheduling, and GitLab Runner fleet management."
category: "CI/CD Integrations"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/gitlab-cicd-pipeline-orchestrator/"
tool_ecosystem:
  tool: "gitlab"
  github_stars: 24278
  github_repo: "gitlabhq/gitlabhq"
  maintained: true
---

# GitLab CI/CD Pipeline Orchestrator

Build and manage GitLab CI/CD pipelines using .gitlab-ci.yml and the GitLab REST API v4. Supports multi-project pipelines, DAG scheduling, and GitLab Runner fleet management.

## Overview

The GitLab CI/CD Pipeline Orchestrator skill manages complex deployment pipelines through .gitlab-ci.yml configuration and the GitLab REST API v4. It generates pipeline configurations using GitLab CI concepts including stages, jobs with rules/only/except conditions, extends keyword for job inheritance, and include for multi-file pipeline composition (include:local, include:remote, include:template). The skill leverages the GitLab API endpoints (projects/{id}/pipelines, projects/{id}/jobs, projects/{id}/trigger/pipeline) for triggering pipelines with variables, monitoring job status, downloading artifacts, and managing environments. Advanced features include DAG (Directed Acyclic Graph) scheduling with needs keyword for parallel job optimization, multi-project pipeline triggers using trigger: keyword, parent-child pipelines for dynamic configuration, and review environments with auto-stop. The orchestrator handles GitLab Runner configuration (config.toml) for Docker and Kubernetes executors, manages CI/CD variables at project/group levels via the API, and supports compliance pipeline enforcement through group-level includes.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gitlab-cicd-pipeline-orchestrator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gitlab-cicd-pipeline-orchestrator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gitlab-cicd-pipeline-orchestrator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gitlab-cicd-pipeline-orchestrator -a codex
```

### OpenClaw

```bash
clawhub install gitlab-cicd-pipeline-orchestrator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/gitlab-cicd-pipeline-orchestrator/
