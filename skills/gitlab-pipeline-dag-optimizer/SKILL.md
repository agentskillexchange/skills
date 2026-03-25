---
name: "GitLab Pipeline DAG Optimizer"
description: "Analyzes GitLab CI/CD pipeline YAML using the GitLab Pipelines API to detect bottlenecks and restructure directed acyclic graph (DAG) dependencies. Integrates with gitlab-runner exec and the Merge Request Approvals API for automated gate checks."
category: "CI/CD Integrations"
framework: "OpenClaw"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/gitlab-pipeline-dag-optimizer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "gitlab"  # from ase_tool_match
  github_stars: 24276  # from ase_github_stars (integer, not string)
  github_repo: "gitlabhq/gitlabhq"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# GitLab Pipeline DAG Optimizer

Analyzes GitLab CI/CD pipeline YAML using the GitLab Pipelines API to detect bottlenecks and restructure directed acyclic graph (DAG) dependencies. Integrates with gitlab-runner exec and the Merge Request Approvals API for automated gate checks.

## Overview

Overview

The GitLab Pipeline DAG Optimizer analyzes your `.gitlab-ci.yml` configurations to identify pipeline bottlenecks and restructure job dependencies for maximum parallelism. It uses the GitLab Pipelines API to fetch historical execution data and identify critical path inefficiencies.

Key Capabilities

This skill maps out directed acyclic graph (DAG) dependencies using the `needs:` keyword relationships, identifying jobs that can run in parallel but are unnecessarily serialized. It integrates with `gitlab-runner exec` for local pipeline simulation and validates optimized configurations before pushing changes. The optimizer also leverages the Merge Request Approvals API to enforce pipeline performance gates.

Optimization Strategies

Implements pipeline sectioning with `rules:` and `workflow:` blocks to skip irrelevant stages, configures `interruptible:` flags for redundant pipeline cancellation, and tunes runner tag assignments based on job resource requirements. Supports multi-project pipeline triggers and downstream pipeline dependency management for monorepo architectures.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gitlab-pipeline-dag-optimizer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gitlab-pipeline-dag-optimizer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gitlab-pipeline-dag-optimizer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gitlab-pipeline-dag-optimizer -a codex
```

### OpenClaw

```bash
clawhub install gitlab-pipeline-dag-optimizer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/gitlab-pipeline-dag-optimizer/
