---
title: GitLab Pipeline Bottleneck Profiler
description: The GitLab Pipeline Bottleneck Profiler skill connects to your GitLab
  instance via the Pipelines API v4 to collect detailed timing data for every pipeline
  stage and job. It reconstructs the full dependency graph using needs/depends_on
  relationships defined in your .gitlab-ci.yml configuration. Using the Job Artifacts
  API, the skill retrieves test timing reports and build logs to correlate pipeline
  duration with actual workload metrics. It generates interactive flame-graph visualizations
  using the d3-flame-graph library showing where time is spent across your pipeline.
  The skill identifies critical path bottlenecks and recommends specific optimizations
  such as parallelizing independent jobs, introducing caching with the GCS or S3 cache
  backends, or splitting monolithic test stages. It supports analysis across multiple
  branches and merge request pipelines. Integration with GitLab Merge Request Notes
  API allows the skill to automatically post profiling summaries as comments on merge
  requests, making performance regressions visible during code review.
verification: security_reviewed
source: https://agentskillexchange.com/skills/gitlab-pipeline-bottleneck-profiler/
category:
- CI/CD Integrations
framework:
- Claude Agents
---

# GitLab Pipeline Bottleneck Profiler

The GitLab Pipeline Bottleneck Profiler skill connects to your GitLab instance via the Pipelines API v4 to collect detailed timing data for every pipeline stage and job. It reconstructs the full dependency graph using needs/depends_on relationships defined in your .gitlab-ci.yml configuration. Using the Job Artifacts API, the skill retrieves test timing reports and build logs to correlate pipeline duration with actual workload metrics. It generates interactive flame-graph visualizations using the d3-flame-graph library showing where time is spent across your pipeline. The skill identifies critical path bottlenecks and recommends specific optimizations such as parallelizing independent jobs, introducing caching with the GCS or S3 cache backends, or splitting monolithic test stages. It supports analysis across multiple branches and merge request pipelines. Integration with GitLab Merge Request Notes API allows the skill to automatically post profiling summaries as comments on merge requests, making performance regressions visible during code review.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-pipeline-bottleneck-profiler/)
