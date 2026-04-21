---
title: "Prometheus Alert Tuner"
description: "Tunes Prometheus alerting rules using the Prometheus HTTP API and PromQL query analysis. Reduces alert fatigue by analyzing firing history, adjusting thresholds via histogram_quantile, and configuring inhibition rules."
verification: security_reviewed
source: "https://github.com/prometheus/prometheus"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
---

# Prometheus Alert Tuner

Tunes Prometheus alerting rules using the Prometheus HTTP API and PromQL query analysis. Reduces alert fatigue by analyzing firing history, adjusting thresholds via histogram_quantile, and configuring inhibition rules.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-tuner/)
