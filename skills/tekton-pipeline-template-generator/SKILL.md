---
title: "Tekton Pipeline Template Generator"
description: "Scaffolds Tekton Pipeline and Task CRDs using the Tekton Hub API for reusable task resolution. Leverages tkn CLI for local testing and integrates with Sigstore cosign for supply chain artifact signing and SLSA provenance attestation."
slug: "tekton-pipeline-template-generator"
category:
  - "CI/CD Integrations"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/tekton-pipeline-template-generator/"
listed: true
---

# Tekton Pipeline Template Generator

Scaffolds Tekton Pipeline and Task CRDs using the Tekton Hub API for reusable task resolution. Leverages tkn CLI for local testing and integrates with Sigstore cosign for supply chain artifact signing and SLSA provenance attestation.

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
clawhub install tekton-pipeline-template-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Overview
The Tekton Pipeline Template Generator scaffolds production-ready Tekton Pipeline and Task custom resources using reusable components from the Tekton Hub API. It creates idiomatic CI/CD workflows that follow Tekton best practices for cloud-native build automation on Kubernetes.
Key Capabilities
This skill resolves tasks from Tekton Hub using the tkn hub CLI and bundles them as OCI artifacts for air-gapped environments. It generates Pipeline resources with proper workspace bindings, result passing between tasks, and when-expression guards for conditional execution. Local testing is supported through tkn pipeline start with embedded parameter defaults.
Supply Chain Security
Integrates with Sigstore cosign for container image signing and verification within pipeline steps. Generates SLSA provenance attestations using Tekton Chains, configuring the transparency log uploads and attestation storage backends. Supports Tekton Results API for long-term pipeline execution archival and compliance audit trail generation.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-template-generator/)
