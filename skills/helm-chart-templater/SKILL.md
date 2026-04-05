---
name: "Helm Chart Templater"
description: "Generates and validates Kubernetes Helm charts using helm template and helm lint APIs. Supports values schema generation via json-schema-generator and chart dependency resolution with helm dependency update."
category: "Templates &amp; Workflows"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/helm-chart-templater/"
---
# Helm Chart Templater

Generates and validates Kubernetes Helm charts using helm template and helm lint APIs. Supports values schema generation via json-schema-generator and chart dependency resolution with helm dependency update.

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

## Details

The Helm Chart Templater automates Kubernetes Helm chart creation, validation, and testing workflows. It generates chart scaffolds with best-practice directory structures including templates for Deployments, Services, Ingress, HPA, PDB, and ServiceMonitor resources. Using helm template, it renders charts locally with different value combinations to validate template logic before deployment. The helm lint API catches common issues like missing required values, invalid YAML syntax, and deprecated API versions. For values.yaml files, it auto-generates JSON Schema definitions using json-schema-generator, enabling IDE autocompletion and validation for chart consumers. The tool runs helm dependency update to resolve and fetch subchart dependencies from OCI registries and traditional Helm repositories. It integrates with helm-unittest for writing and running chart unit tests that verify rendered manifests against expected output. The templater also supports chart version bumping following SemVer conventions and generates CHANGELOG entries from git commit history using conventional-changelog.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/helm-chart-templater/)
