---
title: "Vault Transit Secrets Envelope Verifier"
description: "Verifies encryption workflows with HashiCorp Vault Transit endpoints like `/encrypt`, `/decrypt`, and `/rewrap`, plus key metadata inspection. Useful for agents reviewing whether application secrets handling is actually using envelope encryption correctly instead of assuming the library setup is safe."
verification: "security_reviewed"
source: "https://github.com/hashicorp/vault"
category:
  - "Security & Verification"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "hashicorp/vault"
  github_stars: 35321
---

# Vault Transit Secrets Envelope Verifier

Verifies encryption workflows with HashiCorp Vault Transit endpoints like `/encrypt`, `/decrypt`, and `/rewrap`, plus key metadata inspection. Useful for agents reviewing whether application secrets handling is actually using envelope encryption correctly instead of assuming the library setup is safe.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/vault-transit-secrets-envelope-verifier/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/vault-transit-secrets-envelope-verifier
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/vault-transit-secrets-envelope-verifier`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vault-transit-secrets-envelope-verifier/)
