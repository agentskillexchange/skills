---
name: Vault Secrets Rotation Orchestrator
description: Automates HashiCorp Vault secret rotation using the Vault HTTP API and
  dynamic secrets engines. Manages database credential leases, PKI certificate renewal,
  and AWS STS token rotation with zero-downtime rollover.
category: Security & Verification
framework: MCP
verification: security_reviewed
source: https://github.com/hashicorp/vault
tool_ecosystem:
  github_repo: hashicorp/vault
  github_stars: 35396
  tool: vault
  maintained: true
---
# Vault Secrets Rotation Orchestrator
Automates HashiCorp Vault secret rotation using the Vault HTTP API and dynamic secrets engines. Manages database credential leases, PKI certificate renewal, and AWS STS token rotation with zero-downtime rollover.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/vault-secrets-rotation-orchestrator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/vault-secrets-rotation-orchestrator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vault-secrets-rotation-orchestrator/)
