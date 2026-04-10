---
name: "Sigstore Cosign Verification Pipeline"
description: "Verifies container image signatures and SBOMs using Sigstore Cosign and Rekor transparency log. Enforces supply chain security policies by validating keyless signatures against Fulcio certificate authorities."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/sigstore-cosign-verification-pipeline/"
category:
  - "Security &amp; Verification"
framework:
  - "Codex"
---

# Sigstore Cosign Verification Pipeline

This skill implements container supply chain security verification using the Sigstore ecosystem. It wraps the Cosign CLI to verify image signatures against Fulcio-issued certificates, checking identity and issuer claims in OIDC tokens. The agent queries the Rekor transparency log to confirm signature inclusion and timestamp validity. For SBOM verification, it validates attached attestations in both CycloneDX and SPDX formats, cross-referencing component hashes against known vulnerability databases via OSV.dev API. The pipeline supports policy enforcement through CUE language constraints, rejecting images that fail signature verification or contain critical CVEs. Integration with Kubernetes admission controllers via Kyverno or OPA Gatekeeper policies ensures only verified images are deployed. The skill generates compliance reports mapping verified artifacts to SLSA provenance levels and NIST SSDF practices.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sigstore-cosign-verification-pipeline/)
