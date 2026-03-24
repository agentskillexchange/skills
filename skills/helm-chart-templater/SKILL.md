---
name: "Helm Chart Templater"
description: "Generates and validates Kubernetes Helm charts using helm template and helm lint APIs. Supports values schema generation via json-schema-generator and chart dependency resolution with helm dependency update."
category: "Templates & Workflows"
framework: "Gemini"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/helm-chart-templater/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "helm"  # from ase_tool_match
  github_stars: 29603  # from ase_github_stars (integer, not string)
  github_repo: "helm/helm"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Helm Chart Templater

Generates and validates Kubernetes Helm charts using helm template and helm lint APIs. Supports values schema generation via json-schema-generator and chart dependency resolution with helm dependency update.

## Overview

The Helm Chart Templater automates Kubernetes Helm chart creation, validation, and testing workflows. It generates chart scaffolds with best-practice directory structures including templates for Deployments, Services, Ingress, HPA, PDB, and ServiceMonitor resources. Using helm template, it renders charts locally with different value combinations to validate template logic before deployment. The helm lint API catches common issues like missing required values, invalid YAML syntax, and deprecated API versions. For values.yaml files, it auto-generates JSON Schema definitions using json-schema-generator, enabling IDE autocompletion and validation for chart consumers. The tool runs helm dependency update to resolve and fetch subchart dependencies from OCI registries and traditional Helm repositories. It integrates with helm-unittest for writing and running chart unit tests that verify rendered manifests against expected output. The templater also supports chart version bumping following SemVer conventions and generates CHANGELOG entries from git commit history using conventional-changelog.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill helm-chart-templater
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill helm-chart-templater -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill helm-chart-templater -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill helm-chart-templater -a codex
```

### OpenClaw

```bash
clawhub install helm-chart-templater
```

## Source

- Marketplace: https://agentskillexchange.com/skills/helm-chart-templater/
