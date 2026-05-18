---
name: "Lint live Kubernetes clusters for misconfigurations and operational hygiene with Popeye"
slug: "lint-live-kubernetes-clusters-for-misconfigurations-and-operational-hygiene-with-popeye"
description: "Inspect a live Kubernetes cluster for unhealthy resource settings, missing probes, and other operational smells."
github_stars: 6262
verification: "listed"
source: "https://github.com/derailed/popeye"
author: "derailed"
publisher_type: "organization"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "derailed/popeye"
  github_stars: 6262
---

# Lint live Kubernetes clusters for misconfigurations and operational hygiene with Popeye

Inspect a live Kubernetes cluster for unhealthy resource settings, missing probes, and other operational smells.

## Prerequisites

Kubernetes cluster access, Popeye binary

## Installation

Requirements and caveats from upstream:
- # Your cluster must run a metrics-server for these to take place!
- # Configure node resources.
- node:

Basic usage or getting-started notes:
- Furthermore, if your cluster employs a metric-server, it reports potential resources over/under allocations and attempts to warn you should your cluster run out of capacity.
- # NOTE! This will run Popeye in the context namespace if set or like kubectl will use the default namespace
- # Run Popeye in the fred namespace

- Source: https://github.com/derailed/popeye
- Extracted from upstream docs: https://raw.githubusercontent.com/derailed/popeye/HEAD/README.md

## Documentation

- https://github.com/derailed/popeye

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-live-kubernetes-clusters-for-misconfigurations-and-operational-hygiene-with-popeye/)
