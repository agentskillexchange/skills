---
title: "GitLab CI/CD Pipeline Orchestrator"
description: "Build and manage GitLab CI/CD pipelines using .gitlab-ci.yml and the GitLab REST API v4. Supports multi-project pipelines, DAG scheduling, and GitLab Runner fleet management."
slug: "gitlab-cicd-pipeline-orchestrator"
category:
  - "CI/CD Integrations"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/gitlab-cicd-pipeline-orchestrator/"
listed: true
---

# GitLab CI/CD Pipeline Orchestrator

Build and manage GitLab CI/CD pipelines using .gitlab-ci.yml and the GitLab REST API v4. Supports multi-project pipelines, DAG scheduling, and GitLab Runner fleet management.

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
clawhub install gitlab-cicd-pipeline-orchestrator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The GitLab CI/CD Pipeline Orchestrator skill manages complex deployment pipelines through .gitlab-ci.yml configuration and the GitLab REST API v4. It generates pipeline configurations using GitLab CI concepts including stages, jobs with rules/only/except conditions, extends keyword for job inheritance, and include for multi-file pipeline composition (include:local, include:remote, include:template). The skill leverages the GitLab API endpoints (projects/{id}/pipelines, projects/{id}/jobs, projects/{id}/trigger/pipeline) for triggering pipelines with variables, monitoring job status, downloading artifacts, and managing environments. Advanced features include DAG (Directed Acyclic Graph) scheduling with needs keyword for parallel job optimization, multi-project pipeline triggers using trigger: keyword, parent-child pipelines for dynamic configuration, and review environments with auto-stop. The orchestrator handles GitLab Runner configuration (config.toml) for Docker and Kubernetes executors, manages CI/CD variables at project/group levels via the API, and supports compliance pipeline enforcement through group-level includes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-cicd-pipeline-orchestrator/)
