---
title: "GitLab Pipeline Bottleneck Profiler"
description: "Profiles GitLab CI/CD pipeline execution using the GitLab Pipelines API and Job Artifacts API. Identifies stage bottlenecks and generates flame-graph visualizations of job dependencies."
slug: "gitlab-pipeline-bottleneck-profiler"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/gitlab-pipeline-bottleneck-profiler/"
listed: true
---

# GitLab Pipeline Bottleneck Profiler

Profiles GitLab CI/CD pipeline execution using the GitLab Pipelines API and Job Artifacts API. Identifies stage bottlenecks and generates flame-graph visualizations of job dependencies.

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
clawhub install gitlab-pipeline-bottleneck-profiler
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The GitLab Pipeline Bottleneck Profiler skill connects to your GitLab instance via the Pipelines API v4 to collect detailed timing data for every pipeline stage and job. It reconstructs the full dependency graph using needs/depends_on relationships defined in your .gitlab-ci.yml configuration.
Using the Job Artifacts API, the skill retrieves test timing reports and build logs to correlate pipeline duration with actual workload metrics. It generates interactive flame-graph visualizations using the d3-flame-graph library showing where time is spent across your pipeline.
The skill identifies critical path bottlenecks and recommends specific optimizations such as parallelizing independent jobs, introducing caching with the GCS or S3 cache backends, or splitting monolithic test stages. It supports analysis across multiple branches and merge request pipelines.
Integration with GitLab Merge Request Notes API allows the skill to automatically post profiling summaries as comments on merge requests, making performance regressions visible during code review.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-pipeline-bottleneck-profiler/)
