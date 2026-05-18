---
name: "Cosign Artifact Signature Verifier"
slug: "cosign-artifact-signature-verifier"
description: "Validates container image and artifact signatures using Sigstore Cosign with keyless verification via Fulcio and Rekor transparency logs. Enforces supply chain integrity policies with OPA/Rego."
github_stars: 5837
verification: "listed"
source: "https://github.com/sigstore/cosign"
author: "Sigstore"
category: "Security & Verification"
framework: "Codex"
tool_ecosystem:
  github_repo: "sigstore/cosign"
  github_stars: 5837
---

# Cosign Artifact Signature Verifier

Validates container image and artifact signatures using Sigstore Cosign with keyless verification via Fulcio and Rekor transparency logs. Enforces supply chain integrity policies with OPA/Rego.

## Installation

Use the upstream install or setup path that matches your environment:
- $ git clone https://github.com/sigstore/cosign
- $ go install ./cmd/cosign
- $ docker push $IMAGE_URI

Requirements and caveats from upstream:
- {"Critical":{"Identity":{"docker-reference":""},"Image":{"Docker-manifest-digest":"sha256:87ef60f558bad79beea6425a3b28989f01dd417164150ab3baab98dcbf04def8"},"Type":"cosign container image signature"},"Optional":null}
- **Note:** Most verification workflows require periodically requesting service keys from a TUF repository.
- Verification fails with failed to verify timestamps: threshold not met for verified log entry integrated timestamps: 0 < 1: You may be verifying a signature that requires RFC3161 timestamp support

Basic usage or getting-started notes:
- For Homebrew, Arch, Nix, GitHub Action, and Kubernetes installs see the [installation docs](https://docs.sigstore.dev/cosign/system_config/installation/).
- For Linux and macOS binaries see the [GitHub release assets](https://github.com/sigstore/cosign/releases/latest).
- :rotating_light: If you are downloading releases of cosign from our GCS bucket - please see more information on the July 31, 2023 [deprecation notice](https://blog.sigstore.dev/cosign-releases-bucket-deprecation/) :ro...

- Source: https://github.com/sigstore/cosign
- Extracted from upstream docs: https://raw.githubusercontent.com/sigstore/cosign/HEAD/README.md

## Documentation

- https://docs.sigstore.dev/cosign/overview/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cosign-artifact-signature-verifier/)
