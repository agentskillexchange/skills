---
name: "GitHub Actions CI Pipeline Builder"
description: "Generates and manages GitHub Actions workflows using the Workflow YAML syntax and GitHub REST API. Supports matrix builds, reusable workflows, and composite actions."
category: "CI/CD Integrations"
framework: "Codex"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/github-actions-ci-pipeline-builder/"
---

# GitHub Actions CI Pipeline Builder

Generates and manages GitHub Actions workflows using the Workflow YAML syntax and GitHub REST API. Supports matrix builds, reusable workflows, and composite actions.

## Overview

The GitHub Actions CI Pipeline Builder creates, validates, and manages CI/CD workflows using GitHub Actions YAML syntax and the GitHub REST API (repos/{owner}/{repo}/actions/workflows, actions/runs). It generates production-ready workflow files with proper job dependencies, caching strategies, and artifact management.

The agent supports advanced workflow features including matrix builds with dynamic includes/excludes, reusable workflows (workflow_call trigger), composite actions, and environment protection rules. It configures proper concurrency groups to prevent redundant runs and uses GitHub Packages for container registry integration.

Caching is optimized through actions/cache with language-specific key strategies (pip, npm, cargo, gradle). The agent generates workflows for multi-platform testing (ubuntu, windows, macos), deployment gates with manual approval, and scheduled maintenance jobs.

Security hardening includes OIDC token authentication for cloud deployments, pinned action versions with SHA hashes, and minimal GITHUB_TOKEN permissions via permissions key. The agent also configures CodeQL analysis workflows and dependency review enforcement.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill github-actions-ci-pipeline-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill github-actions-ci-pipeline-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill github-actions-ci-pipeline-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill github-actions-ci-pipeline-builder -a codex
```

### OpenClaw

```bash
clawhub install github-actions-ci-pipeline-builder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/github-actions-ci-pipeline-builder/
