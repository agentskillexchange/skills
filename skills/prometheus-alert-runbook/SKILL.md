---
name: "Prometheus Alert Runbook"
slug: "prometheus-alert-runbook"
description: "Execute structured runbook procedures triggered by Prometheus AlertManager webhooks. Queries PromQL metrics via the Prometheus HTTP API for automated incident diagnosis and escalation."
github_stars: 63584
verification: "listed"
source: "https://github.com/prometheus/prometheus"
category: "Runbooks & Diagnostics"
framework: "MCP"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
---

# Prometheus Alert Runbook

Execute structured runbook procedures triggered by Prometheus AlertManager webhooks. Queries PromQL metrics via the Prometheus HTTP API for automated incident diagnosis and escalation.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-runbook/)
