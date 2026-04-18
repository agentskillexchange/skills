---
title: "Cosign Artifact Signature Verifier"
description: "Validates container image and artifact signatures using Sigstore Cosign with keyless verification via Fulcio and Rekor transparency logs. Enforces supply chain integrity policies with OPA/Rego."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/cosign-artifact-signature-verifier/"
category:
  - "Security & Verification"
framework:
  - "Codex"
---

# Cosign Artifact Signature Verifier

The Cosign Artifact Signature Verifier skill provides supply chain security verification using Sigstore Cosign for container images and software artifacts. It supports both key-based and keyless verification workflows, integrating with Fulcio certificate authority and Rekor transparency log for provenance attestation.

The skill verifies signatures against configurable trust policies, checking certificate identity and issuer claims for keyless signatures. It validates SLSA provenance attestations, ensuring build artifacts originate from trusted CI systems. Integration with OPA (Open Policy Agent) allows defining custom Rego policies for admission control decisions.

Key features include batch verification of multi-architecture image manifests, verification of in-toto attestations for build provenance, and integration with Kubernetes admission controllers like Kyverno and Connaisseur. The skill generates verification reports suitable for compliance audits and supports custom attestation predicates for organizational requirements.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/cosign-artifact-signature-verifier
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/cosign-artifact-signature-verifier` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cosign-artifact-signature-verifier/)
