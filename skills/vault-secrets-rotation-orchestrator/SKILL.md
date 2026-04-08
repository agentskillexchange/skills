---
title: Vault Secrets Rotation Orchestrator
description: The Vault Secrets Rotation Orchestrator skill manages automated secret
  lifecycle operations through HashiCorp Vault’s HTTP API. It orchestrates credential
  rotation across Vault’s dynamic secrets engines, ensuring applications always have
  valid credentials while maintaining security through regular rotation without service
  interruption. Database secrets engine management includes automatic rotation of
  PostgreSQL, MySQL, MongoDB, and MSSQL credentials with configurable TTLs and max-TTLs,
  lease renewal tracking with proactive rotation before expiry, and zero-downtime
  rollover using Vault’s dual-credential rotation strategy where new credentials are
  provisioned before old ones are revoked. Additional engine support covers PKI certificate
  rotation with automatic CSR generation and CA signing through Vault’s PKI secrets
  engine, AWS STS credential rotation using the AWS secrets engine for IAM user access
  keys and assumed role session tokens, and transit engine key rotation for encryption-as-a-service
  deployments. The skill monitors lease utilization across all engines, alerts on
  rotation failures or approaching max-TTL limits, and maintains audit logs of all
  rotation events mapped to Vault’s audit device output for compliance reporting.
verification: security_reviewed
source: https://agentskillexchange.com/skills/vault-secrets-rotation-orchestrator/
category:
- Security &amp; Verification
framework:
- MCP
---

# Vault Secrets Rotation Orchestrator

The Vault Secrets Rotation Orchestrator skill manages automated secret lifecycle operations through HashiCorp Vault’s HTTP API. It orchestrates credential rotation across Vault’s dynamic secrets engines, ensuring applications always have valid credentials while maintaining security through regular rotation without service interruption. Database secrets engine management includes automatic rotation of PostgreSQL, MySQL, MongoDB, and MSSQL credentials with configurable TTLs and max-TTLs, lease renewal tracking with proactive rotation before expiry, and zero-downtime rollover using Vault’s dual-credential rotation strategy where new credentials are provisioned before old ones are revoked. Additional engine support covers PKI certificate rotation with automatic CSR generation and CA signing through Vault’s PKI secrets engine, AWS STS credential rotation using the AWS secrets engine for IAM user access keys and assumed role session tokens, and transit engine key rotation for encryption-as-a-service deployments. The skill monitors lease utilization across all engines, alerts on rotation failures or approaching max-TTL limits, and maintains audit logs of all rotation events mapped to Vault’s audit device output for compliance reporting.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vault-secrets-rotation-orchestrator/)
