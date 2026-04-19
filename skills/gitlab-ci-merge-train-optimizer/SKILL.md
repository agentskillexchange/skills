---
title: "GitLab CI Merge Train Optimizer"
description: "The GitLab CI Merge Train Optimizer agent connects to GitLab via the REST API v4 (/api/v4/projects/{id}/merge_trains, /api/v4/projects/{id}/pipelines) to analyze and optimize merge train performance. It retrieves merge train history, pipeline durations, and individual job timing data to identify throughput bottlenecks. The agent analyzes .gitlab-ci.yml pipeline definitions to identify sequential job chains that could be parallelized using DAG (needs:) dependencies instead of stage-based ordering. It calculates theoretical speedup from proposed restructuring and models merge train throughput under different concurrency settings. For ongoing optimization, the agent monitors pipeline reliability metrics including flaky test rates, runner queue times, and cache hit ratios. It identifies jobs with high variance in execution time and recommends resource class adjustments or job splitting strategies. Supports multi-project pipelines, parent-child pipeline analysis, and integration with GitLab Runner fleet metrics for capacity planning. Generates optimization reports with projected time savings and merge train throughput improvements."
source: "https://github.com/gitlabhq/gitlabhq"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "gitlabhq/gitlabhq"
  github_stars: 24298
---

# GitLab CI Merge Train Optimizer

The GitLab CI Merge Train Optimizer agent connects to GitLab via the REST API v4 (/api/v4/projects/{id}/merge_trains, /api/v4/projects/{id}/pipelines) to analyze and optimize merge train performance. It retrieves merge train history, pipeline durations, and individual job timing data to identify throughput bottlenecks. The agent analyzes .gitlab-ci.yml pipeline definitions to identify sequential job chains that could be parallelized using DAG (needs:) dependencies instead of stage-based ordering. It calculates theoretical speedup from proposed restructuring and models merge train throughput under different concurrency settings. For ongoing optimization, the agent monitors pipeline reliability metrics including flaky test rates, runner queue times, and cache hit ratios. It identifies jobs with high variance in execution time and recommends resource class adjustments or job splitting strategies. Supports multi-project pipelines, parent-child pipeline analysis, and integration with GitLab Runner fleet metrics for capacity planning. Generates optimization reports with projected time savings and merge train throughput improvements.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-merge-train-optimizer/)
