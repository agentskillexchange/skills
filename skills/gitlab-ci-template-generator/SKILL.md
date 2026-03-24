---
name: "GitLab CI Template Generator"
description: "Creates GitLab CI/CD pipeline templates using Auto DevOps components, Kaniko for container builds, and SAST/DAST security scanning. Supports multi-project pipelines with trigger and bridge jobs."
category: "CI/CD Integrations"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/gitlab-ci-template-generator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "gitlab"  # from ase_tool_match
  github_stars: 24276  # from ase_github_stars (integer, not string)
  github_repo: "gitlabhq/gitlabhq"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# GitLab CI Template Generator

Creates GitLab CI/CD pipeline templates using Auto DevOps components, Kaniko for container builds, and SAST/DAST security scanning. Supports multi-project pipelines with trigger and bridge jobs.

## Overview

The GitLab CI Template Generator skill produces comprehensive .gitlab-ci.yml configurations leveraging GitLab native CI/CD features and templates. It integrates the Auto DevOps template includes for standardized build-test-deploy stages, uses gcr.io/kaniko-project/executor for rootless container image building without Docker-in-Docker, and configures the SAST and DAST security scanning templates.

The skill generates pipeline configurations with proper cache policies using cache:key:files for lock-file-based cache invalidation, artifacts:reports for code quality and test coverage reporting, and rules-based job inclusion replacing the deprecated only/except syntax. It handles environment-specific deployments with environment:url and environment:auto_stop_in for review app lifecycle management.

Multi-project pipeline support includes trigger jobs with strategy:depend for downstream pipeline monitoring, bridge jobs for cross-project artifact dependencies, and parent-child pipelines using trigger:include for modular configuration. The skill also configures GitLab Releases API integration for automated release creation with release-cli and generates proper services configurations for integration testing with PostgreSQL, Redis, and Elasticsearch containers.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-template-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-template-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-template-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-template-generator -a codex
```

### OpenClaw

```bash
clawhub install gitlab-ci-template-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/gitlab-ci-template-generator/
