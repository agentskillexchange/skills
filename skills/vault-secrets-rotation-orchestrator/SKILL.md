---
title: "Vault Secrets Rotation Orchestrator"
description: "The Vault Secrets Rotation Orchestrator skill manages automated secret lifecycle operations through HashiCorp Vault&#8217;s HTTP API. It orchestrates credential rotation across Vault&#8217;s dynamic secrets engines, ensuring applications always have valid credentials while maintaining security through regular rotation without service interruption. Database secrets engine management includes automatic rotation of PostgreSQL, MySQL, MongoDB, and MSSQL credentials with configurable TTLs and max-TTLs, lease renewal tracking with proactive rotation before expiry, and zero-downtime rollover using Vault&#8217;s dual-credential rotation strategy where new credentials are provisioned before old ones are revoked. Additional engine support covers PKI certificate rotation with automatic CSR generation and CA signing through Vault&#8217;s PKI secrets engine, AWS STS credential rotation using the AWS secrets engine for IAM user access keys and assumed role session tokens, and transit engine key rotation for encryption-as-a-service deployments. The skill monitors lease utilization across all engines, alerts on rotation failures or approaching max-TTL limits, and maintains audit logs of all rotation events mapped to Vault&#8217;s audit device output for compliance reporting."
source: "https://github.com/hashicorp/vault"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "hashicorp/vault"
  github_stars: 35396
---

# Vault Secrets Rotation Orchestrator

The Vault Secrets Rotation Orchestrator skill manages automated secret lifecycle operations through HashiCorp Vault&#8217;s HTTP API. It orchestrates credential rotation across Vault&#8217;s dynamic secrets engines, ensuring applications always have valid credentials while maintaining security through regular rotation without service interruption. Database secrets engine management includes automatic rotation of PostgreSQL, MySQL, MongoDB, and MSSQL credentials with configurable TTLs and max-TTLs, lease renewal tracking with proactive rotation before expiry, and zero-downtime rollover using Vault&#8217;s dual-credential rotation strategy where new credentials are provisioned before old ones are revoked. Additional engine support covers PKI certificate rotation with automatic CSR generation and CA signing through Vault&#8217;s PKI secrets engine, AWS STS credential rotation using the AWS secrets engine for IAM user access keys and assumed role session tokens, and transit engine key rotation for encryption-as-a-service deployments. The skill monitors lease utilization across all engines, alerts on rotation failures or approaching max-TTL limits, and maintains audit logs of all rotation events mapped to Vault&#8217;s audit device output for compliance reporting.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vault-secrets-rotation-orchestrator/)
