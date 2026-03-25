---
name: "GitLab CI Pipeline Cost Estimator"
description: "Estimates CI/CD pipeline costs by querying the GitLab REST API v4 for job durations, runner types, and compute minutes. Maps shared vs self-hosted runner usage against GitLab pricing tiers."
category: "CI/CD Integrations"
framework: "Custom Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/gitlab-ci-pipeline-cost-estimator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "gitlab"  # from ase_tool_match
  github_stars: 24276  # from ase_github_stars (integer, not string)
  github_repo: "gitlabhq/gitlabhq"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# GitLab CI Pipeline Cost Estimator

Estimates CI/CD pipeline costs by querying the GitLab REST API v4 for job durations, runner types, and compute minutes. Maps shared vs self-hosted runner usage against GitLab pricing tiers.

## Overview

The GitLab CI Pipeline Cost Estimator queries the GitLab REST API v4 (/projects/{id}/pipelines and /projects/{id}/jobs) to aggregate job execution data across pipeline runs. It categorizes jobs by runner type (shared Linux, shared Windows, shared macOS, self-hosted), extracting duration and queue time metrics to calculate compute minute consumption. The skill maps usage against GitLab pricing tiers (Free, Premium, Ultimate) with their respective CI/CD minute allowances and overage rates. For self-hosted runners, it estimates infrastructure cost based on reported runner tags that map to instance types (configurable mapping for AWS, GCP, Azure instance pricing). The estimator generates monthly and per-pipeline cost breakdowns, identifies the most expensive jobs and suggests optimization targets (caching improvements, image size reduction, parallelization opportunities). It supports cross-project aggregation for group-level cost reporting and exports data in CSV format for finance team consumption.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-cost-estimator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-cost-estimator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-cost-estimator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-cost-estimator -a codex
```

### OpenClaw

```bash
clawhub install gitlab-ci-pipeline-cost-estimator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/gitlab-ci-pipeline-cost-estimator/
