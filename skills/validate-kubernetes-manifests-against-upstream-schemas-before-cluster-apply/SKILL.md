---
title: "Validate Kubernetes manifests against upstream schemas before cluster apply"
description: "Uses kubeconform to validate Kubernetes manifests against versioned schemas before anything touches a cluster. The agent can review rendered Helm output, raw manifests, or PR diffs and return invalid resources, missing schemas, and strict-mode failures without requiring live cluster credentials."
verification: "security_reviewed"
source: "https://github.com/yannh/kubeconform"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "yannh/kubeconform"
  github_stars: 2986
---

# Validate Kubernetes manifests against upstream schemas before cluster apply

This entry is built around kubeconform, the manifest validation tool maintained in the yannh/kubeconform repository. The agent job here is concrete: take a set of Kubernetes YAML files, rendered Helm output, or generated deployment artifacts and verify that the resources conform to upstream schemas for the intended Kubernetes version before anyone runs kubectl apply. In practice, the agent uses kubeconform to catch invalid fields, wrong object shapes, duplicated keys in strict mode, and schema mismatches early enough that a release pipeline or reviewer can stop the change before it reaches a live cluster.


You should invoke this skill when an agent is reviewing infrastructure pull requests, preparing a release bundle, validating GitOps repositories, or checking the output of Helm or Kustomize in CI. It is particularly useful when cluster access is unavailable or intentionally restricted, because kubeconform provides a fast static gate that still maps closely to the official Kubernetes API surface. The agent can also summarize which resources were skipped, which CustomResourceDefinition schemas were missing, and which files need a follow-up server-side dry run.


The scope boundary is what keeps this skill from collapsing into a generic Kubernetes product card. kubeconform does not deploy workloads, monitor pods, reconcile drift, or operate clusters. It does one narrow job well: schema-based manifest verification before apply. Integration points include GitHub Actions, GitLab CI, pre-merge checks, Helm rendering pipelines, Kustomize workflows, and agent loops that render manifests, validate them, patch obvious mistakes, and re-run until the bundle is clean.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/validate-kubernetes-manifests-against-upstream-schemas-before-cluster-apply/)
