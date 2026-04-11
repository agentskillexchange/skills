---
title: "Sigstore Cosign Container Signature Checker"
slug: "sigstore-cosign-container-signature-checker"
description: "Checks container trust with `cosign verify`, Rekor transparency log lookups, and OCI image reference inspection. Useful for agents that need to confirm whether an image was actually signed and recorded before it reaches a deployment pipeline."
category: "Security &amp; Verification"
framework: "Claude Code"
verification: "security_reviewed"
source: "https://github.com/sigstore/cosign"
tool_ecosystem:
  github_repo: "sigstore/cosign"
  github_stars: 5776
---

# Sigstore Cosign Container Signature Checker

Checks container trust with `cosign verify`, Rekor transparency log lookups, and OCI image reference inspection. Useful for agents that need to confirm whether an image was actually signed and recorded before it reaches a deployment pipeline.

## Installation

Choose the setup path that fits your environment:

1. Clone or download this skill into your skills directory.
2. Install it through your agent platform's skill manager if supported.
3. Add it as a Git submodule or vendored folder in your repo.
4. Copy the files into a local custom skills/workspace directory.
5. Pull it from the Agent Skill Exchange catalog or this GitHub repo.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sigstore-cosign-container-signature-checker/)
