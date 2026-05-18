---
name: "Prometheus Alert Tuner"
slug: "prometheus-alert-tuner"
description: "Tunes Prometheus alerting rules using the Prometheus HTTP API and PromQL query analysis. Reduces alert fatigue by analyzing firing history, adjusting thresholds via histogram_quantile, and configuring inhibition rules."
github_stars: 63584
verification: "security_reviewed"
source: "https://github.com/prometheus/prometheus"
category: "Runbooks & Diagnostics"
framework: "Gemini"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
---

# Prometheus Alert Tuner

Tunes Prometheus alerting rules using the Prometheus HTTP API and PromQL query analysis. Reduces alert fatigue by analyzing firing history, adjusting thresholds via histogram_quantile, and configuring inhibition rules.

## Installation

Use the upstream install or setup path that matches your environment:
- Docker images are available on [Quay.io](https://quay.io/repository/prometheus/prometheus) or [Docker Hub](https://hub.docker.com/r/prom/prometheus/).
- docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus
- git clone https://github.com/prometheus/prometheus.git
- go install github.com/prometheus/prometheus/cmd/...

Requirements and caveats from upstream:
- [![Docker Repository on Quay](https://quay.io/repository/prometheus/prometheus/status)][quay]
- [![Docker Pulls](https://img.shields.io/docker/pulls/prom/prometheus.svg?maxAge=604800)][hub]
- ### Docker images

Basic usage or getting-started notes:
- There are various ways to install Prometheus.
- ### Precompiled binaries
- Precompiled binaries for released versions are available in the

- Source: https://github.com/prometheus/prometheus
- Extracted from upstream docs: https://raw.githubusercontent.com/prometheus/prometheus/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-tuner/)
