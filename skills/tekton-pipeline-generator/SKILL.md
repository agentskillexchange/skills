---
name: "Tekton Pipeline Generator"
description: "Scaffolds Tekton CI/CD pipelines and tasks using the Tekton Hub API and kubectl. Generates PipelineRun manifests with workspace bindings, result propagation, and sidecar configurations."
category: "CI/CD Integrations"
framework: "Gemini"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/tekton-pipeline-generator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "tekton"  # from ase_tool_match
  github_stars: 8920  # from ase_github_stars (integer, not string)
  github_repo: "tektoncd/pipeline"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Tekton Pipeline Generator

Scaffolds Tekton CI/CD pipelines and tasks using the Tekton Hub API and kubectl. Generates PipelineRun manifests with workspace bindings, result propagation, and sidecar configurations.

## Overview

The Tekton Pipeline Generator skill automates the creation of cloud-native CI/CD pipelines using the Tekton Pipelines framework on Kubernetes. It queries the Tekton Hub API to discover reusable tasks for common operations like git-clone, buildah image builds, and vulnerability scanning.

The generator creates complete Pipeline and PipelineRun YAML manifests with properly configured workspace bindings, parameter passing between tasks, and result propagation chains. It handles PersistentVolumeClaim workspace provisioning and configures sidecar containers for services like Docker-in-Docker or database fixtures.

Using kubectl and the Kubernetes API, the skill validates that required Custom Resource Definitions (CRDs) are installed, checks RBAC permissions for pipeline service accounts, and verifies that referenced secrets and config maps exist. It supports Tekton Triggers configuration for webhook-driven pipeline execution from GitHub, GitLab, and Bitbucket.

The skill also generates TektonConfig resources for cluster-wide pipeline settings and supports Tekton Results integration for long-term pipeline run storage and querying.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-generator -a codex
```

### OpenClaw

```bash
clawhub install tekton-pipeline-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/tekton-pipeline-generator/
