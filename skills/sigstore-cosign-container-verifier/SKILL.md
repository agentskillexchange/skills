---
name: "Sigstore Cosign Container Verifier"
description: "Verifies container image signatures and provenance using Sigstore Cosign and Rekor transparency log. Enforces supply chain policies with OPA Gatekeeper admission rules."
category: "Security & Verification"
framework: "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/sigstore-cosign-container-verifier/"
tool_ecosystem:
  tool: kubernetes
  github_stars: 121334
  github_repo: kubernetes/kubernetes
  license: Apache-2.0
  maintained: true
---

# Sigstore Cosign Container Verifier

Verifies container image signatures and provenance using Sigstore Cosign and Rekor transparency log. Enforces supply chain policies with OPA Gatekeeper admission rules.

## Overview

The Sigstore Cosign Container Verifier ensures software supply chain integrity by validating container image signatures and build provenance attestations. It uses Cosign for keyless signing verification and queries the Rekor transparency log for immutable audit records.

The skill verifies SLSA provenance attestations to confirm images were built from trusted source repositories using expected build systems. It checks Fulcio-issued certificates for identity-based signing, validating that the signer matches your organizations OIDC identity provider.

Policy enforcement is implemented through OPA (Open Policy Agent) Gatekeeper constraints that reject unsigned or unverified images at the Kubernetes admission controller level. The agent generates ConstraintTemplate and Constraint resources for common verification policies.

Supports verification of in-toto attestations for build steps, vulnerability scan results, and SBOM attachments stored alongside images in OCI registries. The skill can scan entire Kubernetes clusters to inventory unsigned images and generate compliance reports for SOC2 and FedRAMP requirements.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sigstore-cosign-container-verifier
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sigstore-cosign-container-verifier -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sigstore-cosign-container-verifier -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sigstore-cosign-container-verifier -a codex
```

### OpenClaw

```bash
clawhub install sigstore-cosign-container-verifier
```

## Source

- Marketplace: https://agentskillexchange.com/skills/sigstore-cosign-container-verifier/
