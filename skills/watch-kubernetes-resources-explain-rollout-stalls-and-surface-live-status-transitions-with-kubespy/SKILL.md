---
name: "Watch Kubernetes resources explain rollout stalls and surface live status transitions with kubespy"
slug: "watch-kubernetes-resources-explain-rollout-stalls-and-surface-live-status-transitions-with-kubespy"
description: "Follow a Kubernetes workload live so an agent can explain why it is pending, failing, or not becoming ready."
github_stars: 3056
verification: "security_reviewed"
source: "https://github.com/pulumi/kubespy"
author: "Pulumi"
publisher_type: "organization"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "pulumi/kubespy"
  github_stars: 3056
---

# Watch Kubernetes resources explain rollout stalls and surface live status transitions with kubespy

Follow a Kubernetes workload live so an agent can explain why it is pending, failing, or not becoming ready.

## Prerequisites

kubespy CLI, Kubernetes cluster access

## Installation

Use the upstream install or setup path that matches your environment:
- brew install kubespy
- go install github.com/pulumi/kubespy@latest

Requirements and caveats from upstream:
- Prerequisite: [homebrew](https://docs.brew.sh/Installation)
- Prerequisite: kubectl v1.12.0 or later
- Prerequisite: [Go](https://golang.org/) version 1.19 or later

Basic usage or getting-started notes:
- time,** derived from the work we did to make Kubernetes deployments predictable in [Pulumi's CLI](https://www.pulumi.com/kubernetes/). Run kubespy at any point in time, and it will watch and report information about a
- You can install kubespy in the following ways:
- ### Homebrew (Mac)

- Source: https://github.com/pulumi/kubespy
- Extracted from upstream docs: https://raw.githubusercontent.com/pulumi/kubespy/HEAD/README.md

## Documentation

- https://github.com/pulumi/kubespy

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/watch-kubernetes-resources-explain-rollout-stalls-and-surface-live-status-transitions-with-kubespy/)
