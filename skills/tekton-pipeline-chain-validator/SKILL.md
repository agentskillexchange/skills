---
title: "Tekton Pipeline Chain Validator"
description: "Validates Tekton pipeline supply chain security using Sigstore cosign verification and SLSA provenance checks. Ensures all pipeline tasks have signed images and proper attestation metadata via the Tekton Results API."
slug: "tekton-pipeline-chain-validator"
category:
  - "CI/CD Integrations"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/tekton-pipeline-chain-validator/"
listed: true
---

# Tekton Pipeline Chain Validator

Validates Tekton pipeline supply chain security using Sigstore cosign verification and SLSA provenance checks. Ensures all pipeline tasks have signed images and proper attestation metadata via the Tekton Results API.

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
clawhub install tekton-pipeline-chain-validator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Tekton Pipeline Chain Validator skill enforces supply chain integrity for Tekton CI/CD pipelines running on Kubernetes. It queries the Tekton Results API to retrieve completed pipeline runs and validates each task image reference against Sigstore cosign signatures. The skill verifies SLSA provenance attestations using in-toto format, checking builder identity, source repository, and build configuration against policy constraints. It supports Tekton Chains integration by validating that TaskRun results include proper signed attestations in the transparency log. Can enforce policies requiring specific signature thresholds, keyless signing via Fulcio certificates, and Rekor log inclusion. Generates compliance reports in SARIF format compatible with GitHub Code Scanning. Alerts on unsigned images, expired certificates, or provenance gaps via PagerDuty or OpsGenie webhooks.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-chain-validator/)
