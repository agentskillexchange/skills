---
title: "Sigstore Cosign Container Signature Checker"
slug: "sigstore-cosign-container-signature-checker"
description: "Checks container trust with `cosign verify`, Rekor transparency log lookups, and OCI image reference inspection. Useful for agents that need to confirm whether an image was actually signed and recorded before it reaches a deployment pipeline."
category:
  - "Security &amp; Verification"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://github.com/sigstore/cosign"
tool_ecosystem:
  github_repo: "sigstore/cosign"
  github_stars: 5776
---

# Sigstore Cosign Container Signature Checker

Checks container trust with `cosign verify`, Rekor transparency log lookups, and OCI image reference inspection. Useful for agents that need to confirm whether an image was actually signed and recorded before it reaches a deployment pipeline.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange catalog in your compatible client.
2. Clone or download this repository and copy the skill folder into your local skills directory.
3. Add it as a git submodule inside your skills collection.
4. Use a package or automation workflow that syncs skills from this repository.
5. Install directly from the original upstream project if you prefer to track source releases.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sigstore-cosign-container-signature-checker/)
