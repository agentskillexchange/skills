---
title: "Cosign Artifact Signature Verifier"
description: "Validates container image and artifact signatures using Sigstore Cosign with keyless verification via Fulcio and Rekor transparency logs. Enforces supply chain integrity policies with OPA/Rego."
verification: "security_reviewed"
source: "https://github.com/sigstore/cosign"
category:
  - "Security & Verification"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "sigstore/cosign"
  github_stars: 5837
---

# Cosign Artifact Signature Verifier

The Cosign Artifact Signature Verifier skill provides supply chain security verification using Sigstore Cosign for container images and software artifacts. It supports both key-based and keyless verification workflows, integrating with Fulcio certificate authority and Rekor transparency log for provenance attestation. The skill verifies signatures against configurable trust policies, checking certificate identity and issuer claims for keyless signatures. It validates SLSA provenance attestations, ensuring build artifacts originate from trusted CI systems. Integration with OPA (Open Policy Agent) allows defining custom Rego policies for admission control decisions. Key features include batch verification of multi-architecture image manifests, verification of in-toto attestations for build provenance, and integration with Kubernetes admission controllers like Kyverno and Connaisseur. The skill generates verification reports suitable for compliance audits and supports custom attestation predicates for organizational requirements.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/cosign-artifact-signature-verifier/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/cosign-artifact-signature-verifier
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/cosign-artifact-signature-verifier`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cosign-artifact-signature-verifier/)
