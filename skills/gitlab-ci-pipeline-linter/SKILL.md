---
name: "GitLab CI Pipeline Linter"
description: "Validates and optimizes .gitlab-ci.yml configurations using the GitLab CI Lint API (/api/v4/ci/lint). Checks for DAG dependency cycles, detects redundant job definitions, and suggests pipeline graph optimizations via the needs keyword."
category: "CI/CD Integrations"
framework: "Claude Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/gitlab-ci-pipeline-linter/"
---
# GitLab CI Pipeline Linter

Validates and optimizes .gitlab-ci.yml configurations using the GitLab CI Lint API (/api/v4/ci/lint). Checks for DAG dependency cycles, detects redundant job definitions, and suggests pipeline graph optimizations via the needs keyword.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-pipeline-linter/)
