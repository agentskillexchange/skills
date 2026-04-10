---
title: "GitLab CI Pipeline Profiler"
description: "Profiles GitLab CI/CD pipeline execution times using the GitLab REST API v4 /projects/:id/pipelines endpoint. Identifies slow jobs, inefficient artifact passing, and cache miss patterns across pipeline history."
slug: "gitlab-ci-pipeline-profiler"
category:
  - "CI/CD Integrations"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/gitlab-ci-pipeline-profiler/"
listed: true
---

# GitLab CI Pipeline Profiler

Profiles GitLab CI/CD pipeline execution times using the GitLab REST API v4 /projects/:id/pipelines endpoint. Identifies slow jobs, inefficient artifact passing, and cache miss patterns across pipeline history.

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
clawhub install gitlab-ci-pipeline-profiler
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The GitLab CI Pipeline Profiler skill analyzes pipeline performance by querying the GitLab REST API v4 for historical pipeline and job execution data. It fetches pipeline details from /projects/:id/pipelines and individual job traces from /projects/:id/jobs/:job_id/trace endpoints. The skill computes statistical profiles for each job stage including median duration, p95 execution time, and variance across recent runs. It identifies bottlenecks such as jobs waiting for shared runners, excessive artifact upload/download times between stages, and cache key misconfigurations causing unnecessary rebuilds. The tool generates flamegraph-style visualizations of pipeline execution showing parallel job utilization and critical path analysis. It recommends optimizations including DAG keyword usage for stage bypassing, needs-based job dependencies, and rules-based job filtering to skip unnecessary work. Integration with GitLab container registry API helps identify oversized Docker images slowing job startup.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-pipeline-profiler/)
