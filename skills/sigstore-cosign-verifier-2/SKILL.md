---
title: "Sigstore Cosign Verifier"
description: "The Sigstore Cosign Verifier skill brings supply chain security verification into AI agent workflows. It wraps the Cosign CLI to verify container image signatures against the Sigstore public-good infrastructure, supporting both key-based and keyless (Fulcio/OIDC) verification modes.\nThe skill queries the Rekor transparency log via its REST API (/api/v1/log/entries) to validate that signatures were recorded in the immutable append-only ledger. It parses Rekor LogEntry objects to extract SignedEntryTimestamp (SET) proofs and verify inclusion against the Rekor tree head.\nSLSA provenance attestations are verified according to the SLSA v1.0 specification, checking builder identity, source repository, and build configuration against configurable policy files in CUE format. The skill also validates Fulcio certificate chains, checking OIDC issuer claims and Subject Alternative Names (SANs) against organization policy. Integration with OPA (Open Policy Agent) via its REST API enables fine-grained admission control decisions. Results are formatted as in-toto attestation bundles and can be pushed to OCI registries via ORAS."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/sigstore-cosign-verifier-2/"
framework:
  - "Cursor"
---

# Sigstore Cosign Verifier

The Sigstore Cosign Verifier skill brings supply chain security verification into AI agent workflows. It wraps the Cosign CLI to verify container image signatures against the Sigstore public-good infrastructure, supporting both key-based and keyless (Fulcio/OIDC) verification modes.
The skill queries the Rekor transparency log via its REST API (/api/v1/log/entries) to validate that signatures were recorded in the immutable append-only ledger. It parses Rekor LogEntry objects to extract SignedEntryTimestamp (SET) proofs and verify inclusion against the Rekor tree head.
SLSA provenance attestations are verified according to the SLSA v1.0 specification, checking builder identity, source repository, and build configuration against configurable policy files in CUE format. The skill also validates Fulcio certificate chains, checking OIDC issuer claims and Subject Alternative Names (SANs) against organization policy. Integration with OPA (Open Policy Agent) via its REST API enables fine-grained admission control decisions. Results are formatted as in-toto attestation bundles and can be pushed to OCI registries via ORAS.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/sigstore-cosign-verifier-2
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/sigstore-cosign-verifier-2` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sigstore-cosign-verifier-2/)
