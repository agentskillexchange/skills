---
title: "Sigstore Cosign Container Signature Checker"
description: "Checks container trust with `cosign verify`, Rekor transparency log lookups, and OCI image reference inspection. Useful for agents that need to confirm whether an image was actually signed and recorded before it reaches a deployment pipeline."
slug: "sigstore-cosign-container-signature-checker"
category:
  - "Security &amp; Verification"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://github.com/sigstore/cosign"
tool_ecosystem:
  github_repo: "sigstore/cosign"
  github_stars: 5776
listed: true
---

# Sigstore Cosign Container Signature Checker

Checks container trust with `cosign verify`, Rekor transparency log lookups, and OCI image reference inspection. Useful for agents that need to confirm whether an image was actually signed and recorded before it reaches a deployment pipeline.

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
clawhub install sigstore-cosign-container-signature-checker
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Sigstore Cosign Container Signature Checker gives agents a practical way to validate software supply chain claims instead of repeating them. It centers on real Cosign verification behavior, Rekor transparency log lookups, and OCI image reference handling to determine whether a container image has a valid signature trail. That is valuable in CI, release review, and cluster admission workflows where teams want to know if an image was signed, by whom, and whether the verification path matches policy.
The skill can compare image references, inspect signature payload expectations, and distinguish unsigned images from signatures that fail policy or trust-root checks. It is especially helpful for deployment gates and audit preparation, where human reviewers need a crisp explanation rather than just a pass/fail flag. By tying the workflow to Cosign and Rekor primitives, the result stays grounded in the actual verification system rather than an abstract trust story.
Use this skill when container provenance matters, when deployment workflows depend on signed artifacts, and when agents should surface signature evidence before a release moves forward.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sigstore-cosign-container-signature-checker/)
