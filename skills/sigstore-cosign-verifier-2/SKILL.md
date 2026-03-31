---
name: "Sigstore Cosign Verifier"
description: "Automates container image signature verification using Cosign CLI and the Rekor transparency log API. Validates SLSA provenance attestations and checks Fulcio certificate chains for keyless signing."
category: "Security & Verification"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/sigstore-cosign-verifier-2/"
---
# Sigstore Cosign Verifier

Automates container image signature verification using Cosign CLI and the Rekor transparency log API. Validates SLSA provenance attestations and checks Fulcio certificate chains for keyless signing.

## Overview

The Sigstore Cosign Verifier skill brings supply chain security verification into AI agent workflows. It wraps the Cosign CLI to verify container image signatures against the Sigstore public-good infrastructure, supporting both key-based and keyless (Fulcio/OIDC) verification modes.

The skill queries the Rekor transparency log via its REST API (/api/v1/log/entries) to validate that signatures were recorded in the immutable append-only ledger. It parses Rekor LogEntry objects to extract SignedEntryTimestamp (SET) proofs and verify inclusion against the Rekor tree head.

SLSA provenance attestations are verified according to the SLSA v1.0 specification, checking builder identity, source repository, and build configuration against configurable policy files in CUE format. The skill also validates Fulcio certificate chains, checking OIDC issuer claims and Subject Alternative Names (SANs) against organization policy. Integration with OPA (Open Policy Agent) via its REST API enables fine-grained admission control decisions. Results are formatted as in-toto attestation bundles and can be pushed to OCI registries via ORAS.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sigstore-cosign-verifier-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sigstore-cosign-verifier-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sigstore-cosign-verifier-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sigstore-cosign-verifier-2 -a codex
```

### OpenClaw

```bash
clawhub install sigstore-cosign-verifier-2
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sigstore-cosign-verifier-2/)
