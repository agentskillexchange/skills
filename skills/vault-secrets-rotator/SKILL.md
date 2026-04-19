---
title: "Vault Secrets Rotator"
description: "The Vault Secrets Rotator skill automates credentials management by interfacing with the HashiCorp Vault HTTP API v1. It manages the complete secret lifecycle including creation, rotation, revocation, and auditing across multiple secrets engines (KV v2, database, PKI, transit). For database credentials, the skill configures Vault dynamic secrets engines via /v1/database/config and /v1/database/roles endpoints, generating short-lived credentials for PostgreSQL, MySQL, and MongoDB with automatic revocation via TTL and max-TTL policies. Credential rotation is triggered on configurable schedules or in response to security events. Kubernetes integration uses the External Secrets Operator, creating and updating ExternalSecret CRDs that sync Vault secrets into Kubernetes Secret objects. The skill manages Vault Kubernetes auth method configuration via /v1/auth/kubernetes/config, ensuring service account token validation against the cluster API server. PKI certificate management leverages the Vault PKI secrets engine to issue and rotate TLS certificates, with automatic renewal triggered at 70% of certificate lifetime. Audit logging is configured via the /v1/sys/audit endpoint with syslog and file backends for compliance requirements."
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

# Vault Secrets Rotator

The Vault Secrets Rotator skill automates credentials management by interfacing with the HashiCorp Vault HTTP API v1. It manages the complete secret lifecycle including creation, rotation, revocation, and auditing across multiple secrets engines (KV v2, database, PKI, transit). For database credentials, the skill configures Vault dynamic secrets engines via /v1/database/config and /v1/database/roles endpoints, generating short-lived credentials for PostgreSQL, MySQL, and MongoDB with automatic revocation via TTL and max-TTL policies. Credential rotation is triggered on configurable schedules or in response to security events. Kubernetes integration uses the External Secrets Operator, creating and updating ExternalSecret CRDs that sync Vault secrets into Kubernetes Secret objects. The skill manages Vault Kubernetes auth method configuration via /v1/auth/kubernetes/config, ensuring service account token validation against the cluster API server. PKI certificate management leverages the Vault PKI secrets engine to issue and rotate TLS certificates, with automatic renewal triggered at 70% of certificate lifetime. Audit logging is configured via the /v1/sys/audit endpoint with syslog and file backends for compliance requirements.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vault-secrets-rotator/)
