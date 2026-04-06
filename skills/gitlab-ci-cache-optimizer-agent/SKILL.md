---
name: "GitLab CI Cache Optimizer"
description: "Optimizes GitLab CI/CD cache configurations using the GitLab Pipelines API v4 and cache:key:files directive analysis. Reduces pipeline duration by identifying cache misses and suggesting optimal key strategies."
category: "CI/CD Integrations"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/gitlab-ci-cache-optimizer-agent/"
---
# GitLab CI Cache Optimizer

Optimizes GitLab CI/CD cache configurations using the GitLab Pipelines API v4 and cache:key:files directive analysis. Reduces pipeline duration by identifying cache misses and suggesting optimal key strategies.

The GitLab CI Cache Optimizer analyzes your GitLab CI/CD pipeline cache usage to identify optimization opportunities that reduce build times and storage costs. Using the GitLab Pipelines API v4, it fetches job execution data including cache hit/miss statistics and artifact sizes.



The agent parses .gitlab-ci.yml files to evaluate cache configurations, checking for common issues like overly broad cache keys that cause frequent invalidation, missing cache:key:files directives for dependency-based caching, and redundant cache paths that waste storage. It analyzes cache effectiveness by comparing job durations with and without cache hits.



Optimization recommendations include implementing cache:key:files with lock file references for deterministic caching, splitting caches by job stage to improve hit rates, configuring cache:when policies for failed builds, and setting appropriate cache:untracked and cache:unprotect options. The agent can generate optimized .gitlab-ci.yml cache blocks and estimate time savings based on historical pipeline data. Supports GitLab SaaS and self-managed instances.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-cache-optimizer-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-cache-optimizer-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-cache-optimizer-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-cache-optimizer-agent -a codex
```

### OpenClaw

```bash
clawhub install gitlab-ci-cache-optimizer-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-cache-optimizer-agent/)
