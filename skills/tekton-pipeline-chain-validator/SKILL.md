---
title: "Tekton Pipeline Chain Validator"
description: "Validates Tekton pipeline supply chain security using Sigstore cosign verification and SLSA provenance checks. Ensures all pipeline tasks have signed images and proper attestation metadata via the Tekton Results API."
verification: security_reviewed
source: "https://github.com/tektoncd/pipeline"
category:
  - "CI/CD Integrations"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "tektoncd/pipeline"
  github_stars: 8936
  license: "Apache-2.0"
---

# Tekton Pipeline Chain Validator

The Tekton Pipeline Chain Validator skill enforces supply chain integrity for Tekton CI/CD pipelines running on Kubernetes. It queries the Tekton Results API to retrieve completed pipeline runs and validates each task image reference against Sigstore cosign signatures. The skill verifies SLSA provenance attestations using in-toto format, checking builder identity, source repository, and build configuration against policy constraints. It supports Tekton Chains integration by validating that TaskRun results include proper signed attestations in the transparency log. Can enforce policies requiring specific signature thresholds, keyless signing via Fulcio certificates, and Rekor log inclusion. Generates compliance reports in SARIF format compatible with GitHub Code Scanning. Alerts on unsigned images, expired certificates, or provenance gaps via PagerDuty or OpsGenie webhooks.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/tekton-pipeline-chain-validator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/tekton-pipeline-chain-validator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-chain-validator/)
