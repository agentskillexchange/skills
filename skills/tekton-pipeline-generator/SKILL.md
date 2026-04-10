---
name: Tekton Pipeline Generator
description: Scaffolds Tekton CI/CD pipelines and tasks using the Tekton Hub API and
  kubectl. Generates PipelineRun manifests with workspace bindings, result propagation,
  and sidecar configurations.
verification: security_reviewed
source: https://agentskillexchange.com/skills/tekton-pipeline-generator/
category:
- CI/CD Integrations
framework:
- Gemini
---
# Tekton Pipeline Generator

The Tekton Pipeline Generator skill automates the creation of cloud-native CI/CD pipelines using the Tekton Pipelines framework on Kubernetes. It queries the Tekton Hub API to discover reusable tasks for common operations like git-clone, buildah image builds, and vulnerability scanning.
The generator creates complete Pipeline and PipelineRun YAML manifests with properly configured workspace bindings, parameter passing between tasks, and result propagation chains. It handles PersistentVolumeClaim workspace provisioning and configures sidecar containers for services like Docker-in-Docker or database fixtures.
Using kubectl and the Kubernetes API, the skill validates that required Custom Resource Definitions (CRDs) are installed, checks RBAC permissions for pipeline service accounts, and verifies that referenced secrets and config maps exist. It supports Tekton Triggers configuration for webhook-driven pipeline execution from GitHub, GitLab, and Bitbucket.
The skill also generates TektonConfig resources for cluster-wide pipeline settings and supports Tekton Results integration for long-term pipeline run storage and querying.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-generator/)
