---
title: "Cosign Artifact Signature Verifier"
description: "Validates container image and artifact signatures using Sigstore Cosign with keyless verification via Fulcio and Rekor transparency logs. Enforces supply chain integrity policies with OPA/Rego."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/cosign-artifact-signature-verifier/"
category:
  - "Security &amp; Verification"
framework:
  - "Codex"
---

# Cosign Artifact Signature Verifier

The Cosign Artifact Signature Verifier skill provides supply chain security verification using Sigstore Cosign for container images and software artifacts. It supports both key-based and keyless verification workflows, integrating with Fulcio certificate authority and Rekor transparency log for provenance attestation.

The skill verifies signatures against configurable trust policies, checking certificate identity and issuer claims for keyless signatures. It validates SLSA provenance attestations, ensuring build artifacts originate from trusted CI systems. Integration with OPA (Open Policy Agent) allows defining custom Rego policies for admission control decisions.

Key features include batch verification of multi-architecture image manifests, verification of in-toto attestations for build provenance, and integration with Kubernetes admission controllers like Kyverno and Connaisseur. The skill generates verification reports suitable for compliance audits and supports custom attestation predicates for organizational requirements.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cosign-artifact-signature-verifier/)
