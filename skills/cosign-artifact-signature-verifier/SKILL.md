---
title: "Cosign Artifact Signature Verifier"
description: "Validates container image and artifact signatures using Sigstore Cosign with keyless verification via Fulcio and Rekor transparency logs. Enforces supply chain integrity policies with OPA/Rego."
verification: "security_reviewed"
source: "https://github.com/sigstore/cosign"
author: "Sigstore"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "sigstore/cosign"
  github_stars: 5837
---

# Cosign Artifact Signature Verifier

Validates container image and artifact signatures using Sigstore Cosign with keyless verification via Fulcio and Rekor transparency logs. Enforces supply chain integrity policies with OPA/Rego.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Documentation

- https://docs.sigstore.dev/cosign/overview/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cosign-artifact-signature-verifier/)
