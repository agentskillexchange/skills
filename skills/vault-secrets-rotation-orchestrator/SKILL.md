---
name: "Vault Secrets Rotation Orchestrator"
description: "Automates HashiCorp Vault secret rotation using the Vault HTTP API and dynamic secrets engines. Manages database credential leases, PKI certificate renewal, and AWS STS token rotation with zero-downtime rollover."
category: "Security &amp; Verification"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/vault-secrets-rotation-orchestrator/"
---
# Vault Secrets Rotation Orchestrator

Automates HashiCorp Vault secret rotation using the Vault HTTP API and dynamic secrets engines. Manages database credential leases, PKI certificate renewal, and AWS STS token rotation with zero-downtime rollover.

The Vault Secrets Rotation Orchestrator skill manages automated secret lifecycle operations through HashiCorp Vault’s HTTP API. It orchestrates credential rotation across Vault’s dynamic secrets engines, ensuring applications always have valid credentials while maintaining security through regular rotation without service interruption.

Database secrets engine management includes automatic rotation of PostgreSQL, MySQL, MongoDB, and MSSQL credentials with configurable TTLs and max-TTLs, lease renewal tracking with proactive rotation before expiry, and zero-downtime rollover using Vault’s dual-credential rotation strategy where new credentials are provisioned before old ones are revoked.

Additional engine support covers PKI certificate rotation with automatic CSR generation and CA signing through Vault’s PKI secrets engine, AWS STS credential rotation using the AWS secrets engine for IAM user access keys and assumed role session tokens, and transit engine key rotation for encryption-as-a-service deployments. The skill monitors lease utilization across all engines, alerts on rotation failures or approaching max-TTL limits, and maintains audit logs of all rotation events mapped to Vault’s audit device output for compliance reporting.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill vault-secrets-rotation-orchestrator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill vault-secrets-rotation-orchestrator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill vault-secrets-rotation-orchestrator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill vault-secrets-rotation-orchestrator -a codex
```

### OpenClaw

```bash
clawhub install vault-secrets-rotation-orchestrator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vault-secrets-rotation-orchestrator/)
