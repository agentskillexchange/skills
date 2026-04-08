---
title: GitLab CI Pipeline Cost Estimator
description: The GitLab CI Pipeline Cost Estimator queries the GitLab REST API v4
  (/projects/{id}/pipelines and /projects/{id}/jobs) to aggregate job execution data
  across pipeline runs. It categorizes jobs by runner type (shared Linux, shared Windows,
  shared macOS, self-hosted), extracting duration and queue time metrics to calculate
  compute minute consumption. The skill maps usage against GitLab pricing tiers (Free,
  Premium, Ultimate) with their respective CI/CD minute allowances and overage rates.
  For self-hosted runners, it estimates infrastructure cost based on reported runner
  tags that map to instance types (configurable mapping for AWS, GCP, Azure instance
  pricing). The estimator generates monthly and per-pipeline cost breakdowns, identifies
  the most expensive jobs and suggests optimization targets (caching improvements,
  image size reduction, parallelization opportunities). It supports cross-project
  aggregation for group-level cost reporting and exports data in CSV format for finance
  team consumption.
verification: security_reviewed
source: https://agentskillexchange.com/skills/gitlab-ci-pipeline-cost-estimator/
category:
- CI/CD Integrations
framework:
- Custom Agents
---

# GitLab CI Pipeline Cost Estimator

The GitLab CI Pipeline Cost Estimator queries the GitLab REST API v4 (/projects/{id}/pipelines and /projects/{id}/jobs) to aggregate job execution data across pipeline runs. It categorizes jobs by runner type (shared Linux, shared Windows, shared macOS, self-hosted), extracting duration and queue time metrics to calculate compute minute consumption. The skill maps usage against GitLab pricing tiers (Free, Premium, Ultimate) with their respective CI/CD minute allowances and overage rates. For self-hosted runners, it estimates infrastructure cost based on reported runner tags that map to instance types (configurable mapping for AWS, GCP, Azure instance pricing). The estimator generates monthly and per-pipeline cost breakdowns, identifies the most expensive jobs and suggests optimization targets (caching improvements, image size reduction, parallelization opportunities). It supports cross-project aggregation for group-level cost reporting and exports data in CSV format for finance team consumption.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-pipeline-cost-estimator/)
