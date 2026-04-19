---
title: "GitLab CI Pipeline Cost Estimator"
description: "The GitLab CI Pipeline Cost Estimator queries the GitLab REST API v4 (/projects/{id}/pipelines and /projects/{id}/jobs) to aggregate job execution data across pipeline runs. It categorizes jobs by runner type (shared Linux, shared Windows, shared macOS, self-hosted), extracting duration and queue time metrics to calculate compute minute consumption. The skill maps usage against GitLab pricing tiers (Free, Premium, Ultimate) with their respective CI/CD minute allowances and overage rates. For self-hosted runners, it estimates infrastructure cost based on reported runner tags that map to instance types (configurable mapping for AWS, GCP, Azure instance pricing). The estimator generates monthly and per-pipeline cost breakdowns, identifies the most expensive jobs and suggests optimization targets (caching improvements, image size reduction, parallelization opportunities). It supports cross-project aggregation for group-level cost reporting and exports data in CSV format for finance team consumption."
source: "https://github.com/gitlabhq/gitlabhq"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "gitlabhq/gitlabhq"
  github_stars: 24298
---

# GitLab CI Pipeline Cost Estimator

The GitLab CI Pipeline Cost Estimator queries the GitLab REST API v4 (/projects/{id}/pipelines and /projects/{id}/jobs) to aggregate job execution data across pipeline runs. It categorizes jobs by runner type (shared Linux, shared Windows, shared macOS, self-hosted), extracting duration and queue time metrics to calculate compute minute consumption. The skill maps usage against GitLab pricing tiers (Free, Premium, Ultimate) with their respective CI/CD minute allowances and overage rates. For self-hosted runners, it estimates infrastructure cost based on reported runner tags that map to instance types (configurable mapping for AWS, GCP, Azure instance pricing). The estimator generates monthly and per-pipeline cost breakdowns, identifies the most expensive jobs and suggests optimization targets (caching improvements, image size reduction, parallelization opportunities). It supports cross-project aggregation for group-level cost reporting and exports data in CSV format for finance team consumption.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-pipeline-cost-estimator/)
