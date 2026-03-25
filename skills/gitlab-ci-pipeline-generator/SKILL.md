---
name: "GitLab CI Pipeline Generator"
description: "Creates and manages GitLab CI/CD pipelines via the GitLab REST API v4. Generates .gitlab-ci.yml with multi-stage definitions, DAG dependencies, and environment-scoped deployments."
category: "CI/CD Integrations"
framework: "ChatGPT Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/gitlab-ci-pipeline-generator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "gitlab"  # from ase_tool_match
  github_stars: 24276  # from ase_github_stars (integer, not string)
  github_repo: "gitlabhq/gitlabhq"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# GitLab CI Pipeline Generator

Creates and manages GitLab CI/CD pipelines via the GitLab REST API v4. Generates .gitlab-ci.yml with multi-stage definitions, DAG dependencies, and environment-scoped deployments.

## Overview

The GitLab CI Pipeline Generator skill provides automated pipeline configuration for GitLab CI/CD environments. Using the GitLab REST API v4, it programmatically manages pipeline definitions, job configurations, and deployment environments without requiring manual YAML editing.

The skill generates .gitlab-ci.yml files with proper multi-stage pipeline definitions including build, test, security scanning, and deployment stages. It implements DAG (Directed Acyclic Graph) dependencies using the needs keyword for optimal job parallelization, reducing pipeline execution time by eliminating unnecessary stage-gate waits. Variable management uses GitLab CI/CD variables API to securely store and reference secrets at project and group levels.

Advanced features include generating include directives for shared CI templates from central repositories, configuring Auto DevOps pipelines with custom overrides, and setting up review environments with dynamic environment URLs using the environments API. The skill integrates GitLab Container Registry for Docker image builds, configures SAST/DAST scanning via GitLab Security templates, and manages merge request pipelines with proper rules syntax for branch-based and tag-based triggering. Deployment tracking uses GitLab Releases API for automated changelog generation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-generator -a codex
```

### OpenClaw

```bash
clawhub install gitlab-ci-pipeline-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/gitlab-ci-pipeline-generator/
