---
name: "GitHub Actions Workflow Optimizer"
description: "Analyzes GitHub Actions YAML workflows to identify redundant steps, optimize caching strategies, and reduce CI minutes. Uses the GitHub Actions REST API and actions/cache toolkit to benchmark and improve pipeline performance."
category: "CI/CD Integrations"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/github-actions-workflow-optimizer/"
---
# GitHub Actions Workflow Optimizer

Analyzes GitHub Actions YAML workflows to identify redundant steps, optimize caching strategies, and reduce CI minutes. Uses the GitHub Actions REST API and actions/cache toolkit to benchmark and improve pipeline performance.

## Overview

The GitHub Actions Workflow Optimizer agent analyzes your CI/CD workflows defined in GitHub Actions YAML files to identify performance bottlenecks and optimization opportunities. It leverages the GitHub Actions REST API to fetch workflow run history, job durations, and cache hit rates, providing actionable recommendations to reduce build times and CI minutes consumption.

Key capabilities include detecting redundant checkout steps across jobs, recommending optimal cache key strategies using actions/cache v4, identifying opportunities to parallelize independent jobs with matrix strategies, and suggesting conditional step execution with if expressions. The agent analyzes your workflow against GitHub’s runner specifications to recommend appropriate runner sizes and operating systems.

It also monitors GitHub Actions usage quotas via the billing API, alerting when spending approaches limits. The optimizer generates before/after comparisons showing estimated time and cost savings, and can automatically create pull requests with optimized workflow files using the GitHub Contents API.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill github-actions-workflow-optimizer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill github-actions-workflow-optimizer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill github-actions-workflow-optimizer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill github-actions-workflow-optimizer -a codex
```

### OpenClaw

```bash
clawhub install github-actions-workflow-optimizer
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-workflow-optimizer/)
