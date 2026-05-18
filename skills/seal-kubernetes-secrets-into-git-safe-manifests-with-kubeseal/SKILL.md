---
name: "Seal Kubernetes Secrets into Git-safe manifests with kubeseal"
slug: "seal-kubernetes-secrets-into-git-safe-manifests-with-kubeseal"
description: "Encrypt Kubernetes Secret manifests against a Sealed Secrets controller so agents can commit cluster-targeted secrets to Git without exposing plaintext."
github_stars: 9045
verification: "listed"
source: "https://github.com/bitnami-labs/sealed-secrets"
author: "bitnami-labs"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "bitnami-labs/sealed-secrets"
  github_stars: 9045
---

# Seal Kubernetes Secrets into Git-safe manifests with kubeseal

Encrypt Kubernetes Secret manifests against a Sealed Secrets controller so agents can commit cluster-targeted secrets to Git without exposing plaintext.

## Prerequisites

kubeseal CLI, access to the target Sealed Secrets controller certificate or cluster, kubectl-compatible Secret manifest input

## Installation

Use the upstream install or setup path that matches your environment:
- brew install kubeseal
- go install github.com/bitnami-labs/sealed-secrets/cmd/kubeseal@main

Requirements and caveats from upstream:
- [![Download Status](https://img.shields.io/docker/pulls/bitnami/sealed-secrets-controller.svg)](https://hub.docker.com/r/bitnami/sealed-secrets-controller)
- (requires secure access to the Kubernetes API server), which is
- A cluster administrator must have already installed the SealedSecret CRDs.

Basic usage or getting-started notes:
- <!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
- [Usage](#usage)
- The [Usage](#usage) section explores in more detail how you craft SealedSecret resources.

- Source: https://github.com/bitnami-labs/sealed-secrets
- Extracted from upstream docs: https://raw.githubusercontent.com/bitnami-labs/sealed-secrets/HEAD/README.md

## Documentation

- https://github.com/bitnami-labs/sealed-secrets#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/seal-kubernetes-secrets-into-git-safe-manifests-with-kubeseal/)
