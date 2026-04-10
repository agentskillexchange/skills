---
name: "Sigstore Cosign Container Verifier"
description: "Verifies container image signatures and provenance using Sigstore Cosign and Rekor transparency log. Enforces supply chain policies with OPA Gatekeeper admission rules."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/sigstore-cosign-container-verifier/"
category:
  - "Security &amp; Verification"
framework:
  - "MCP"
---

# Sigstore Cosign Container Verifier

The Sigstore Cosign Container Verifier ensures software supply chain integrity by validating container image signatures and build provenance attestations. It uses Cosign for keyless signing verification and queries the Rekor transparency log for immutable audit records.
The skill verifies SLSA provenance attestations to confirm images were built from trusted source repositories using expected build systems. It checks Fulcio-issued certificates for identity-based signing, validating that the signer matches your organizations OIDC identity provider.
Policy enforcement is implemented through OPA (Open Policy Agent) Gatekeeper constraints that reject unsigned or unverified images at the Kubernetes admission controller level. The agent generates ConstraintTemplate and Constraint resources for common verification policies.
Supports verification of in-toto attestations for build steps, vulnerability scan results, and SBOM attachments stored alongside images in OCI registries. The skill can scan entire Kubernetes clusters to inventory unsigned images and generate compliance reports for SOC2 and FedRAMP requirements.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sigstore-cosign-container-verifier/)
