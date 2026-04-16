---
title: "GitLab CI Cache Optimizer"
description: "Optimizes GitLab CI/CD cache configurations using the GitLab Pipelines API v4 and cache:key:files directive analysis. Reduces pipeline duration by identifying cache misses and suggesting optimal key strategies."
verification: "security_reviewed"
source: "https://github.com/gitlabhq/gitlabhq"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "gitlabhq/gitlabhq"
  github_stars: 24298
---

# GitLab CI Cache Optimizer

The GitLab CI Cache Optimizer analyzes your GitLab CI/CD pipeline cache usage to identify optimization opportunities that reduce build times and storage costs. Using the GitLab Pipelines API v4, it fetches job execution data including cache hit/miss statistics and artifact sizes.


The agent parses .gitlab-ci.yml files to evaluate cache configurations, checking for common issues like overly broad cache keys that cause frequent invalidation, missing cache:key:files directives for dependency-based caching, and redundant cache paths that waste storage. It analyzes cache effectiveness by comparing job durations with and without cache hits.


Optimization recommendations include implementing cache:key:files with lock file references for deterministic caching, splitting caches by job stage to improve hit rates, configuring cache:when policies for failed builds, and setting appropriate cache:untracked and cache:unprotect options. The agent can generate optimized .gitlab-ci.yml cache blocks and estimate time savings based on historical pipeline data. Supports GitLab SaaS and self-managed instances.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-cache-optimizer-agent/)
