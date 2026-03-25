---
name: "GitLab CI Pipeline Profiler"
description: "Profiles GitLab CI/CD pipeline execution times using the GitLab REST API v4 /projects/:id/pipelines endpoint. Identifies slow jobs, inefficient artifact passing, and cache miss patterns across pipeline history."
category: "CI/CD Integrations"
framework: "Custom Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/gitlab-ci-pipeline-profiler/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "gitlab"  # from ase_tool_match
  github_stars: 24276  # from ase_github_stars (integer, not string)
  github_repo: "gitlabhq/gitlabhq"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# GitLab CI Pipeline Profiler

Profiles GitLab CI/CD pipeline execution times using the GitLab REST API v4 /projects/:id/pipelines endpoint. Identifies slow jobs, inefficient artifact passing, and cache miss patterns across pipeline history.

## Overview

The GitLab CI Pipeline Profiler skill analyzes pipeline performance by querying the GitLab REST API v4 for historical pipeline and job execution data. It fetches pipeline details from /projects/:id/pipelines and individual job traces from /projects/:id/jobs/:job_id/trace endpoints. The skill computes statistical profiles for each job stage including median duration, p95 execution time, and variance across recent runs. It identifies bottlenecks such as jobs waiting for shared runners, excessive artifact upload/download times between stages, and cache key misconfigurations causing unnecessary rebuilds. The tool generates flamegraph-style visualizations of pipeline execution showing parallel job utilization and critical path analysis. It recommends optimizations including DAG keyword usage for stage bypassing, needs-based job dependencies, and rules-based job filtering to skip unnecessary work. Integration with GitLab container registry API helps identify oversized Docker images slowing job startup.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-profiler
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-profiler -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-profiler -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-profiler -a codex
```

### OpenClaw

```bash
clawhub install gitlab-ci-pipeline-profiler
```

## Source

- Marketplace: https://agentskillexchange.com/skills/gitlab-ci-pipeline-profiler/
