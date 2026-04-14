---
title: "Sigstore Cosign Verifier"
description: "Automates container image signature verification using Cosign CLI and the Rekor transparency log API. Validates SLSA provenance attestations and checks Fulcio certificate chains for keyless signing."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/sigstore-cosign-verifier-2/"
category:
  - "Security &amp; Verification"
framework:
  - "Cursor"
---

# Sigstore Cosign Verifier

The Sigstore Cosign Verifier skill brings supply chain security verification into AI agent workflows. It wraps the Cosign CLI to verify container image signatures against the Sigstore public-good infrastructure, supporting both key-based and keyless (Fulcio/OIDC) verification modes.

The skill queries the Rekor transparency log via its REST API (/api/v1/log/entries) to validate that signatures were recorded in the immutable append-only ledger. It parses Rekor LogEntry objects to extract SignedEntryTimestamp (SET) proofs and verify inclusion against the Rekor tree head.

SLSA provenance attestations are verified according to the SLSA v1.0 specification, checking builder identity, source repository, and build configuration against configurable policy files in CUE format. The skill also validates Fulcio certificate chains, checking OIDC issuer claims and Subject Alternative Names (SANs) against organization policy. Integration with OPA (Open Policy Agent) via its REST API enables fine-grained admission control decisions. Results are formatted as in-toto attestation bundles and can be pushed to OCI registries via ORAS.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sigstore-cosign-verifier-2/)
