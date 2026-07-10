---
title: "Probe Kubernetes clusters with kube-hunter for exposed services and misconfigurations"
description: "Run a focused exposure probe against a Kubernetes environment before deeper pentest work or remediation planning starts."
verification: "listed"
source: "https://github.com/aquasecurity/kube-hunter"
author: "Aqua Security"
publisher_type: "organization"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "aquasecurity/kube-hunter"
  github_stars: 7267
  npm_package: "kube-hunter"
  npm_weekly_downloads: 0
---

# Probe Kubernetes clusters with kube-hunter for exposed services and misconfigurations

Run a focused exposure probe against a Kubernetes environment before deeper pentest work or remediation planning starts.

## Prerequisites

kube-hunter binary or container image, network access to the target cluster or services, operator-approved scan scope

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install kube-hunter from the upstream release or container image, choose the documented remote or in-cluster scan mode, then run it against the approved target environment and review the findings.
```

## Documentation

- https://github.com/aquasecurity/kube-hunter

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/probe-kubernetes-clusters-with-kube-hunter-for-exposed-services-and-misconfigurations/)
