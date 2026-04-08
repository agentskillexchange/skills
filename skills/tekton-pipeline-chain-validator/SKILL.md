---
title: Tekton Pipeline Chain Validator
description: The Tekton Pipeline Chain Validator skill enforces supply chain integrity
  for Tekton CI/CD pipelines running on Kubernetes. It queries the Tekton Results
  API to retrieve completed pipeline runs and validates each task image reference
  against Sigstore cosign signatures. The skill verifies SLSA provenance attestations
  using in-toto format, checking builder identity, source repository, and build configuration
  against policy constraints. It supports Tekton Chains integration by validating
  that TaskRun results include proper signed attestations in the transparency log.
  Can enforce policies requiring specific signature thresholds, keyless signing via
  Fulcio certificates, and Rekor log inclusion. Generates compliance reports in SARIF
  format compatible with GitHub Code Scanning. Alerts on unsigned images, expired
  certificates, or provenance gaps via PagerDuty or OpsGenie webhooks.
verification: security_reviewed
source: https://agentskillexchange.com/skills/tekton-pipeline-chain-validator/
category:
- CI/CD Integrations
framework:
- OpenClaw
---

# Tekton Pipeline Chain Validator

The Tekton Pipeline Chain Validator skill enforces supply chain integrity for Tekton CI/CD pipelines running on Kubernetes. It queries the Tekton Results API to retrieve completed pipeline runs and validates each task image reference against Sigstore cosign signatures. The skill verifies SLSA provenance attestations using in-toto format, checking builder identity, source repository, and build configuration against policy constraints. It supports Tekton Chains integration by validating that TaskRun results include proper signed attestations in the transparency log. Can enforce policies requiring specific signature thresholds, keyless signing via Fulcio certificates, and Rekor log inclusion. Generates compliance reports in SARIF format compatible with GitHub Code Scanning. Alerts on unsigned images, expired certificates, or provenance gaps via PagerDuty or OpsGenie webhooks.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-chain-validator/)
