---
name: GitLab CI Pipeline Dependency Tracer
description: Traces job dependency chains in GitLab CI pipelines using the GitLab Jobs API and pipeline graph endpoints. Detects bottleneck stages that block parallel execution and suggests DAG refactoring. Integrates with the GitLab Merge Requests API to post optimization reports as MR comments.
category: CI/CD Integrations
framework: Any Agent
verification: security_reviewed
rating: 4.0
reviews: 45
source: https://agentskillexchange.com/skill/gitlab-ci-pipeline-dependency-tracer/
---

# GitLab CI Pipeline Dependency Tracer

Traces job dependency chains in GitLab CI pipelines using the GitLab Jobs API and pipeline graph endpoints. Detects bottleneck stages that block parallel execution and suggests DAG refactoring. Integrates with the GitLab Merge Requests API to post optimization reports as MR comments.

## Overview

Traces job dependency chains in GitLab CI pipelines using the GitLab Jobs API and pipeline graph endpoints. Detects bottleneck stages that block parallel execution and suggests DAG refactoring. Integrates with the GitLab Merge Requests API to post optimization reports as MR comments.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-dependency-tracer
```

### OpenClaw

```bash
clawhub install gitlab-ci-pipeline-dependency-tracer
```

### Claude Code

```bash
claude mcp add gitlab-ci-pipeline-dependency-tracer
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/gitlab-ci-pipeline-dependency-tracer/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: CI/CD Integrations
- **Framework**: Any Agent
- **Rating**: 4.0/5 (45 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/gitlab-ci-pipeline-dependency-tracer/)
