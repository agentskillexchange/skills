---
title: "GitLab Pipeline Bottleneck Profiler"
description: "Profiles GitLab CI/CD pipeline execution using the GitLab Pipelines API and Job Artifacts API. Identifies stage bottlenecks and generates flame-graph visualizations of job dependencies."
verification: "security_reviewed"
source: "https://github.com/gitlabhq/gitlabhq"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "gitlabhq/gitlabhq"
  github_stars: 24298
---

# GitLab Pipeline Bottleneck Profiler

The GitLab Pipeline Bottleneck Profiler skill connects to your GitLab instance via the Pipelines API v4 to collect detailed timing data for every pipeline stage and job. It reconstructs the full dependency graph using needs/depends_on relationships defined in your .gitlab-ci.yml configuration.


Using the Job Artifacts API, the skill retrieves test timing reports and build logs to correlate pipeline duration with actual workload metrics. It generates interactive flame-graph visualizations using the d3-flame-graph library showing where time is spent across your pipeline.


The skill identifies critical path bottlenecks and recommends specific optimizations such as parallelizing independent jobs, introducing caching with the GCS or S3 cache backends, or splitting monolithic test stages. It supports analysis across multiple branches and merge request pipelines.


Integration with GitLab Merge Request Notes API allows the skill to automatically post profiling summaries as comments on merge requests, making performance regressions visible during code review.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-pipeline-bottleneck-profiler/)
