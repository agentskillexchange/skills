---
name: "Benchmark Kubernetes clusters against CIS controls with kube-bench"
slug: "benchmark-kubernetes-clusters-against-cis-controls-with-kube-bench"
description: "Run CIS benchmark checks against cluster nodes and control planes when an agent needs a narrow Kubernetes hardening audit, not a general platform listing."
github_stars: 8022
verification: "security_reviewed"
source: "https://github.com/aquasecurity/kube-bench"
author: "Aqua Security"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "aquasecurity/kube-bench"
  github_stars: 8022
---

# Benchmark Kubernetes clusters against CIS controls with kube-bench

Run CIS benchmark checks against cluster nodes and control planes when an agent needs a narrow Kubernetes hardening audit, not a general platform listing.

## Prerequisites

kube-bench binary or container image, access to target Kubernetes nodes or cluster context

## Installation

Requirements and caveats from upstream:
- [![Docker Pulls][docker-pull]][docker]
- [docker-pull]: https://img.shields.io/docker/pulls/aquasec/kube-bench?logo=docker&label=docker%20pulls%20%2F%20kube-bench
- [docker]: https://hub.docker.com/r/aquasec/kube-bench

Basic usage or getting-started notes:
- There are multiple ways to run kube-bench.
- You can run kube-bench inside a pod, but it will need access to the host's PID namespace in order to check the running processes, as well as access to some directories on the host where config files and other files ar...
- The supplied job.yaml [file](job.yaml) can be applied to run the tests as a job. For example:

- Source: https://github.com/aquasecurity/kube-bench
- Extracted from upstream docs: https://raw.githubusercontent.com/aquasecurity/kube-bench/HEAD/README.md

## Documentation

- https://github.com/aquasecurity/kube-bench#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/benchmark-kubernetes-clusters-against-cis-controls-with-kube-bench/)
