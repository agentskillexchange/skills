---
title: "Tekton Pipeline Task Assembler"
description: "Assembles Tekton CI/CD pipelines from reusable Task and ClusterTask definitions using tkn CLI and Tekton Hub catalog. Manages PipelineRun parameters, workspace bindings, and result propagation across task steps."
slug: "tekton-pipeline-task-assembler"
category:
  - "CI/CD Integrations"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/tekton-pipeline-task-assembler/"
listed: true
---

# Tekton Pipeline Task Assembler

Assembles Tekton CI/CD pipelines from reusable Task and ClusterTask definitions using tkn CLI and Tekton Hub catalog. Manages PipelineRun parameters, workspace bindings, and result propagation across task steps.

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
clawhub install tekton-pipeline-task-assembler
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Tekton Pipeline Task Assembler builds cloud-native CI/CD pipelines using Tekton on Kubernetes. It assembles Pipeline resources from reusable Task and ClusterTask definitions, sourcing community tasks from Tekton Hub catalog and combining them with custom tasks for organization-specific workflows. The tkn CLI integration provides pipeline execution, log streaming, and resource management capabilities. The assembler handles PipelineRun parameter propagation, mapping pipeline-level parameters to individual task parameters with type checking and default value resolution. Workspace bindings connect PersistentVolumeClaims, ConfigMaps, and Secrets to task steps, enabling data sharing across pipeline stages. Result propagation chains task outputs to downstream task inputs using the $(tasks.taskname.results.resultname) syntax with validation of result availability. The tool generates TriggerTemplate and TriggerBinding resources for event-driven pipeline execution from GitHub webhooks, GitLab push events, and container registry notifications. Pipeline-as-code with Tekton Chains provides supply chain security through automated artifact signing and attestation generation.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-task-assembler/)
