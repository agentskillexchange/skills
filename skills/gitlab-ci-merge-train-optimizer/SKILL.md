---
name: "GitLab CI Merge Train Optimizer"
description: "Optimizes GitLab CI/CD merge trains via the GitLab REST API v4 (/api/v4/projects/{id}/merge_trains). Analyzes pipeline durations, identifies bottleneck stages, and recommends DAG-based job dependencies for parallel execution."
category: "CI/CD Integrations"
framework: "Codex"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/gitlab-ci-merge-train-optimizer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "gitlab"  # from ase_tool_match
  github_stars: 24276  # from ase_github_stars (integer, not string)
  github_repo: "gitlabhq/gitlabhq"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# GitLab CI Merge Train Optimizer

Optimizes GitLab CI/CD merge trains via the GitLab REST API v4 (/api/v4/projects/{id}/merge_trains). Analyzes pipeline durations, identifies bottleneck stages, and recommends DAG-based job dependencies for parallel execution.

## Overview

The GitLab CI Merge Train Optimizer agent connects to GitLab via the REST API v4 (/api/v4/projects/{id}/merge_trains, /api/v4/projects/{id}/pipelines) to analyze and optimize merge train performance. It retrieves merge train history, pipeline durations, and individual job timing data to identify throughput bottlenecks.

The agent analyzes .gitlab-ci.yml pipeline definitions to identify sequential job chains that could be parallelized using DAG (needs:) dependencies instead of stage-based ordering. It calculates theoretical speedup from proposed restructuring and models merge train throughput under different concurrency settings.

For ongoing optimization, the agent monitors pipeline reliability metrics including flaky test rates, runner queue times, and cache hit ratios. It identifies jobs with high variance in execution time and recommends resource class adjustments or job splitting strategies. Supports multi-project pipelines, parent-child pipeline analysis, and integration with GitLab Runner fleet metrics for capacity planning. Generates optimization reports with projected time savings and merge train throughput improvements.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-merge-train-optimizer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-merge-train-optimizer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-merge-train-optimizer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-merge-train-optimizer -a codex
```

### OpenClaw

```bash
clawhub install gitlab-ci-merge-train-optimizer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/gitlab-ci-merge-train-optimizer/
