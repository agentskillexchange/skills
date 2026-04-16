---
title: "Sigstore Cosign Verification Pipeline"
description: "Verifies container image signatures and SBOMs using Sigstore Cosign and Rekor transparency log. Enforces supply chain security policies by validating keyless signatures against Fulcio certificate authorities."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/sigstore-cosign-verification-pipeline/"
category:
  - "Security &amp; Verification"
framework:
  - "Codex"
---

# Sigstore Cosign Verification Pipeline

This skill implements container supply chain security verification using the Sigstore ecosystem. It wraps the Cosign CLI to verify image signatures against Fulcio-issued certificates, checking identity and issuer claims in OIDC tokens. The agent queries the Rekor transparency log to confirm signature inclusion and timestamp validity. For SBOM verification, it validates attached attestations in both CycloneDX and SPDX formats, cross-referencing component hashes against known vulnerability databases via OSV.dev API. The pipeline supports policy enforcement through CUE language constraints, rejecting images that fail signature verification or contain critical CVEs. Integration with Kubernetes admission controllers via Kyverno or OPA Gatekeeper policies ensures only verified images are deployed. The skill generates compliance reports mapping verified artifacts to SLSA provenance levels and NIST SSDF practices.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sigstore-cosign-verification-pipeline/)
