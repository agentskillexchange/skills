---
title: "Sign agent-made Git commits with gitsign"
description: "Use this skill when an agent needs commit provenance, especially in repos where machine-made changes should still be attributable and verifiable. It fits workflows that want signed commits without managing long-lived GPG keys. Invoke it instead of using gitsign as a raw product when the concrete job is to install the signing path, sign commits during normal Git work, and verify that the resulting signatures are present and usable in review or policy checks. This stays skill-shaped because the scope is a specific operator workflow: sign and verify Git commits with keyless Sigstore identities. It is not a generic Sigstore or supply-chain product card."
source: "https://github.com/sigstore/gitsign"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "sigstore/gitsign"
  github_stars: 1079
---

# Sign agent-made Git commits with gitsign

Use this skill when an agent needs commit provenance, especially in repos where machine-made changes should still be attributable and verifiable. It fits workflows that want signed commits without managing long-lived GPG keys. Invoke it instead of using gitsign as a raw product when the concrete job is to install the signing path, sign commits during normal Git work, and verify that the resulting signatures are present and usable in review or policy checks. This stays skill-shaped because the scope is a specific operator workflow: sign and verify Git commits with keyless Sigstore identities. It is not a generic Sigstore or supply-chain product card.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sign-agent-made-git-commits-with-gitsign/)
