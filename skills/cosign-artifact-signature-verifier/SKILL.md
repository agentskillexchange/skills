---
name: Cosign Artifact Signature Verifier
description: Validates container image and artifact signatures using Sigstore Cosign
  with keyless verification via Fulcio and Rekor transparency logs. Enforces supply
  chain integrity policies with OPA/Rego.
verification: security_reviewed
source: https://agentskillexchange.com/skills/cosign-artifact-signature-verifier/
category:
- Security &amp; Verification
framework:
- Codex
---
# Cosign Artifact Signature Verifier

The Cosign Artifact Signature Verifier skill provides supply chain security verification using Sigstore Cosign for container images and software artifacts. It supports both key-based and keyless verification workflows, integrating with Fulcio certificate authority and Rekor transparency log for provenance attestation.
The skill verifies signatures against configurable trust policies, checking certificate identity and issuer claims for keyless signatures. It validates SLSA provenance attestations, ensuring build artifacts originate from trusted CI systems. Integration with OPA (Open Policy Agent) allows defining custom Rego policies for admission control decisions.
Key features include batch verification of multi-architecture image manifests, verification of in-toto attestations for build provenance, and integration with Kubernetes admission controllers like Kyverno and Connaisseur. The skill generates verification reports suitable for compliance audits and supports custom attestation predicates for organizational requirements.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cosign-artifact-signature-verifier/)
