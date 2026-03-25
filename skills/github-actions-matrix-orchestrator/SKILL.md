---
name: "GitHub Actions Matrix Orchestrator"
description: "Dynamically generates GitHub Actions matrix strategies using the GitHub REST API and workflow dispatch events. Supports conditional job inclusion via the actions/github-script action and OIDC token federation for cross-account AWS deployments."
category: "CI/CD Integrations"
framework: "Claude Code"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/github-actions-matrix-orchestrator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "aws"  # from ase_tool_match
  github_stars: 3594  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 9204385  # from ase_npm_downloads
  github_repo: "aws/aws-sdk-js-v3"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# GitHub Actions Matrix Orchestrator

Dynamically generates GitHub Actions matrix strategies using the GitHub REST API and workflow dispatch events. Supports conditional job inclusion via the actions/github-script action and OIDC token federation for cross-account AWS deployments.

## Overview

Overview

The GitHub Actions Matrix Orchestrator dynamically generates CI/CD matrix strategies for complex multi-platform builds. By leveraging the GitHub REST API’s workflow dispatch endpoint and the `actions/github-script` action, it creates conditional job matrices that adapt based on changed files, branch names, or PR labels.

Key Capabilities

This skill handles OIDC token federation for cross-account AWS deployments, enabling secure assume-role operations without storing long-lived credentials. It analyzes `dorny/paths-filter` outputs to determine which matrix combinations are necessary, reducing unnecessary CI minutes. The orchestrator supports reusable workflow composition with `workflow_call` triggers and dynamic job generation through JSON matrix output steps.

Technical Integration

Integrates with GitHub’s check runs API for granular status reporting, supports concurrency groups for deployment serialization, and manages artifact retention policies through the actions/upload-artifact v4 API. Compatible with self-hosted runners using custom labels and runner groups.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill github-actions-matrix-orchestrator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill github-actions-matrix-orchestrator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill github-actions-matrix-orchestrator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill github-actions-matrix-orchestrator -a codex
```

### OpenClaw

```bash
clawhub install github-actions-matrix-orchestrator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/github-actions-matrix-orchestrator/
