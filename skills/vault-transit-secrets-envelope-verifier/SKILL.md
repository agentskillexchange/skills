---
title: "Vault Transit Secrets Envelope Verifier"
description: "Verifies encryption workflows with HashiCorp Vault Transit endpoints like `/encrypt`, `/decrypt`, and `/rewrap`, plus key metadata inspection. Useful for agents reviewing whether application secrets handling is actually using envelope encryption correctly instead of assuming the library setup is safe."
slug: "vault-transit-secrets-envelope-verifier"
category:
  - "Security &amp; Verification"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://github.com/hashicorp/vault"
tool_ecosystem:
  github_repo: "hashicorp/vault"
  github_stars: 35321
---

# Vault Transit Secrets Envelope Verifier

Verifies encryption workflows with HashiCorp Vault Transit endpoints like `/encrypt`, `/decrypt`, and `/rewrap`, plus key metadata inspection. Useful for agents reviewing whether application secrets handling is actually using envelope encryption correctly instead of assuming the library setup is safe.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install vault-transit-secrets-envelope-verifier
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Vault Transit Secrets Envelope Verifier focuses on a narrow but important security problem: confirming that applications using HashiCorp Vault Transit are actually handling encryption the way the team thinks they are. It relies on Vault Transit endpoints such as /encrypt, /decrypt, and /rewrap, along with key metadata inspection, to review how ciphertext is produced, rotated, and rewrapped. That helps when teams migrate keys, audit secrets handling, or need to verify that envelope encryption is more than just a box checked in architecture docs.
The skill can compare expected key names, versions, and ciphertext formats, then flag mismatches between documented and observed behavior. It is useful in security reviews, compliance preparation, and incident follow-up where cryptographic controls must be described precisely. Because the workflow is built around real Transit operations, it also makes it easier to distinguish application misuse from Vault-side configuration issues.
Use this skill when secret-handling claims need verification, when key rotation workflows need review, or when agents should validate Transit-backed encryption with concrete API evidence.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vault-transit-secrets-envelope-verifier/)
