---
name: Tekton Pipeline Chain Validator
description: Validates Tekton pipeline supply chain security using Sigstore cosign
  verification and SLSA provenance checks. Ensures all pipeline tasks have signed
  images and proper attestation metadata via the Tekton Results API.
category: CI/CD Integrations
framework: OpenClaw
verification: security_reviewed
source: https://github.com/tektoncd/pipeline
tool_ecosystem:
  github_repo: tektoncd/pipeline
  github_stars: 8936
  tool: pipeline
  license: Apache-2.0
  maintained: true
---
# Tekton Pipeline Chain Validator
Validates Tekton pipeline supply chain security using Sigstore cosign verification and SLSA provenance checks. Ensures all pipeline tasks have signed images and proper attestation metadata via the Tekton Results API.

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
