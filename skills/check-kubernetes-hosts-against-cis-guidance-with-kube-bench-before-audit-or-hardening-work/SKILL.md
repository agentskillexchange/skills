---
name: "Check Kubernetes hosts against CIS guidance with kube-bench before audit or hardening work"
slug: "check-kubernetes-hosts-against-cis-guidance-with-kube-bench-before-audit-or-hardening-work"
description: "Run a benchmark-driven posture check on Kubernetes nodes and control planes before an audit, upgrade, or hardening sprint starts."
github_stars: 7788
verification: "security_reviewed"
source: "https://github.com/aquasecurity/kube-bench"
author: "Aqua Security"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "aquasecurity/kube-bench"
  github_stars: 7788
---

# Check Kubernetes hosts against CIS guidance with kube-bench before audit or hardening work

Run a benchmark-driven posture check on Kubernetes nodes and control planes before an audit, upgrade, or hardening sprint starts.

## Prerequisites

kube-bench binary or container image, access to Kubernetes nodes or cluster context, benchmark profile matching the target environment

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

- https://github.com/aquasecurity/kube-bench

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/check-kubernetes-hosts-against-cis-guidance-with-kube-bench-before-audit-or-hardening-work/)
