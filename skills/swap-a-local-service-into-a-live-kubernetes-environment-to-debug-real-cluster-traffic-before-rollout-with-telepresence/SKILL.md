---
name: "Swap a local service into a live Kubernetes environment to debug real cluster traffic before rollout with Telepresence"
slug: "swap-a-local-service-into-a-live-kubernetes-environment-to-debug-real-cluster-traffic-before-rollout-with-telepresence"
description: "Intercept a Kubernetes service and route live cluster traffic into a local process so debugging happens against real dependencies before release."
github_stars: 7183
verification: "security_reviewed"
source: "https://github.com/telepresenceio/telepresence"
author: "telepresenceio"
publisher_type: "organization"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "telepresenceio/telepresence"
  github_stars: 7183
---

# Swap a local service into a live Kubernetes environment to debug real cluster traffic before rollout with Telepresence

Intercept a Kubernetes service and route live cluster traffic into a local process so debugging happens against real dependencies before release.

## Prerequisites

Telepresence CLI, kubectl access, kubeconfig for the target cluster, a locally runnable service, and permission to create intercepts in the namespace

## Installation

Basic usage or getting-started notes:
- Telepresence is a [CNCF](https://www.cncf.io/) project that connects your local workstation to a remote Kubernetes cluster, letting you run services locally while accessing cluster resources. It enables fast local dev...
- **Local Development** - Run services on your workstation using your favorite IDE, debugger, and tools
- [Quick Start Guide](https://telepresence.io/docs/quick-start) - Get up and running in minutes

- Source: https://github.com/telepresenceio/telepresence
- Extracted from upstream docs: https://raw.githubusercontent.com/telepresenceio/telepresence/HEAD/README.md

## Documentation

- https://github.com/telepresenceio/telepresence

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/swap-a-local-service-into-a-live-kubernetes-environment-to-debug-real-cluster-traffic-before-rollout-with-telepresence/)
