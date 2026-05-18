---
name: "Find deprecated Kubernetes APIs before cluster upgrades with kubent"
slug: "find-deprecated-kubernetes-apis-before-cluster-upgrades-with-kubent"
description: "Scan manifests and live clusters for removed or deprecated Kubernetes APIs before an upgrade window turns into an outage."
github_stars: 3658
verification: "listed"
source: "https://github.com/doitintl/kube-no-trouble"
author: "doitintl"
publisher_type: "organization"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "doitintl/kube-no-trouble"
  github_stars: 3658
---

# Find deprecated Kubernetes APIs before cluster upgrades with kubent

Scan manifests and live clusters for removed or deprecated Kubernetes APIs before an upgrade window turns into an outage.

## Prerequisites

kubent binary, access to target Kubernetes manifests or cluster, target Kubernetes version context for upgrade analysis

## Installation

Use the upstream install or setup path that matches your environment:
- brew install kubent
- $ docker run -it --rm \
- git clone https://github.com/doitintl/kube-no-trouble.git
- $ make

Requirements and caveats from upstream:
- ### Docker Image

Basic usage or getting-started notes:
- Run the following command in your terminal to install kubent using a shell script:
- sh
- sh -c "$(curl -sSL https://git.io/install-kubent)"

- Source: https://github.com/doitintl/kube-no-trouble
- Extracted from upstream docs: https://raw.githubusercontent.com/doitintl/kube-no-trouble/HEAD/README.md

## Documentation

- https://github.com/doitintl/kube-no-trouble#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/find-deprecated-kubernetes-apis-before-cluster-upgrades-with-kubent/)
