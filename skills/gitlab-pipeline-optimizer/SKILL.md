---
name: "GitLab Pipeline Optimizer"
description: "Analyzes and optimizes GitLab CI/CD pipelines using the GitLab REST API v4 and .gitlab-ci.yml schema. Reduces pipeline duration by identifying bottleneck stages, configuring DAG dependencies with needs keyword, and implementing rules-based job filtering."
category: "CI/CD Integrations"
framework: "Claude Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/gitlab-pipeline-optimizer/"
tool_ecosystem:
  tool: gitlab
  github_stars: 24278
  github_repo: gitlabhq/gitlabhq
  maintained: true
---

# GitLab Pipeline Optimizer

Analyzes and optimizes GitLab CI/CD pipelines using the GitLab REST API v4 and .gitlab-ci.yml schema. Reduces pipeline duration by identifying bottleneck stages, configuring DAG dependencies with needs keyword, and implementing rules-based job filtering.

## Overview

The GitLab Pipeline Optimizer skill performs deep analysis of GitLab CI/CD pipeline configurations to reduce build times and resource consumption. It connects to the GitLab REST API v4 endpoints including /projects/:id/pipelines and /projects/:id/jobs to gather historical execution data and identify performance bottlenecks.

The skill parses .gitlab-ci.yml files and restructures them using directed acyclic graph (DAG) execution with the needs keyword, replacing sequential stage-based execution with parallel job graphs. It analyzes job dependency chains and recommends optimal grouping strategies.

Capabilities include configuring rules-based job filtering to skip unnecessary jobs on merge requests vs. default branch pushes, implementing extends and !reference tags for DRY configuration, setting up distributed caching with cache:key:files for package managers (npm, pip, composer), and configuring interruptible jobs with auto-cancel redundant pipelines. The skill also generates pipeline analytics dashboards using the GitLab pipeline analytics API and recommends runner fleet sizing based on job queue metrics from the /runners API endpoint.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gitlab-pipeline-optimizer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gitlab-pipeline-optimizer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gitlab-pipeline-optimizer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gitlab-pipeline-optimizer -a codex
```

### OpenClaw

```bash
clawhub install gitlab-pipeline-optimizer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/gitlab-pipeline-optimizer/
