---
name: "GitLab CI Pipeline Dependency Tracer"
description: "Traces job dependency chains in GitLab CI pipelines using the GitLab Jobs API and pipeline graph endpoints. Detects bottleneck stages that block parallel execution and suggests DAG refactoring. Integrates with the GitLab Merge Requests API to post optimization reports as MR comments."
category: "CI/CD Integrations"
framework: "Codex"
verification: security_reviewed
source: "https://github.com/gitlabhq/gitlabhq"
tool_ecosystem:
  tool: gitlab
  github_repo: gitlabhq/gitlabhq
  github_stars: 24283
  maintained: true
---
# GitLab CI Pipeline Dependency Tracer

Traces job dependency chains in GitLab CI pipelines using the GitLab Jobs API and pipeline graph endpoints. Detects bottleneck stages that block parallel execution and suggests DAG refactoring. Integrates with the GitLab Merge Requests API to post optimization reports as MR comments.

## Overview

This skill uses the GitLab REST API (gitlab.com/api/v4) to fetch pipeline definitions and job dependency metadata. It builds a directed acyclic graph (DAG) of job relationships using the needs keyword and identifies critical path bottlenecks that force serialization. The skill calls the GitLab Pipelines API to pull historical duration data across branches and computes median stage latency. When bottlenecks are detected, it generates refactored .gitlab-ci.yml snippets with corrected needs declarations. Integration with the GitLab Merge Requests API enables automatic posting of a structured optimization report as an MR comment, including a Mermaid diagram of the corrected pipeline graph. Compatible with GitLab SaaS, self-managed, and GitLab Dedicated.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-dependency-tracer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-dependency-tracer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-dependency-tracer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-dependency-tracer -a codex
```

### OpenClaw

```bash
clawhub install gitlab-ci-pipeline-dependency-tracer
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-pipeline-dependency-tracer/)
