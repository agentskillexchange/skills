---
title: "Sigstore Cosign Container Verifier"
description: "Verifies container image signatures and provenance using Sigstore Cosign and Rekor transparency log. Enforces supply chain policies with OPA Gatekeeper admission rules."
verification: "security_reviewed"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sigstore-cosign-container-verifier/)
