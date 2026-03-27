---
name: "Vault Transit Secrets Envelope Verifier"
description: "Verifies encryption workflows with HashiCorp Vault Transit endpoints like `/encrypt`, `/decrypt`, and `/rewrap`, plus key metadata inspection. Useful for agents reviewing whether application secrets handling is actually using envelope encryption correctly instead of assuming the library setup is safe."
category: "Security & Verification"
framework: "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/vault-transit-secrets-envelope-verifier/"
tool_ecosystem:
  tool: vault
  github_stars: 35275
  github_repo: hashicorp/vault
  maintained: true
---

# Vault Transit Secrets Envelope Verifier

Verifies encryption workflows with HashiCorp Vault Transit endpoints like `/encrypt`, `/decrypt`, and `/rewrap`, plus key metadata inspection. Useful for agents reviewing whether application secrets handling is actually using envelope encryption correctly instead of assuming the library setup is safe.

## Overview

Vault Transit Secrets Envelope Verifier focuses on a narrow but important security problem: confirming that applications using HashiCorp Vault Transit are actually handling encryption the way the team thinks they are. It relies on Vault Transit endpoints such as `/encrypt`, `/decrypt`, and `/rewrap`, along with key metadata inspection, to review how ciphertext is produced, rotated, and rewrapped. That helps when teams migrate keys, audit secrets handling, or need to verify that envelope encryption is more than just a box checked in architecture docs.

The skill can compare expected key names, versions, and ciphertext formats, then flag mismatches between documented and observed behavior. It is useful in security reviews, compliance preparation, and incident follow-up where cryptographic controls must be described precisely. Because the workflow is built around real Transit operations, it also makes it easier to distinguish application misuse from Vault-side configuration issues.

Use this skill when secret-handling claims need verification, when key rotation workflows need review, or when agents should validate Transit-backed encryption with concrete API evidence.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill vault-transit-secrets-envelope-verifier
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill vault-transit-secrets-envelope-verifier -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill vault-transit-secrets-envelope-verifier -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill vault-transit-secrets-envelope-verifier -a codex
```

### OpenClaw

```bash
clawhub install vault-transit-secrets-envelope-verifier
```

## Source

- Marketplace: https://agentskillexchange.com/skills/vault-transit-secrets-envelope-verifier/
