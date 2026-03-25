---
name: "Cosign Artifact Signature Verifier"
description: "Validates container image and artifact signatures using Sigstore Cosign with keyless verification via Fulcio and Rekor transparency logs. Enforces supply chain integrity policies with OPA/Rego."
category: "Security & Verification"
framework: "Codex"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/cosign-artifact-signature-verifier/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kubernetes"  # from ase_tool_match
  github_stars: 121313  # from ase_github_stars (integer, not string)
  github_repo: "kubernetes/kubernetes"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Cosign Artifact Signature Verifier

Validates container image and artifact signatures using Sigstore Cosign with keyless verification via Fulcio and Rekor transparency logs. Enforces supply chain integrity policies with OPA/Rego.

## Overview

The Cosign Artifact Signature Verifier skill provides supply chain security verification using **Sigstore Cosign** for container images and software artifacts. It supports both key-based and keyless verification workflows, integrating with Fulcio certificate authority and Rekor transparency log for provenance attestation.

The skill verifies signatures against configurable trust policies, checking certificate identity and issuer claims for keyless signatures. It validates SLSA provenance attestations, ensuring build artifacts originate from trusted CI systems. Integration with OPA (Open Policy Agent) allows defining custom Rego policies for admission control decisions.

Key features include batch verification of multi-architecture image manifests, verification of in-toto attestations for build provenance, and integration with Kubernetes admission controllers like Kyverno and Connaisseur. The skill generates verification reports suitable for compliance audits and supports custom attestation predicates for organizational requirements.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cosign-artifact-signature-verifier
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cosign-artifact-signature-verifier -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cosign-artifact-signature-verifier -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cosign-artifact-signature-verifier -a codex
```

### OpenClaw

```bash
clawhub install cosign-artifact-signature-verifier
```

## Source

- Marketplace: https://agentskillexchange.com/skills/cosign-artifact-signature-verifier/
