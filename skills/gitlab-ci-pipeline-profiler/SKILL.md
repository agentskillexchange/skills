---
title: "GitLab CI Pipeline Profiler"
description: "Profiles GitLab CI/CD pipeline execution times using the GitLab REST API v4 /projects/:id/pipelines endpoint. Identifies slow jobs, inefficient artifact passing, and cache miss patterns across pipeline history."
verification: "security_reviewed"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-pipeline-profiler/)
