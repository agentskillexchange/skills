---
name: "GitLab CI Template Library"
description: "Creates reusable GitLab CI/CD template libraries using include:template and extends keywords. Manages pipeline configurations with rules:changes path filtering, needs DAG dependencies, and Auto DevOps customization via CI/CD variables."
category: "CI/CD Integrations"
framework: "MCP-compatible"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/gitlab-ci-template-library/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "gitlab"  # from ase_tool_match
  github_stars: 24276  # from ase_github_stars (integer, not string)
  github_repo: "gitlabhq/gitlabhq"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# GitLab CI Template Library

Creates reusable GitLab CI/CD template libraries using include:template and extends keywords. Manages pipeline configurations with rules:changes path filtering, needs DAG dependencies, and Auto DevOps customization via CI/CD variables.

## Overview

The GitLab CI Template Library skill creates and manages reusable CI/CD template collections for GitLab pipelines. It generates `.gitlab-ci.yml` configurations using the `include:template` directive for referencing shared templates and the `extends` keyword for job inheritance patterns.

This skill builds template libraries organized in GitLab project repositories with proper versioning using Git tags. Templates use `rules:changes` for path-based pipeline filtering, ensuring jobs only run when relevant files are modified. It configures DAG dependencies using the `needs` keyword for parallel stage execution.

For monorepo support, the skill generates parent-child pipeline architectures using `trigger:include` with dynamic child pipeline generation via `generate_ci_config` scripts. It handles multi-project pipelines with cross-project `trigger` configurations and artifact passing between upstream and downstream projects.

Advanced capabilities include Auto DevOps customization through CI/CD variables, `cache` configuration with per-branch key strategies, GitLab Container Registry integration for Docker builds using `kaniko`, review app environments with dynamic URLs, and `release` job configuration for automated changelog generation using `release-cli`.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-template-library
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-template-library -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-template-library -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-template-library -a codex
```

### OpenClaw

```bash
clawhub install gitlab-ci-template-library
```

## Source

- Marketplace: https://agentskillexchange.com/skills/gitlab-ci-template-library/
