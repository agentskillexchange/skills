---
title: "Prometheus Alert Runbook Linker"
slug: "prometheus-alert-runbook-linker"
description: "Links Prometheus alerting rules to operational runbooks by parsing AlertManager configurations and PrometheusRule CRDs. Validates runbook_url annotations exist and are reachable, and generates stub runbooks for undocumented alerts."
verification: security_reviewed
source: "https://github.com/prometheus/prometheus"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
---

# Prometheus Alert Runbook Linker

Links Prometheus alerting rules to operational runbooks by parsing AlertManager configurations and PrometheusRule CRDs. Validates runbook_url annotations exist and are reachable, and generates stub runbooks for undocumented alerts.

## Installation

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-runbook-linker/)
