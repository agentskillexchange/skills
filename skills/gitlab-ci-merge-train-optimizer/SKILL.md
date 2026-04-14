---
title: "GitLab CI Merge Train Optimizer"
description: "Optimizes GitLab CI/CD merge trains via the GitLab REST API v4 (/api/v4/projects/{id}/merge_trains). Analyzes pipeline durations, identifies bottleneck stages, and recommends DAG-based job dependencies for parallel execution."
verification: security_reviewed
source: "https://github.com/gitlabhq/gitlabhq"
category:
  - "CI/CD Integrations"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "gitlabhq/gitlabhq"
  github_stars: 24298
---

# GitLab CI Merge Train Optimizer

The GitLab CI Merge Train Optimizer agent connects to GitLab via the REST API v4 (/api/v4/projects/{id}/merge_trains, /api/v4/projects/{id}/pipelines) to analyze and optimize merge train performance. It retrieves merge train history, pipeline durations, and individual job timing data to identify throughput bottlenecks.

The agent analyzes .gitlab-ci.yml pipeline definitions to identify sequential job chains that could be parallelized using DAG (needs:) dependencies instead of stage-based ordering. It calculates theoretical speedup from proposed restructuring and models merge train throughput under different concurrency settings.

For ongoing optimization, the agent monitors pipeline reliability metrics including flaky test rates, runner queue times, and cache hit ratios. It identifies jobs with high variance in execution time and recommends resource class adjustments or job splitting strategies. Supports multi-project pipelines, parent-child pipeline analysis, and integration with GitLab Runner fleet metrics for capacity planning. Generates optimization reports with projected time savings and merge train throughput improvements.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-merge-train-optimizer/)
