---
title: "Sigstore Cosign Container Verifier"
description: "Verifies container image signatures and provenance using Sigstore Cosign and Rekor transparency log. Enforces supply chain policies with OPA Gatekeeper admission rules."
verification: security_reviewed
source: "https://github.com/sigstore/cosign"
category:
  - "Security & Verification"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "sigstore/cosign"
  github_stars: 5830
---

# Sigstore Cosign Container Verifier

The Sigstore Cosign Container Verifier ensures software supply chain integrity by validating container image signatures and build provenance attestations. It uses Cosign for keyless signing verification and queries the Rekor transparency log for immutable audit records.

The skill verifies SLSA provenance attestations to confirm images were built from trusted source repositories using expected build systems. It checks Fulcio-issued certificates for identity-based signing, validating that the signer matches your organizations OIDC identity provider.

Policy enforcement is implemented through OPA (Open Policy Agent) Gatekeeper constraints that reject unsigned or unverified images at the Kubernetes admission controller level. The agent generates ConstraintTemplate and Constraint resources for common verification policies.

Supports verification of in-toto attestations for build steps, vulnerability scan results, and SBOM attachments stored alongside images in OCI registries. The skill can scan entire Kubernetes clusters to inventory unsigned images and generate compliance reports for SOC2 and FedRAMP requirements.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/sigstore-cosign-container-verifier
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/sigstore-cosign-container-verifier` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sigstore-cosign-container-verifier/)
