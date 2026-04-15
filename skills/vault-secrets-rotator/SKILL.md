---
title: "Vault Secrets Rotator"
description: "Manages secret lifecycle through the HashiCorp Vault HTTP API v1. Rotates database credentials via Vault dynamic secrets engine and syncs to Kubernetes via External Secrets Operator CRDs."
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

# Vault Secrets Rotator

The Vault Secrets Rotator skill automates credentials management by interfacing with the HashiCorp Vault HTTP API v1. It manages the complete secret lifecycle including creation, rotation, revocation, and auditing across multiple secrets engines (KV v2, database, PKI, transit).

For database credentials, the skill configures Vault dynamic secrets engines via /v1/database/config and /v1/database/roles endpoints, generating short-lived credentials for PostgreSQL, MySQL, and MongoDB with automatic revocation via TTL and max-TTL policies. Credential rotation is triggered on configurable schedules or in response to security events.

Kubernetes integration uses the External Secrets Operator, creating and updating ExternalSecret CRDs that sync Vault secrets into Kubernetes Secret objects. The skill manages Vault Kubernetes auth method configuration via /v1/auth/kubernetes/config, ensuring service account token validation against the cluster API server. PKI certificate management leverages the Vault PKI secrets engine to issue and rotate TLS certificates, with automatic renewal triggered at 70% of certificate lifetime. Audit logging is configured via the /v1/sys/audit endpoint with syslog and file backends for compliance requirements.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/vault-secrets-rotator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/vault-secrets-rotator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vault-secrets-rotator/)
