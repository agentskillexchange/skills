---
name: "Kubernetes Helm Chart Scaffold Builder"
description: "Generates Helm v3 chart scaffolds with templated deployments, services, ingress rules, and values.yaml schemas. Validates charts against Helm lint and Kubeval for Kubernetes API version compatibility."
category: "Templates & Workflows"
framework: "MCP-compatible"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/kubernetes-helm-chart-scaffold-builder/"
tool_ecosystem:
  tool: "helm"
  github_stars: 29610
  github_repo: "helm/helm"
  license: "Apache-2.0"
  maintained: true
---

# Kubernetes Helm Chart Scaffold Builder

Generates Helm v3 chart scaffolds with templated deployments, services, ingress rules, and values.yaml schemas. Validates charts against Helm lint and Kubeval for Kubernetes API version compatibility.

## Overview

This skill creates production-grade Helm v3 chart packages following the chart developer guide conventions. It generates Chart.yaml with proper apiVersion v2 metadata, dependency declarations, and annotation blocks for ArtifactHub publishing. Template files include deployments with resource limits, liveness/readiness probes, and pod disruption budgets. Service templates support ClusterIP, NodePort, and LoadBalancer types with configurable port mappings. Ingress templates handle both networking.k8s.io/v1 and legacy extensions/v1beta1 API versions with TLS certificate references. The values.yaml file includes JSON Schema validation through values.schema.json generation, ensuring type safety for consumer overrides. Helper templates in _helpers.tpl provide standard label selectors, naming conventions, and resource annotations. The skill runs helm lint for syntax validation and kubeval for Kubernetes API schema conformance. Chart testing configurations include ct.yaml for automated testing in CI pipelines. NOTES.txt templates provide post-install instructions with dynamic endpoint resolution.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill kubernetes-helm-chart-scaffold-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-helm-chart-scaffold-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-helm-chart-scaffold-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-helm-chart-scaffold-builder -a codex
```

### OpenClaw

```bash
clawhub install kubernetes-helm-chart-scaffold-builder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/kubernetes-helm-chart-scaffold-builder/
