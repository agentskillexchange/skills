---
name: "CircleCI Pipeline Optimizer"
description: "Interfaces with CircleCI API v2 /pipeline and /workflow endpoints to analyze build performance. Identifies slow jobs via timing data, recommends Docker layer caching, and generates optimized .circleci/config.yml with parallelism settings."
category: "CI/CD Integrations"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/circleci-pipeline-optimizer/"
---
# CircleCI Pipeline Optimizer

Interfaces with CircleCI API v2 /pipeline and /workflow endpoints to analyze build performance. Identifies slow jobs via timing data, recommends Docker layer caching, and generates optimized .circleci/config.yml with parallelism settings.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill circleci-pipeline-optimizer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill circleci-pipeline-optimizer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill circleci-pipeline-optimizer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill circleci-pipeline-optimizer -a codex
```

### OpenClaw

```bash
clawhub install circleci-pipeline-optimizer
```

## Details

The CircleCI Pipeline Optimizer connects to the CircleCI API v2 to analyze pipeline performance and identify optimization opportunities. It queries /pipeline/{pipeline-id}/workflow to map workflow structures, then fetches job details via /workflow/{id}/job to extract timing breakdowns for each step. The agent identifies bottlenecks by comparing step durations across recent runs and flagging jobs that consistently exceed expected execution times. It analyzes Docker image pull times and recommends Docker Layer Caching (DLC) for custom images, calculates optimal parallelism values based on test splitting data from circleci tests split, and suggests resource class upgrades where CPU/memory constraints cause slowdowns. The optimizer generates updated .circleci/config.yml configurations with proper orb references, workspace persistence for artifact sharing between jobs, and conditional workflow execution using pipeline parameters and when/unless clauses. It also evaluates cache hit rates and recommends key rotation strategies.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-pipeline-optimizer/)
