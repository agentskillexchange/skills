---
name: "Vault Secrets Rotator"
description: "Manages secret lifecycle through the HashiCorp Vault HTTP API v1. Rotates database credentials via Vault dynamic secrets engine and syncs to Kubernetes via External Secrets Operator CRDs."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/vault-secrets-rotator/"
category:
  - "Security &amp; Verification"
framework:
  - "MCP"
---

# Vault Secrets Rotator

The Vault Secrets Rotator skill automates credentials management by interfacing with the HashiCorp Vault HTTP API v1. It manages the complete secret lifecycle including creation, rotation, revocation, and auditing across multiple secrets engines (KV v2, database, PKI, transit).
For database credentials, the skill configures Vault dynamic secrets engines via /v1/database/config and /v1/database/roles endpoints, generating short-lived credentials for PostgreSQL, MySQL, and MongoDB with automatic revocation via TTL and max-TTL policies. Credential rotation is triggered on configurable schedules or in response to security events.
Kubernetes integration uses the External Secrets Operator, creating and updating ExternalSecret CRDs that sync Vault secrets into Kubernetes Secret objects. The skill manages Vault Kubernetes auth method configuration via /v1/auth/kubernetes/config, ensuring service account token validation against the cluster API server. PKI certificate management leverages the Vault PKI secrets engine to issue and rotate TLS certificates, with automatic renewal triggered at 70% of certificate lifetime. Audit logging is configured via the /v1/sys/audit endpoint with syslog and file backends for compliance requirements.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vault-secrets-rotator/)
