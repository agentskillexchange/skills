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
---

# Tekton Pipeline Chain Validator

The Tekton Pipeline Chain Validator skill enforces supply chain integrity for Tekton CI/CD pipelines running on Kubernetes. It queries the Tekton Results API to retrieve completed pipeline runs and validates each task image reference against Sigstore cosign signatures. The skill verifies SLSA provenance attestations using in-toto format, checking builder identity, source repository, and build configuration against policy constraints. It supports Tekton Chains integration by validating that TaskRun results include proper signed attestations in the transparency log. Can enforce policies requiring specific signature thresholds, keyless signing via Fulcio certificates, and Rekor log inclusion. Generates compliance reports in SARIF format compatible with GitHub Code Scanning. Alerts on unsigned images, expired certificates, or provenance gaps via PagerDuty or OpsGenie webhooks.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-chain-validator/)
