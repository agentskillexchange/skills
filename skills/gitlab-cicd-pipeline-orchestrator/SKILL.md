---
title: "GitLab CI/CD Pipeline Orchestrator"
description: "Build and manage GitLab CI/CD pipelines using .gitlab-ci.yml and the GitLab REST API v4. Supports multi-project pipelines, DAG scheduling, and GitLab Runner fleet management."
verification: "security_reviewed"
source: "https://github.com/gitlabhq/gitlabhq"
category:
  - "CI/CD Integrations"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "gitlabhq/gitlabhq"
  github_stars: 24298
---

# GitLab CI/CD Pipeline Orchestrator

The GitLab CI/CD Pipeline Orchestrator skill manages complex deployment pipelines through .gitlab-ci.yml configuration and the GitLab REST API v4. It generates pipeline configurations using GitLab CI concepts including stages, jobs with rules/only/except conditions, extends keyword for job inheritance, and include for multi-file pipeline composition (include:local, include:remote, include:template). The skill leverages the GitLab API endpoints (projects/{id}/pipelines, projects/{id}/jobs, projects/{id}/trigger/pipeline) for triggering pipelines with variables, monitoring job status, downloading artifacts, and managing environments. Advanced features include DAG (Directed Acyclic Graph) scheduling with needs keyword for parallel job optimization, multi-project pipeline triggers using trigger: keyword, parent-child pipelines for dynamic configuration, and review environments with auto-stop. The orchestrator handles GitLab Runner configuration (config.toml) for Docker and Kubernetes executors, manages CI/CD variables at project/group levels via the API, and supports compliance pipeline enforcement through group-level includes.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/gitlab-cicd-pipeline-orchestrator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gitlab-cicd-pipeline-orchestrator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/gitlab-cicd-pipeline-orchestrator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-cicd-pipeline-orchestrator/)
