---
name: "Kubernetes Helm Chart Scaffold Builder"
description: "Generates Helm v3 chart scaffolds with templated deployments, services, ingress rules, and values.yaml schemas. Validates charts against Helm lint and Kubeval for Kubernetes API version compatibility."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/kubernetes-helm-chart-scaffold-builder/"
category:
  - "Templates &amp; Workflows"
framework:
  - "MCP"
---

# Kubernetes Helm Chart Scaffold Builder

This skill creates production-grade Helm v3 chart packages following the chart developer guide conventions. It generates Chart.yaml with proper apiVersion v2 metadata, dependency declarations, and annotation blocks for ArtifactHub publishing. Template files include deployments with resource limits, liveness/readiness probes, and pod disruption budgets. Service templates support ClusterIP, NodePort, and LoadBalancer types with configurable port mappings. Ingress templates handle both networking.k8s.io/v1 and legacy extensions/v1beta1 API versions with TLS certificate references. The values.yaml file includes JSON Schema validation through values.schema.json generation, ensuring type safety for consumer overrides. Helper templates in _helpers.tpl provide standard label selectors, naming conventions, and resource annotations. The skill runs helm lint for syntax validation and kubeval for Kubernetes API schema conformance. Chart testing configurations include ct.yaml for automated testing in CI pipelines. NOTES.txt templates provide post-install instructions with dynamic endpoint resolution.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-helm-chart-scaffold-builder/)
