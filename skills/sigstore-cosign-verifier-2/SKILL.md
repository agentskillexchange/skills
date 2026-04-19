---
title: "Sigstore Cosign Verifier"
description: "The Sigstore Cosign Verifier skill brings supply chain security verification into AI agent workflows. It wraps the Cosign CLI to verify container image signatures against the Sigstore public-good infrastructure, supporting both key-based and keyless (Fulcio/OIDC) verification modes. The skill queries the Rekor transparency log via its REST API (/api/v1/log/entries) to validate that signatures were recorded in the immutable append-only ledger. It parses Rekor LogEntry objects to extract SignedEntryTimestamp (SET) proofs and verify inclusion against the Rekor tree head. SLSA provenance attestations are verified according to the SLSA v1.0 specification, checking builder identity, source repository, and build configuration against configurable policy files in CUE format. The skill also validates Fulcio certificate chains, checking OIDC issuer claims and Subject Alternative Names (SANs) against organization policy. Integration with OPA (Open Policy Agent) via its REST API enables fine-grained admission control decisions. Results are formatted as in-toto attestation bundles and can be pushed to OCI registries via ORAS."
source: "https://github.com/sigstore/cosign"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "sigstore/cosign"
  github_stars: 5830
---

# Sigstore Cosign Verifier

The Sigstore Cosign Verifier skill brings supply chain security verification into AI agent workflows. It wraps the Cosign CLI to verify container image signatures against the Sigstore public-good infrastructure, supporting both key-based and keyless (Fulcio/OIDC) verification modes. The skill queries the Rekor transparency log via its REST API (/api/v1/log/entries) to validate that signatures were recorded in the immutable append-only ledger. It parses Rekor LogEntry objects to extract SignedEntryTimestamp (SET) proofs and verify inclusion against the Rekor tree head. SLSA provenance attestations are verified according to the SLSA v1.0 specification, checking builder identity, source repository, and build configuration against configurable policy files in CUE format. The skill also validates Fulcio certificate chains, checking OIDC issuer claims and Subject Alternative Names (SANs) against organization policy. Integration with OPA (Open Policy Agent) via its REST API enables fine-grained admission control decisions. Results are formatted as in-toto attestation bundles and can be pushed to OCI registries via ORAS.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sigstore-cosign-verifier-2/)
