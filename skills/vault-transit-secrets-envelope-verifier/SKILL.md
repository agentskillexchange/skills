---
title: "Vault Transit Secrets Envelope Verifier"
slug: "vault-transit-secrets-envelope-verifier"
verification: "security_reviewed"
description: "Verifies encryption workflows with HashiCorp Vault Transit endpoints like `/encrypt`, `/decrypt`, and `/rewrap`, plus key metadata inspection. Useful for agents reviewing whether application secrets handling is actually using envelope encryption correctly instead of assuming the library setup is safe."
category:
  - "Security &amp; Verification"
framework:
  - "Codex"
source: "https://github.com/hashicorp/vault"
tool_ecosystem:
  github_repo: "hashicorp/vault"
  github_stars: 35321
---

# Vault Transit Secrets Envelope Verifier

Verifies encryption workflows with HashiCorp Vault Transit endpoints like `/encrypt`, `/decrypt`, and `/rewrap`, plus key metadata inspection. Useful for agents reviewing whether application secrets handling is actually using envelope encryption correctly instead of assuming the library setup is safe.

## Installation

Choose the setup path that fits your environment:

1. Clone or download this skill into your local skills workspace.
2. Install it with ClawHub if it is available there.
3. Copy the folder into your OpenClaw or AgentSkills directory manually.
4. Add it as a git submodule if you manage skills as pinned dependencies.
5. Vendor it directly into a project repo when you need a fixed internal copy.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vault-transit-secrets-envelope-verifier/)
