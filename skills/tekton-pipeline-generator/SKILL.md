---
title: "Tekton Pipeline Generator"
description: "Scaffolds Tekton CI/CD pipelines and tasks using the Tekton Hub API and kubectl. Generates PipelineRun manifests with workspace bindings, result propagation, and sidecar configurations."
slug: "tekton-pipeline-generator"
category:
  - "CI/CD Integrations"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/tekton-pipeline-generator/"
---

# Tekton Pipeline Generator

Scaffolds Tekton CI/CD pipelines and tasks using the Tekton Hub API and kubectl. Generates PipelineRun manifests with workspace bindings, result propagation, and sidecar configurations.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install tekton-pipeline-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Tekton Pipeline Generator skill automates the creation of cloud-native CI/CD pipelines using the Tekton Pipelines framework on Kubernetes. It queries the Tekton Hub API to discover reusable tasks for common operations like git-clone, buildah image builds, and vulnerability scanning.
The generator creates complete Pipeline and PipelineRun YAML manifests with properly configured workspace bindings, parameter passing between tasks, and result propagation chains. It handles PersistentVolumeClaim workspace provisioning and configures sidecar containers for services like Docker-in-Docker or database fixtures.
Using kubectl and the Kubernetes API, the skill validates that required Custom Resource Definitions (CRDs) are installed, checks RBAC permissions for pipeline service accounts, and verifies that referenced secrets and config maps exist. It supports Tekton Triggers configuration for webhook-driven pipeline execution from GitHub, GitLab, and Bitbucket.
The skill also generates TektonConfig resources for cluster-wide pipeline settings and supports Tekton Results integration for long-term pipeline run storage and querying.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-generator/)
