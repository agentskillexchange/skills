---
name: "Sigstore Cosign Verification Pipeline"
description: "Verifies container image signatures and SBOMs using Sigstore Cosign and Rekor transparency log. Enforces supply chain security policies by validating keyless signatures against Fulcio certificate authorities."
category: "Security & Verification"
framework: "Codex"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/sigstore-cosign-verification-pipeline/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kubernetes"  # from ase_tool_match
  github_stars: 121334  # from ase_github_stars (integer, not string)
  github_repo: "kubernetes/kubernetes"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Sigstore Cosign Verification Pipeline

Verifies container image signatures and SBOMs using Sigstore Cosign and Rekor transparency log. Enforces supply chain security policies by validating keyless signatures against Fulcio certificate authorities.

## Overview

This skill implements container supply chain security verification using the Sigstore ecosystem. It wraps the Cosign CLI to verify image signatures against Fulcio-issued certificates, checking identity and issuer claims in OIDC tokens. The agent queries the Rekor transparency log to confirm signature inclusion and timestamp validity. For SBOM verification, it validates attached attestations in both CycloneDX and SPDX formats, cross-referencing component hashes against known vulnerability databases via OSV.dev API. The pipeline supports policy enforcement through CUE language constraints, rejecting images that fail signature verification or contain critical CVEs. Integration with Kubernetes admission controllers via Kyverno or OPA Gatekeeper policies ensures only verified images are deployed. The skill generates compliance reports mapping verified artifacts to SLSA provenance levels and NIST SSDF practices.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sigstore-cosign-verification-pipeline
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sigstore-cosign-verification-pipeline -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sigstore-cosign-verification-pipeline -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sigstore-cosign-verification-pipeline -a codex
```

### OpenClaw

```bash
clawhub install sigstore-cosign-verification-pipeline
```

## Source

- Marketplace: https://agentskillexchange.com/skills/sigstore-cosign-verification-pipeline/
