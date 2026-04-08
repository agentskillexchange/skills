---
title: Kubernetes Helm Chart Scaffold Builder
description: This skill creates production-grade Helm v3 chart packages following
  the chart developer guide conventions. It generates Chart.yaml with proper apiVersion
  v2 metadata, dependency declarations, and annotation blocks for ArtifactHub publishing.
  Template files include deployments with resource limits, liveness/readiness probes,
  and pod disruption budgets. Service templates support ClusterIP, NodePort, and LoadBalancer
  types with configurable port mappings. Ingress templates handle both networking.k8s.io/v1
  and legacy extensions/v1beta1 API versions with TLS certificate references. The
  values.yaml file includes JSON Schema validation through values.schema.json generation,
  ensuring type safety for consumer overrides. Helper templates in _helpers.tpl provide
  standard label selectors, naming conventions, and resource annotations. The skill
  runs helm lint for syntax validation and kubeval for Kubernetes API schema conformance.
  Chart testing configurations include ct.yaml for automated testing in CI pipelines.
  NOTES.txt templates provide post-install instructions with dynamic endpoint resolution.
verification: security_reviewed
source: https://agentskillexchange.com/skills/kubernetes-helm-chart-scaffold-builder/
category:
- Templates &amp; Workflows
framework:
- MCP
---

# Kubernetes Helm Chart Scaffold Builder

This skill creates production-grade Helm v3 chart packages following the chart developer guide conventions. It generates Chart.yaml with proper apiVersion v2 metadata, dependency declarations, and annotation blocks for ArtifactHub publishing. Template files include deployments with resource limits, liveness/readiness probes, and pod disruption budgets. Service templates support ClusterIP, NodePort, and LoadBalancer types with configurable port mappings. Ingress templates handle both networking.k8s.io/v1 and legacy extensions/v1beta1 API versions with TLS certificate references. The values.yaml file includes JSON Schema validation through values.schema.json generation, ensuring type safety for consumer overrides. Helper templates in _helpers.tpl provide standard label selectors, naming conventions, and resource annotations. The skill runs helm lint for syntax validation and kubeval for Kubernetes API schema conformance. Chart testing configurations include ct.yaml for automated testing in CI pipelines. NOTES.txt templates provide post-install instructions with dynamic endpoint resolution.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-helm-chart-scaffold-builder/)
