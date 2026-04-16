---
title: "Kubernetes Helm Chart Scaffold Builder"
description: "Generates Helm v3 chart scaffolds with templated deployments, services, ingress rules, and values.yaml schemas. Validates charts against Helm lint and Kubeval for Kubernetes API version compatibility."
verification: "security_reviewed"
source: "https://github.com/helm/helm"
category:
  - "Templates & Workflows"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "helm/helm"
  github_stars: 29697
  license: "Apache-2.0"
---

# Kubernetes Helm Chart Scaffold Builder

This skill creates production-grade Helm v3 chart packages following the chart developer guide conventions. It generates Chart.yaml with proper apiVersion v2 metadata, dependency declarations, and annotation blocks for ArtifactHub publishing. Template files include deployments with resource limits, liveness/readiness probes, and pod disruption budgets. Service templates support ClusterIP, NodePort, and LoadBalancer types with configurable port mappings. Ingress templates handle both networking.k8s.io/v1 and legacy extensions/v1beta1 API versions with TLS certificate references. The values.yaml file includes JSON Schema validation through values.schema.json generation, ensuring type safety for consumer overrides. Helper templates in _helpers.tpl provide standard label selectors, naming conventions, and resource annotations. The skill runs helm lint for syntax validation and kubeval for Kubernetes API schema conformance. Chart testing configurations include ct.yaml for automated testing in CI pipelines. NOTES.txt templates provide post-install instructions with dynamic endpoint resolution.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-helm-chart-scaffold-builder/)
