---
title: "GitLab CI Pipeline Cost Estimator"
description: "The GitLab CI Pipeline Cost Estimator queries the GitLab REST API v4 (/projects/{id}/pipelines and /projects/{id}/jobs) to aggregate job execution data across pipeline runs. It categorizes jobs by runner type (shared Linux, shared Windows, shared macOS, self-hosted), extracting duration and queue time metrics to calculate compute minute consumption. The skill maps usage against GitLab pricing tiers (Free, Premium, Ultimate) with their respective CI/CD minute allowances and overage rates. For self-hosted runners, it estimates infrastructure cost based on reported runner tags that map to instance types (configurable mapping for AWS, GCP, Azure instance pricing). The estimator generates monthly and per-pipeline cost breakdowns, identifies the most expensive jobs and suggests optimization targets (caching improvements, image size reduction, parallelization opportunities). It supports cross-project aggregation for group-level cost reporting and exports data in CSV format for finance team consumption."
verification: security_reviewed
source: "https://github.com/gitlabhq/gitlabhq"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "gitlabhq/gitlabhq"
  github_stars: 24298
---

# GitLab CI Pipeline Cost Estimator

The GitLab CI Pipeline Cost Estimator queries the GitLab REST API v4 (/projects/{id}/pipelines and /projects/{id}/jobs) to aggregate job execution data across pipeline runs. It categorizes jobs by runner type (shared Linux, shared Windows, shared macOS, self-hosted), extracting duration and queue time metrics to calculate compute minute consumption. The skill maps usage against GitLab pricing tiers (Free, Premium, Ultimate) with their respective CI/CD minute allowances and overage rates. For self-hosted runners, it estimates infrastructure cost based on reported runner tags that map to instance types (configurable mapping for AWS, GCP, Azure instance pricing). The estimator generates monthly and per-pipeline cost breakdowns, identifies the most expensive jobs and suggests optimization targets (caching improvements, image size reduction, parallelization opportunities). It supports cross-project aggregation for group-level cost reporting and exports data in CSV format for finance team consumption.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gitlab-ci-pipeline-cost-estimator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/gitlab-ci-pipeline-cost-estimator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-pipeline-cost-estimator/)
