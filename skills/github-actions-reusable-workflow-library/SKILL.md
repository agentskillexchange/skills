---
name: "GitHub Actions Reusable Workflow Library"
description: "Generates and manages a library of reusable GitHub Actions workflows using workflow_call triggers. Creates parameterized CI/CD templates for Node.js, Python, Rust, and Go projects with matrix strategies, caching, and artifact management."
category: "Templates & Workflows"
framework: "Claude Code"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/github-actions-reusable-workflow-library/"
---

# GitHub Actions Reusable Workflow Library

Generates and manages a library of reusable GitHub Actions workflows using workflow_call triggers. Creates parameterized CI/CD templates for Node.js, Python, Rust, and Go projects with matrix strategies, caching, and artifact management.

## Overview

Overview

The GitHub Actions Reusable Workflow Library skill helps agents build and maintain a centralized repository of reusable CI/CD workflow templates using GitHub Actions’ `workflow_call` trigger. Instead of copying YAML between repositories, this skill generates parameterized workflow files that consuming repos can reference with `uses: org/.github/.github/workflows/ci.yml@main` and pass inputs and secrets via the `with:` and `secrets:` blocks.

How It Works

The agent scaffolds reusable workflow YAML files with properly typed `workflow_call` inputs (string, boolean, number) and secret declarations. It generates language-specific templates: Node.js workflows with `actions/setup-node`, `actions/cache` for node_modules, and matrix strategies across Node 18/20/22; Python workflows with `actions/setup-python`, pip caching, and tox/pytest execution; Rust workflows with `dtolnay/rust-toolchain`, cargo caching via `Swatinem/rust-cache`, and clippy/fmt checks; Go workflows with `actions/setup-go` and golangci-lint. Each template includes concurrency groups, timeout-minutes, and proper permissions blocks.

Output and Management

The skill outputs workflow files to `.github/workflows/` with standardized naming conventions like `reusable-ci-node.yml` and `reusable-deploy-docker.yml`. It generates a caller workflow example for each template showing the correct `uses:` syntax with all available inputs documented. Manages versioning through git tags so consumers can pin to `@v1` or `@v1.2.0`. Includes composite actions in `.github/actions/` for common steps like Docker build-push with `docker/build-push-action`, Terraform plan-apply with `hashicorp/setup-terraform`, and Helm chart deployment with `azure/k8s-deploy`. All generated YAML passes `actionlint` validation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill github-actions-reusable-workflow-library
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill github-actions-reusable-workflow-library -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill github-actions-reusable-workflow-library -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill github-actions-reusable-workflow-library -a codex
```

### OpenClaw

```bash
clawhub install github-actions-reusable-workflow-library
```

## Source

- Marketplace: https://agentskillexchange.com/skills/github-actions-reusable-workflow-library/
