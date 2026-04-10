---
title: "Vault Secrets Rotation Orchestrator"
description: "Automates HashiCorp Vault secret rotation using the Vault HTTP API and dynamic secrets engines. Manages database credential leases, PKI certificate renewal, and AWS STS token rotation with zero-downtime rollover."
slug: "vault-secrets-rotation-orchestrator"
category:
  - "Security &amp; Verification"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/vault-secrets-rotation-orchestrator/"
listed: true
---

# Vault Secrets Rotation Orchestrator

Automates HashiCorp Vault secret rotation using the Vault HTTP API and dynamic secrets engines. Manages database credential leases, PKI certificate renewal, and AWS STS token rotation with zero-downtime rollover.

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
clawhub install vault-secrets-rotation-orchestrator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Vault Secrets Rotation Orchestrator skill manages automated secret lifecycle operations through HashiCorp Vault’s HTTP API. It orchestrates credential rotation across Vault’s dynamic secrets engines, ensuring applications always have valid credentials while maintaining security through regular rotation without service interruption.
Database secrets engine management includes automatic rotation of PostgreSQL, MySQL, MongoDB, and MSSQL credentials with configurable TTLs and max-TTLs, lease renewal tracking with proactive rotation before expiry, and zero-downtime rollover using Vault’s dual-credential rotation strategy where new credentials are provisioned before old ones are revoked.
Additional engine support covers PKI certificate rotation with automatic CSR generation and CA signing through Vault’s PKI secrets engine, AWS STS credential rotation using the AWS secrets engine for IAM user access keys and assumed role session tokens, and transit engine key rotation for encryption-as-a-service deployments. The skill monitors lease utilization across all engines, alerts on rotation failures or approaching max-TTL limits, and maintains audit logs of all rotation events mapped to Vault’s audit device output for compliance reporting.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vault-secrets-rotation-orchestrator/)
