---
title: "Sigstore Cosign Container Verifier"
description: "Verifies container image signatures and provenance using Sigstore Cosign and Rekor transparency log. Enforces supply chain policies with OPA Gatekeeper admission rules."
slug: "sigstore-cosign-container-verifier"
category:
  - "Security &amp; Verification"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/sigstore-cosign-container-verifier/"
---

# Sigstore Cosign Container Verifier

Verifies container image signatures and provenance using Sigstore Cosign and Rekor transparency log. Enforces supply chain policies with OPA Gatekeeper admission rules.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install sigstore-cosign-container-verifier
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Sigstore Cosign Container Verifier ensures software supply chain integrity by validating container image signatures and build provenance attestations. It uses Cosign for keyless signing verification and queries the Rekor transparency log for immutable audit records.
The skill verifies SLSA provenance attestations to confirm images were built from trusted source repositories using expected build systems. It checks Fulcio-issued certificates for identity-based signing, validating that the signer matches your organizations OIDC identity provider.
Policy enforcement is implemented through OPA (Open Policy Agent) Gatekeeper constraints that reject unsigned or unverified images at the Kubernetes admission controller level. The agent generates ConstraintTemplate and Constraint resources for common verification policies.
Supports verification of in-toto attestations for build steps, vulnerability scan results, and SBOM attachments stored alongside images in OCI registries. The skill can scan entire Kubernetes clusters to inventory unsigned images and generate compliance reports for SOC2 and FedRAMP requirements.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sigstore-cosign-container-verifier/)
