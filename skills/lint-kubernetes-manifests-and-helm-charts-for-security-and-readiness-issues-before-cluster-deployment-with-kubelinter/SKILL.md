---
name: "Lint Kubernetes manifests and Helm charts for security and readiness issues before cluster deployment with KubeLinter"
slug: "lint-kubernetes-manifests-and-helm-charts-for-security-and-readiness-issues-before-cluster-deployment-with-kubelinter"
description: "Run a static policy pass over Kubernetes YAML before misconfigurations, missing limits, or risky defaults reach a cluster."
github_stars: 3437
verification: "security_reviewed"
source: "https://github.com/stackrox/kube-linter"
author: "StackRox"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "stackrox/kube-linter"
  github_stars: 3437
---

# Lint Kubernetes manifests and Helm charts for security and readiness issues before cluster deployment with KubeLinter

Run a static policy pass over Kubernetes YAML before misconfigurations, missing limits, or risky defaults reach a cluster.

## Prerequisites

KubeLinter binary or container image, Kubernetes YAML or Helm/Kustomize inputs, and optional CI integration.

## Installation

Use the upstream install or setup path that matches your environment:
- go install golang.stackrox.io/kube-linter/cmd/kube-linter@latest
- brew install kube-linter
- docker pull stackrox/kube-linter:latest
- git clone git@github.com:stackrox/kube-linter.git

Requirements and caveats from upstream:
- ### Using docker
- Running KubeLinter to Lint your YAML files only requires two steps in its most basic form.

Basic usage or getting-started notes:
- To install using [Go](https://golang.org/), run the following command:
- To install using Homebrew or LinuxBrew, run the following command:
- Make sure that you have [installed Go](https://golang.org/doc/install) prior to building from source.

- Source: https://github.com/stackrox/kube-linter
- Extracted from upstream docs: https://raw.githubusercontent.com/stackrox/kube-linter/HEAD/README.md

## Documentation

- https://github.com/stackrox/kube-linter

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-kubernetes-manifests-and-helm-charts-for-security-and-readiness-issues-before-cluster-deployment-with-kubelinter/)
