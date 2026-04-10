---
name: Tekton Pipeline Composer
description: Builds Tekton CI/CD pipelines on Kubernetes using the Tekton Pipelines
  API and tkn CLI. Composes Tasks, PipelineRuns, and TriggerBindings with proper workspace
  and result propagation between steps.
verification: security_reviewed
source: https://agentskillexchange.com/skills/tekton-pipeline-composer/
category:
- CI/CD Integrations
framework:
- Gemini
---
# Tekton Pipeline Composer

The Tekton Pipeline Composer skill creates and manages cloud-native CI/CD pipelines using the Tekton Pipelines framework on Kubernetes. It generates Task, Pipeline, PipelineRun, and TriggerTemplate custom resource definitions that follow Tekton best practices for workspace sharing and result propagation.
This skill uses the tkn CLI and Kubernetes API to inspect cluster state, list available ClusterTasks, and validate resource definitions before applying them. It understands Tekton workspace types (emptyDir, PVC, ConfigMap, Secret) and ensures proper volume binding across pipeline tasks.
Key features include automatic generation of TriggerBindings and TriggerTemplates for webhook-driven pipelines, EventListener configuration with CEL interceptors for branch filtering, and proper parameterization of pipeline definitions for reuse across environments.
The skill handles complex scenarios like fan-out/fan-in patterns using Tekton's when expressions, matrix parameters for parallel test execution, and custom task result propagation using $(tasks.taskname.results.resultname) syntax. It also integrates with Tekton Chains for supply chain security attestation.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-composer/)
