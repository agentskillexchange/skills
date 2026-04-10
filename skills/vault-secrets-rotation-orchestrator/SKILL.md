---
name: "Vault Secrets Rotation Orchestrator"
description: "Automates HashiCorp Vault secret rotation using the Vault HTTP API and dynamic secrets engines. Manages database credential leases, PKI certificate renewal, and AWS STS token rotation with zero-downtime rollover."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/vault-secrets-rotation-orchestrator/"
category:
  - "Security &amp; Verification"
framework:
  - "MCP"
---

# Vault Secrets Rotation Orchestrator

The Vault Secrets Rotation Orchestrator skill manages automated secret lifecycle operations through HashiCorp Vault's HTTP API. It orchestrates credential rotation across Vault's dynamic secrets engines, ensuring applications always have valid credentials while maintaining security through regular rotation without service interruption.
Database secrets engine management includes automatic rotation of PostgreSQL, MySQL, MongoDB, and MSSQL credentials with configurable TTLs and max-TTLs, lease renewal tracking with proactive rotation before expiry, and zero-downtime rollover using Vault's dual-credential rotation strategy where new credentials are provisioned before old ones are revoked.
Additional engine support covers PKI certificate rotation with automatic CSR generation and CA signing through Vault's PKI secrets engine, AWS STS credential rotation using the AWS secrets engine for IAM user access keys and assumed role session tokens, and transit engine key rotation for encryption-as-a-service deployments. The skill monitors lease utilization across all engines, alerts on rotation failures or approaching max-TTL limits, and maintains audit logs of all rotation events mapped to Vault's audit device output for compliance reporting.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vault-secrets-rotation-orchestrator/)
