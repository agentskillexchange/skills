---
title: "GitLab CI Pipeline Profiler"
description: "Profiles GitLab CI/CD pipeline execution times using the GitLab REST API v4 /projects/:id/pipelines endpoint. Identifies slow jobs, inefficient artifact passing, and cache miss patterns across pipeline history."
verification: security_reviewed
source: "https://github.com/gitlabhq/gitlabhq"
category:
  - "CI/CD Integrations"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "gitlabhq/gitlabhq"
  github_stars: 24298
---

# GitLab CI Pipeline Profiler

The GitLab CI Pipeline Profiler skill analyzes pipeline performance by querying the GitLab REST API v4 for historical pipeline and job execution data. It fetches pipeline details from /projects/:id/pipelines and individual job traces from /projects/:id/jobs/:job_id/trace endpoints. The skill computes statistical profiles for each job stage including median duration, p95 execution time, and variance across recent runs. It identifies bottlenecks such as jobs waiting for shared runners, excessive artifact upload/download times between stages, and cache key misconfigurations causing unnecessary rebuilds. The tool generates flamegraph-style visualizations of pipeline execution showing parallel job utilization and critical path analysis. It recommends optimizations including DAG keyword usage for stage bypassing, needs-based job dependencies, and rules-based job filtering to skip unnecessary work. Integration with GitLab container registry API helps identify oversized Docker images slowing job startup.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gitlab-ci-pipeline-profiler
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/gitlab-ci-pipeline-profiler` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-pipeline-profiler/)
