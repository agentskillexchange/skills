---
title: "Sigstore Cosign Container Signature Checker"
description: "Checks container trust with `cosign verify`, Rekor transparency log lookups, and OCI image reference inspection. Useful for agents that need to confirm whether an image was actually signed and recorded before it reaches a deployment pipeline."
verification: "security_reviewed"
source: "https://github.com/sigstore/cosign"
category:
  - "Security & Verification"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "sigstore/cosign"
  github_stars: 5776
---
# Sigstore Cosign Container Signature Checker

Checks container trust with `cosign verify`, Rekor transparency log lookups, and OCI image reference inspection. Useful for agents that need to confirm whether an image was actually signed and recorded before it reaches a deployment pipeline.

## Installation

You can install this skill in a few common ways:

1. Browse and install from Agent Skill Exchange in the UI if your client supports it.
2. Install from a local skill folder by copying it into your skills directory.
3. Add it as a git submodule or vendor it into your shared skills repo.
4. Fetch it with your preferred skill or package workflow if the upstream project publishes one.
5. Follow the upstream project documentation for manual setup and dependencies.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sigstore-cosign-container-signature-checker/)
