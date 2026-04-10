---
title: "Tekton Pipeline Composer"
description: "Builds Tekton CI/CD pipelines on Kubernetes using the Tekton Pipelines API and tkn CLI. Composes Tasks, PipelineRuns, and TriggerBindings with proper workspace and result propagation between steps."
slug: "tekton-pipeline-composer"
category:
  - "CI/CD Integrations"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/tekton-pipeline-composer/"
---

# Tekton Pipeline Composer

Builds Tekton CI/CD pipelines on Kubernetes using the Tekton Pipelines API and tkn CLI. Composes Tasks, PipelineRuns, and TriggerBindings with proper workspace and result propagation between steps.

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
clawhub install tekton-pipeline-composer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Tekton Pipeline Composer skill creates and manages cloud-native CI/CD pipelines using the Tekton Pipelines framework on Kubernetes. It generates Task, Pipeline, PipelineRun, and TriggerTemplate custom resource definitions that follow Tekton best practices for workspace sharing and result propagation.
This skill uses the tkn CLI and Kubernetes API to inspect cluster state, list available ClusterTasks, and validate resource definitions before applying them. It understands Tekton workspace types (emptyDir, PVC, ConfigMap, Secret) and ensures proper volume binding across pipeline tasks.
Key features include automatic generation of TriggerBindings and TriggerTemplates for webhook-driven pipelines, EventListener configuration with CEL interceptors for branch filtering, and proper parameterization of pipeline definitions for reuse across environments.
The skill handles complex scenarios like fan-out/fan-in patterns using Tekton’s when expressions, matrix parameters for parallel test execution, and custom task result propagation using $(tasks.taskname.results.resultname) syntax. It also integrates with Tekton Chains for supply chain security attestation.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-composer/)
