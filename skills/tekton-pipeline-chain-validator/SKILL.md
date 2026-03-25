---
name: "Tekton Pipeline Chain Validator"
description: "Validates Tekton pipeline supply chain security using Sigstore cosign verification and SLSA provenance checks. Ensures all pipeline tasks have signed images and proper attestation metadata via the Tekton Results API."
category: "CI/CD Integrations"
framework: "OpenClaw"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/tekton-pipeline-chain-validator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "tekton"  # from ase_tool_match
  github_stars: 8920  # from ase_github_stars (integer, not string)
  github_repo: "tektoncd/pipeline"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Tekton Pipeline Chain Validator

Validates Tekton pipeline supply chain security using Sigstore cosign verification and SLSA provenance checks. Ensures all pipeline tasks have signed images and proper attestation metadata via the Tekton Results API.

## Overview

The Tekton Pipeline Chain Validator skill enforces supply chain integrity for Tekton CI/CD pipelines running on Kubernetes. It queries the Tekton Results API to retrieve completed pipeline runs and validates each task image reference against Sigstore cosign signatures. The skill verifies SLSA provenance attestations using in-toto format, checking builder identity, source repository, and build configuration against policy constraints. It supports Tekton Chains integration by validating that TaskRun results include proper signed attestations in the transparency log. Can enforce policies requiring specific signature thresholds, keyless signing via Fulcio certificates, and Rekor log inclusion. Generates compliance reports in SARIF format compatible with GitHub Code Scanning. Alerts on unsigned images, expired certificates, or provenance gaps via PagerDuty or OpsGenie webhooks.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-chain-validator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-chain-validator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-chain-validator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-chain-validator -a codex
```

### OpenClaw

```bash
clawhub install tekton-pipeline-chain-validator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/tekton-pipeline-chain-validator/
