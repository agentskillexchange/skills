---
name: "Tekton Pipeline Template Generator"
description: "Scaffolds Tekton Pipeline and Task CRDs using the Tekton Hub API for reusable task resolution. Leverages tkn CLI for local testing and integrates with Sigstore cosign for supply chain artifact signing and SLSA provenance attestation."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/tekton-pipeline-template-generator/"
category:
  - "CI/CD Integrations"
framework:
  - "MCP"
---

# Tekton Pipeline Template Generator

Overview
The Tekton Pipeline Template Generator scaffolds production-ready Tekton Pipeline and Task custom resources using reusable components from the Tekton Hub API. It creates idiomatic CI/CD workflows that follow Tekton best practices for cloud-native build automation on Kubernetes.
Key Capabilities
This skill resolves tasks from Tekton Hub using the tkn hub CLI and bundles them as OCI artifacts for air-gapped environments. It generates Pipeline resources with proper workspace bindings, result passing between tasks, and when-expression guards for conditional execution. Local testing is supported through tkn pipeline start with embedded parameter defaults.
Supply Chain Security
Integrates with Sigstore cosign for container image signing and verification within pipeline steps. Generates SLSA provenance attestations using Tekton Chains, configuring the transparency log uploads and attestation storage backends. Supports Tekton Results API for long-term pipeline execution archival and compliance audit trail generation.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-template-generator/)
