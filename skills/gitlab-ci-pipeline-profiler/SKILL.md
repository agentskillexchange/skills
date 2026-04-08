---
title: GitLab CI Pipeline Profiler
description: The GitLab CI Pipeline Profiler skill analyzes pipeline performance by
  querying the GitLab REST API v4 for historical pipeline and job execution data.
  It fetches pipeline details from /projects/:id/pipelines and individual job traces
  from /projects/:id/jobs/:job_id/trace endpoints. The skill computes statistical
  profiles for each job stage including median duration, p95 execution time, and variance
  across recent runs. It identifies bottlenecks such as jobs waiting for shared runners,
  excessive artifact upload/download times between stages, and cache key misconfigurations
  causing unnecessary rebuilds. The tool generates flamegraph-style visualizations
  of pipeline execution showing parallel job utilization and critical path analysis.
  It recommends optimizations including DAG keyword usage for stage bypassing, needs-based
  job dependencies, and rules-based job filtering to skip unnecessary work. Integration
  with GitLab container registry API helps identify oversized Docker images slowing
  job startup.
verification: security_reviewed
source: https://agentskillexchange.com/skills/gitlab-ci-pipeline-profiler/
category:
- CI/CD Integrations
framework:
- Custom Agents
---

# GitLab CI Pipeline Profiler

The GitLab CI Pipeline Profiler skill analyzes pipeline performance by querying the GitLab REST API v4 for historical pipeline and job execution data. It fetches pipeline details from /projects/:id/pipelines and individual job traces from /projects/:id/jobs/:job_id/trace endpoints. The skill computes statistical profiles for each job stage including median duration, p95 execution time, and variance across recent runs. It identifies bottlenecks such as jobs waiting for shared runners, excessive artifact upload/download times between stages, and cache key misconfigurations causing unnecessary rebuilds. The tool generates flamegraph-style visualizations of pipeline execution showing parallel job utilization and critical path analysis. It recommends optimizations including DAG keyword usage for stage bypassing, needs-based job dependencies, and rules-based job filtering to skip unnecessary work. Integration with GitLab container registry API helps identify oversized Docker images slowing job startup.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-pipeline-profiler/)
