---
name: "GitLab Pipeline Bottleneck Profiler"
description: "Profiles GitLab CI/CD pipeline execution using the GitLab Pipelines API and Job Artifacts API. Identifies stage bottlenecks and generates flame-graph visualizations of job dependencies."
category: "CI/CD Integrations"
framework: "Claude Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/gitlab-pipeline-bottleneck-profiler/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "gitlab"  # from ase_tool_match
  github_stars: 24276  # from ase_github_stars (integer, not string)
  github_repo: "gitlabhq/gitlabhq"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# GitLab Pipeline Bottleneck Profiler

Profiles GitLab CI/CD pipeline execution using the GitLab Pipelines API and Job Artifacts API. Identifies stage bottlenecks and generates flame-graph visualizations of job dependencies.

## Overview

The GitLab Pipeline Bottleneck Profiler skill connects to your GitLab instance via the Pipelines API v4 to collect detailed timing data for every pipeline stage and job. It reconstructs the full dependency graph using needs/depends_on relationships defined in your .gitlab-ci.yml configuration.

Using the Job Artifacts API, the skill retrieves test timing reports and build logs to correlate pipeline duration with actual workload metrics. It generates interactive flame-graph visualizations using the d3-flame-graph library showing where time is spent across your pipeline.

The skill identifies critical path bottlenecks and recommends specific optimizations such as parallelizing independent jobs, introducing caching with the GCS or S3 cache backends, or splitting monolithic test stages. It supports analysis across multiple branches and merge request pipelines.

Integration with GitLab Merge Request Notes API allows the skill to automatically post profiling summaries as comments on merge requests, making performance regressions visible during code review.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gitlab-pipeline-bottleneck-profiler
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gitlab-pipeline-bottleneck-profiler -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gitlab-pipeline-bottleneck-profiler -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gitlab-pipeline-bottleneck-profiler -a codex
```

### OpenClaw

```bash
clawhub install gitlab-pipeline-bottleneck-profiler
```

## Source

- Marketplace: https://agentskillexchange.com/skills/gitlab-pipeline-bottleneck-profiler/
