---
name: "GitLab CI Pipeline Validator"
description: "Validates .gitlab-ci.yml files against GitLab CI/CD schema using the gitlab-ci-lint API endpoint. Catches stage dependency errors, invalid artifact paths, and misconfigured rules before commit."
category: "CI/CD Integrations"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/gitlab-ci-pipeline-validator/"
---
# GitLab CI Pipeline Validator

Validates .gitlab-ci.yml files against GitLab CI/CD schema using the gitlab-ci-lint API endpoint. Catches stage dependency errors, invalid artifact paths, and misconfigured rules before commit.

The GitLab CI Pipeline Validator skill provides comprehensive validation of .gitlab-ci.yml configuration files before they reach your CI/CD pipeline. It leverages the GitLab CI Lint API (/api/v4/ci/lint) to perform server-side validation, catching syntax errors, undefined stage references, and circular dependencies that would otherwise cause pipeline failures.

Key capabilities include validating job dependencies and needs declarations, checking artifact path patterns against gitignore-style rules, verifying rules:if expressions use valid CI/CD predefined variables, and ensuring include: references resolve to accessible files. The skill also validates cache key templates, services configurations, and parallel:matrix definitions.

For monorepo setups, it supports changes-based rules validation and can verify trigger:project references. It outputs detailed error messages with line numbers and suggestions for fixes, making it ideal for pre-commit hooks or code review automation. Supports GitLab 15.x+ API schemas with backward compatibility detection.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-validator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-validator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-validator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-validator -a codex
```

### OpenClaw

```bash
clawhub install gitlab-ci-pipeline-validator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-pipeline-validator/)
