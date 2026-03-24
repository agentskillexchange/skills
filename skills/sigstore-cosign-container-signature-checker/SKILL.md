---
name: "Sigstore Cosign Container Signature Checker"
description: "Checks container trust with `cosign verify`, Rekor transparency log lookups, and OCI image reference inspection. Useful for agents that need to confirm whether an image was actually signed and recorded before it reaches a deployment pipeline."
category: "Security & Verification"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/sigstore-cosign-container-signature-checker/"
---

# Sigstore Cosign Container Signature Checker

Checks container trust with `cosign verify`, Rekor transparency log lookups, and OCI image reference inspection. Useful for agents that need to confirm whether an image was actually signed and recorded before it reaches a deployment pipeline.

## Overview

Sigstore Cosign Container Signature Checker gives agents a practical way to validate software supply chain claims instead of repeating them. It centers on real Cosign verification behavior, Rekor transparency log lookups, and OCI image reference handling to determine whether a container image has a valid signature trail. That is valuable in CI, release review, and cluster admission workflows where teams want to know if an image was signed, by whom, and whether the verification path matches policy.

The skill can compare image references, inspect signature payload expectations, and distinguish unsigned images from signatures that fail policy or trust-root checks. It is especially helpful for deployment gates and audit preparation, where human reviewers need a crisp explanation rather than just a pass/fail flag. By tying the workflow to Cosign and Rekor primitives, the result stays grounded in the actual verification system rather than an abstract trust story.

Use this skill when container provenance matters, when deployment workflows depend on signed artifacts, and when agents should surface signature evidence before a release moves forward.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sigstore-cosign-container-signature-checker
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sigstore-cosign-container-signature-checker -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sigstore-cosign-container-signature-checker -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sigstore-cosign-container-signature-checker -a codex
```

### OpenClaw

```bash
clawhub install sigstore-cosign-container-signature-checker
```

## Source

- Marketplace: https://agentskillexchange.com/skills/sigstore-cosign-container-signature-checker/
