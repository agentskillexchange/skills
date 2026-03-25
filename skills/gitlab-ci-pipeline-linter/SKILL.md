---
name: "GitLab CI Pipeline Linter"
description: "Validates and optimizes .gitlab-ci.yml configurations using the GitLab CI Lint API (/api/v4/ci/lint). Checks for DAG dependency cycles, detects redundant job definitions, and suggests pipeline graph optimizations via the needs keyword."
category: "CI/CD Integrations"
framework: "Claude Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/gitlab-ci-pipeline-linter/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "gitlab"  # from ase_tool_match
  github_stars: 24278  # from ase_github_stars (integer, not string)
  github_repo: "gitlabhq/gitlabhq"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# GitLab CI Pipeline Linter

Validates and optimizes .gitlab-ci.yml configurations using the GitLab CI Lint API (/api/v4/ci/lint). Checks for DAG dependency cycles, detects redundant job definitions, and suggests pipeline graph optimizations via the needs keyword.

## Overview

The GitLab CI Pipeline Linter skill provides comprehensive validation and optimization for GitLab CI/CD pipeline configurations. It connects to the GitLab CI Lint API endpoint (/api/v4/ci/lint) to perform syntax validation, then applies deeper static analysis to detect common anti-patterns.

The skill analyzes job dependency graphs to identify DAG cycles that would cause pipeline failures, detects redundant job definitions that could be consolidated using extends or YAML anchors, and suggests optimizations using the needs keyword for parallel execution.

It validates that all referenced Docker images exist and are accessible, checks that artifact paths and dependencies are correctly configured, and ensures cache key strategies follow best practices for build performance.

The skill also supports multi-project pipeline validation by resolving trigger and include references across repositories using the GitLab Projects API. It can generate visual pipeline graph representations and estimate execution time based on historical job duration data from the GitLab Jobs API (/api/v4/projects/:id/jobs).

Supports both gitlab.com and self-hosted GitLab instances with personal access token or CI job token authentication.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-linter
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-linter -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-linter -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-linter -a codex
```

### OpenClaw

```bash
clawhub install gitlab-ci-pipeline-linter
```

## Source

- Marketplace: https://agentskillexchange.com/skills/gitlab-ci-pipeline-linter/
