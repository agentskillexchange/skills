---
name: "Prometheus AlertManager Router"
slug: "prometheus-alertmanager-router"
description: "Configures and manages Prometheus AlertManager routing trees and silences via the AlertManager HTTP API. Supports PagerDuty, OpsGenie, and Slack receiver configuration with inhibition rules."
github_stars: 63584
verification: "listed"
source: "https://github.com/prometheus/prometheus"
category: "Monitoring & Alerts"
framework: "Cursor"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
---

# Prometheus AlertManager Router

Configures and manages Prometheus AlertManager routing trees and silences via the AlertManager HTTP API. Supports PagerDuty, OpsGenie, and Slack receiver configuration with inhibition rules.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-router/)
