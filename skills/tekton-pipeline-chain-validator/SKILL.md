---
name: "Tekton Pipeline Chain Validator"
slug: "tekton-pipeline-chain-validator"
description: "Validates Tekton pipeline supply chain security using Sigstore cosign verification and SLSA provenance checks. Ensures all pipeline tasks have signed images and proper attestation metadata via the Tekton Results API."
github_stars: 8936
verification: "security_reviewed"
source: "https://github.com/tektoncd/pipeline"
author: "tektoncd"
category: "CI/CD Integrations"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "tektoncd/pipeline"
  github_stars: 8936
---

# Tekton Pipeline Chain Validator

Validates Tekton pipeline supply chain security using Sigstore cosign verification and SLSA provenance checks. Ensures all pipeline tasks have signed images and proper attestation metadata via the Tekton Results API.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Documentation

- https://tekton.dev/docs/pipelines/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-chain-validator/)
