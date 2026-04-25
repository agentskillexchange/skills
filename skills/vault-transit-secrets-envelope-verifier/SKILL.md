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

Vault Transit Secrets Envelope Verifier focuses on a narrow but important security problem: confirming that applications using HashiCorp Vault Transit are actually handling encryption the way the team thinks they are. It relies on Vault Transit endpoints such as /encrypt, /decrypt, and /rewrap, along with key metadata inspection, to review how ciphertext is produced, rotated, and rewrapped. That helps when teams migrate keys, audit secrets handling, or need to verify that envelope encryption is more than just a box checked in architecture docs. The skill can compare expected key names, versions, and ciphertext formats, then flag mismatches between documented and observed behavior. It is useful in security reviews, compliance preparation, and incident follow-up where cryptographic controls must be described precisely. Because the workflow is built around real Transit operations, it also makes it easier to distinguish application misuse from Vault-side configuration issues. Use this skill when secret-handling claims need verification, when key rotation workflows need review, or when agents should validate Transit-backed encryption with concrete API evidence.

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
