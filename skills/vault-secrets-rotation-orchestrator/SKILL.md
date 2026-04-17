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

The Vault Secrets Rotation Orchestrator skill manages automated secret lifecycle operations through HashiCorp Vault’s HTTP API. It orchestrates credential rotation across Vault’s dynamic secrets engines, ensuring applications always have valid credentials while maintaining security through regular rotation without service interruption.

Database secrets engine management includes automatic rotation of PostgreSQL, MySQL, MongoDB, and MSSQL credentials with configurable TTLs and max-TTLs, lease renewal tracking with proactive rotation before expiry, and zero-downtime rollover using Vault’s dual-credential rotation strategy where new credentials are provisioned before old ones are revoked.

Additional engine support covers PKI certificate rotation with automatic CSR generation and CA signing through Vault’s PKI secrets engine, AWS STS credential rotation using the AWS secrets engine for IAM user access keys and assumed role session tokens, and transit engine key rotation for encryption-as-a-service deployments. The skill monitors lease utilization across all engines, alerts on rotation failures or approaching max-TTL limits, and maintains audit logs of all rotation events mapped to Vault’s audit device output for compliance reporting.

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
