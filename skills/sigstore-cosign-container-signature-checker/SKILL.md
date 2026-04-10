---
name: Sigstore Cosign Container Signature Checker
description: Checks container trust with `cosign verify`, Rekor transparency log lookups,
  and OCI image reference inspection. Useful for agents that need to confirm whether
  an image was actually signed and recorded before it reaches a deployment pipeline.
verification: security_reviewed
source: https://github.com/sigstore/cosign
category:
- Security &amp; Verification
framework:
- Claude Code
tool_ecosystem:
  github_repo: sigstore/cosign
  github_stars: 5776
---
# Sigstore Cosign Container Signature Checker

Sigstore Cosign Container Signature Checker gives agents a practical way to validate software supply chain claims instead of repeating them. It centers on real Cosign verification behavior, Rekor transparency log lookups, and OCI image reference handling to determine whether a container image has a valid signature trail. That is valuable in CI, release review, and cluster admission workflows where teams want to know if an image was signed, by whom, and whether the verification path matches policy.
The skill can compare image references, inspect signature payload expectations, and distinguish unsigned images from signatures that fail policy or trust-root checks. It is especially helpful for deployment gates and audit preparation, where human reviewers need a crisp explanation rather than just a pass/fail flag. By tying the workflow to Cosign and Rekor primitives, the result stays grounded in the actual verification system rather than an abstract trust story.
Use this skill when container provenance matters, when deployment workflows depend on signed artifacts, and when agents should surface signature evidence before a release moves forward.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sigstore-cosign-container-signature-checker/)
