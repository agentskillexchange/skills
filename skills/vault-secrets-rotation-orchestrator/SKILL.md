---
title: "Vault Secrets Rotation Orchestrator"
description: "Automates HashiCorp Vault secret rotation using the Vault HTTP API and dynamic secrets engines. Manages database credential leases, PKI certificate renewal, and AWS STS token rotation with zero-downtime rollover."
verification: security_reviewed
source: "https://github.com/hashicorp/vault"
category:
  - "Security & Verification"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "hashicorp/vault"
  github_stars: 35396
---

# Vault Secrets Rotation Orchestrator

Automates HashiCorp Vault secret rotation using the Vault HTTP API and dynamic secrets engines. Manages database credential leases, PKI certificate renewal, and AWS STS token rotation with zero-downtime rollover.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/vault-secrets-rotation-orchestrator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/vault-secrets-rotation-orchestrator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/vault-secrets-rotation-orchestrator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vault-secrets-rotation-orchestrator/)
