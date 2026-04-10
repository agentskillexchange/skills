---
name: Tekton Pipeline Task Assembler
description: Assembles Tekton CI/CD pipelines from reusable Task and ClusterTask definitions
  using tkn CLI and Tekton Hub catalog. Manages PipelineRun parameters, workspace
  bindings, and result propagation across task steps.
verification: security_reviewed
source: https://agentskillexchange.com/skills/tekton-pipeline-task-assembler/
category:
- CI/CD Integrations
framework:
- Gemini
---
# Tekton Pipeline Task Assembler

The Tekton Pipeline Task Assembler builds cloud-native CI/CD pipelines using Tekton on Kubernetes. It assembles Pipeline resources from reusable Task and ClusterTask definitions, sourcing community tasks from Tekton Hub catalog and combining them with custom tasks for organization-specific workflows. The tkn CLI integration provides pipeline execution, log streaming, and resource management capabilities. The assembler handles PipelineRun parameter propagation, mapping pipeline-level parameters to individual task parameters with type checking and default value resolution. Workspace bindings connect PersistentVolumeClaims, ConfigMaps, and Secrets to task steps, enabling data sharing across pipeline stages. Result propagation chains task outputs to downstream task inputs using the $(tasks.taskname.results.resultname) syntax with validation of result availability. The tool generates TriggerTemplate and TriggerBinding resources for event-driven pipeline execution from GitHub webhooks, GitLab push events, and container registry notifications. Pipeline-as-code with Tekton Chains provides supply chain security through automated artifact signing and attestation generation.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-task-assembler/)
