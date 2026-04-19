---
title: "GitLab CI/CD Pipeline Orchestrator"
description: "The GitLab CI/CD Pipeline Orchestrator skill manages complex deployment pipelines through .gitlab-ci.yml configuration and the GitLab REST API v4. It generates pipeline configurations using GitLab CI concepts including stages, jobs with rules/only/except conditions, extends keyword for job inheritance, and include for multi-file pipeline composition (include:local, include:remote, include:template). The skill leverages the GitLab API endpoints (projects/{id}/pipelines, projects/{id}/jobs, projects/{id}/trigger/pipeline) for triggering pipelines with variables, monitoring job status, downloading artifacts, and managing environments. Advanced features include DAG (Directed Acyclic Graph) scheduling with needs keyword for parallel job optimization, multi-project pipeline triggers using trigger: keyword, parent-child pipelines for dynamic configuration, and review environments with auto-stop. The orchestrator handles GitLab Runner configuration (config.toml) for Docker and Kubernetes executors, manages CI/CD variables at project/group levels via the API, and supports compliance pipeline enforcement through group-level includes."
source: "https://github.com/gitlabhq/gitlabhq"
verification: "security_reviewed"
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

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-cicd-pipeline-orchestrator/)
