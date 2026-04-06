---
name: "Tekton Pipeline Template Generator"
description: "Scaffolds Tekton Pipeline and Task CRDs using the Tekton Hub API for reusable task resolution. Leverages tkn CLI for local testing and integrates with Sigstore cosign for supply chain artifact signing and SLSA provenance attestation."
category: "CI/CD Integrations"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/tekton-pipeline-template-generator/"
---
# Tekton Pipeline Template Generator

Scaffolds Tekton Pipeline and Task CRDs using the Tekton Hub API for reusable task resolution. Leverages tkn CLI for local testing and integrates with Sigstore cosign for supply chain artifact signing and SLSA provenance attestation.

Overview

The Tekton Pipeline Template Generator scaffolds production-ready Tekton Pipeline and Task custom resources using reusable components from the Tekton Hub API. It creates idiomatic CI/CD workflows that follow Tekton best practices for cloud-native build automation on Kubernetes.

Key Capabilities

This skill resolves tasks from Tekton Hub using the tkn hub CLI and bundles them as OCI artifacts for air-gapped environments. It generates Pipeline resources with proper workspace bindings, result passing between tasks, and when-expression guards for conditional execution. Local testing is supported through tkn pipeline start with embedded parameter defaults.

Supply Chain Security

Integrates with Sigstore cosign for container image signing and verification within pipeline steps. Generates SLSA provenance attestations using Tekton Chains, configuring the transparency log uploads and attestation storage backends. Supports Tekton Results API for long-term pipeline execution archival and compliance audit trail generation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-template-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-template-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-template-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-template-generator -a codex
```

### OpenClaw

```bash
clawhub install tekton-pipeline-template-generator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-template-generator/)
