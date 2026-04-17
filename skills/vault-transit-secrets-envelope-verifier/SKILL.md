---
name: Vault Transit Secrets Envelope Verifier
description: Verifies encryption workflows with HashiCorp Vault Transit endpoints
  like `/encrypt`, `/decrypt`, and `/rewrap`, plus key metadata inspection. Useful
  for agents reviewing whether application secrets handling is actually using envelope
  encryption correctly instead of assuming the library setup is safe.
category: Security & Verification
framework: Codex
verification: security_reviewed
source: https://github.com/hashicorp/vault
tool_ecosystem:
  github_repo: hashicorp/vault
  github_stars: 35321
  tool: vault
---
# Vault Transit Secrets Envelope Verifier
Verifies encryption workflows with HashiCorp Vault Transit endpoints like `/encrypt`, `/decrypt`, and `/rewrap`, plus key metadata inspection. Useful for agents reviewing whether application secrets handling is actually using envelope encryption correctly instead of assuming the library setup is safe.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/vault-transit-secrets-envelope-verifier
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/vault-transit-secrets-envelope-verifier` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vault-transit-secrets-envelope-verifier/)
