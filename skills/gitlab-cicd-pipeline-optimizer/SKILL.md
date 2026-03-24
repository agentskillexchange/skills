---
name: "GitLab CI/CD Pipeline Optimizer"
description: "Optimizes GitLab CI/CD pipelines using the .gitlab-ci.yml specification and GitLab API v4. Implements DAG pipelines, parallel testing, and dynamic child pipelines."
category: "CI/CD Integrations"
framework: "ChatGPT Agents"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/gitlab-cicd-pipeline-optimizer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "gitlab"  # from ase_tool_match
  github_stars: 24276  # from ase_github_stars (integer, not string)
  github_repo: "gitlabhq/gitlabhq"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# GitLab CI/CD Pipeline Optimizer

Optimizes GitLab CI/CD pipelines using the .gitlab-ci.yml specification and GitLab API v4. Implements DAG pipelines, parallel testing, and dynamic child pipelines.

## Overview

The GitLab CI/CD Pipeline Optimizer analyzes and improves GitLab CI/CD configurations using the .gitlab-ci.yml specification and GitLab REST API v4 (/api/v4/projects/{id}/pipelines, /jobs, /bridges). It restructures pipeline stages for maximum parallelism and minimum execution time.

The agent implements Directed Acyclic Graph (DAG) pipelines using the needs keyword to break sequential stage dependencies. It configures parallel keyword for test splitting, rules-based job inclusion for merge request pipelines, and extends/include for DRY configuration across projects.

Dynamic child pipelines are generated using trigger:include for monorepo workflows, with parent-child pipeline communication via dotenv artifacts. The agent optimizes Docker layer caching through kaniko builds and GitLab Container Registry integration.

Advanced features include Auto DevOps customization, review app configuration with dynamic environments, and pipeline efficiency metrics tracking. The agent monitors pipeline analytics via the API and suggests optimizations based on job duration trends, failure rates, and resource utilization patterns.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gitlab-cicd-pipeline-optimizer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gitlab-cicd-pipeline-optimizer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gitlab-cicd-pipeline-optimizer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gitlab-cicd-pipeline-optimizer -a codex
```

### OpenClaw

```bash
clawhub install gitlab-cicd-pipeline-optimizer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/gitlab-cicd-pipeline-optimizer/
