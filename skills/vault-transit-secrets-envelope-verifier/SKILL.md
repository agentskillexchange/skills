---
title: "Vault Transit Secrets Envelope Verifier"
description: "Verifies encryption workflows with HashiCorp Vault Transit endpoints like `/encrypt`, `/decrypt`, and `/rewrap`, plus key metadata inspection. Useful for agents reviewing whether application secrets handling is actually using envelope encryption correctly instead of assuming the library setup is safe."
verification: security_reviewed
source: "https://github.com/hashicorp/vault"
category:
  - "Security &amp; Verification"
tool_ecosystem:
  github_repo: "hashicorp/vault"
  github_stars: 35321
---

# Vault Transit Secrets Envelope Verifier

Verifies encryption workflows with HashiCorp Vault Transit endpoints like `/encrypt`, `/decrypt`, and `/rewrap`, plus key metadata inspection. Useful for agents reviewing whether application secrets handling is actually using envelope encryption correctly instead of assuming the library setup is safe.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vault-transit-secrets-envelope-verifier/)
