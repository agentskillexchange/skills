---
title: "Seal Kubernetes Secrets into Git-safe manifests with kubeseal"
slug: "seal-kubernetes-secrets-into-git-safe-manifests-with-kubeseal"
description: "Encrypt Kubernetes Secret manifests against a Sealed Secrets controller so agents can commit cluster-targeted secrets to Git without exposing plaintext."
github_stars: 9045
verification: "security_reviewed"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install kubeseal from the Sealed Secrets releases or package manager instructions, fetch or reference the target controller certificate as documented upstream, then run kubeseal against a Kubernetes Secret manifest to emit a SealedSecret for Git-safe storage.
```

## Documentation

- https://github.com/bitnami-labs/sealed-secrets#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/seal-kubernetes-secrets-into-git-safe-manifests-with-kubeseal/)
