---
title: "Sigstore Cosign Verification Pipeline"
description: "Verifies container image signatures and SBOMs using Sigstore Cosign and Rekor transparency log. Enforces supply chain security policies by validating keyless signatures against Fulcio certificate authorities."
slug: "sigstore-cosign-verification-pipeline"
category:
  - "Security &amp; Verification"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/sigstore-cosign-verification-pipeline/"
listed: true
---

# Sigstore Cosign Verification Pipeline

Verifies container image signatures and SBOMs using Sigstore Cosign and Rekor transparency log. Enforces supply chain security policies by validating keyless signatures against Fulcio certificate authorities.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install sigstore-cosign-verification-pipeline
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill implements container supply chain security verification using the Sigstore ecosystem. It wraps the Cosign CLI to verify image signatures against Fulcio-issued certificates, checking identity and issuer claims in OIDC tokens. The agent queries the Rekor transparency log to confirm signature inclusion and timestamp validity. For SBOM verification, it validates attached attestations in both CycloneDX and SPDX formats, cross-referencing component hashes against known vulnerability databases via OSV.dev API. The pipeline supports policy enforcement through CUE language constraints, rejecting images that fail signature verification or contain critical CVEs. Integration with Kubernetes admission controllers via Kyverno or OPA Gatekeeper policies ensures only verified images are deployed. The skill generates compliance reports mapping verified artifacts to SLSA provenance levels and NIST SSDF practices.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sigstore-cosign-verification-pipeline/)
