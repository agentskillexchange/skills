---
name: "Prometheus Alertmanager Rule Auditor"
slug: "prometheus-alertmanager-rule-auditor"
description: "Validates Prometheus recording and alerting rules using promtool check rules, analyzes Alertmanager routing trees for notification gaps, and tests alert expressions against live TSDB data via the Prometheus HTTP API."
github_stars: 8403
verification: "security_reviewed"
source: "https://github.com/prometheus/alertmanager"
author: "prometheus"
category: "Monitoring & Alerts"
framework: "Gemini"
tool_ecosystem:
  github_repo: "prometheus/alertmanager"
  github_stars: 8403
---

# Prometheus Alertmanager Rule Auditor

Validates Prometheus recording and alerting rules using promtool check rules, analyzes Alertmanager routing trees for notification gaps, and tests alert expressions against live TSDB data via the Prometheus HTTP API.

## Installation

Use the upstream install or setup path that matches your environment:
- Docker images are available on [Quay.io](https://quay.io/repository/prometheus/alertmanager) or [Docker Hub](https://hub.docker.com/r/prom/alertmanager/).
- $ docker run --name alertmanager -d -p 127.0.0.1:9093:9093 quay.io/prometheus/alertmanager
- $ git clone https://github.com/prometheus/alertmanager.git
- $ make build

Requirements and caveats from upstream:
- [![Docker Repository on Quay](https://quay.io/repository/prometheus/alertmanager/status "Docker Repository on Quay")][quay]
- [![Docker Pulls](https://img.shields.io/docker/pulls/prom/alertmanager.svg?maxAge=604800)][hub]
- ### Docker images

Basic usage or getting-started notes:
- There are various ways of installing Alertmanager.
- ### Precompiled binaries
- Precompiled binaries for released versions are available in the

- Source: https://github.com/prometheus/alertmanager
- Extracted from upstream docs: https://raw.githubusercontent.com/prometheus/alertmanager/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-rule-auditor/)
