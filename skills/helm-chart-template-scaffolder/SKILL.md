---
name: "Helm Chart Template Scaffolder"
description: "Scaffolds Helm 3 chart templates with Go templating best practices. Uses helm-unittest for test generation and Polaris for Kubernetes resource validation scoring."
category: "Templates & Workflows"
framework: "Codex"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/helm-chart-template-scaffolder/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "helm"  # from ase_tool_match
  github_stars: 29610  # from ase_github_stars (integer, not string)
  github_repo: "helm/helm"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Helm Chart Template Scaffolder

Scaffolds Helm 3 chart templates with Go templating best practices. Uses helm-unittest for test generation and Polaris for Kubernetes resource validation scoring.

## Overview

The Helm Chart Template Scaffolder generates production-ready Helm 3 charts from application specifications. It creates properly structured templates using Go template functions from the Sprig library, including conditionals, loops, and named template definitions. Values.yaml files are generated with sensible defaults, JSON Schema validation (values.schema.json), and documented parameters. The skill produces templates for Deployments, Services, Ingresses, ConfigMaps, ServiceAccounts, HorizontalPodAutoscalers, and PodDisruptionBudgets. Each chart includes helm-unittest test suites that verify template rendering with different value combinations. Polaris integration scores generated resources against security and reliability best practices, flagging issues like missing resource limits, running as root, or absent health checks. The skill supports Helm library charts for shared templates and handles chart dependencies with proper version constraints in Chart.yaml.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill helm-chart-template-scaffolder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill helm-chart-template-scaffolder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill helm-chart-template-scaffolder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill helm-chart-template-scaffolder -a codex
```

### OpenClaw

```bash
clawhub install helm-chart-template-scaffolder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/helm-chart-template-scaffolder/
