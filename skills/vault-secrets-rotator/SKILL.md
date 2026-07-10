---
name: "Vault Secrets Rotator"
slug: "vault-secrets-rotator"
description: "Manages secret lifecycle through the HashiCorp Vault HTTP API v1. Rotates database credentials via Vault dynamic secrets engine and syncs to Kubernetes via External Secrets Operator CRDs."
github_stars: 35396
verification: "security_reviewed"
source: "https://github.com/hashicorp/vault"
category: "Security & Verification"
framework: "MCP"
tool_ecosystem:
  github_repo: "hashicorp/vault"
  github_stars: 35396
---

# Vault Secrets Rotator

Manages secret lifecycle through the HashiCorp Vault HTTP API v1. Rotates database credentials via Vault dynamic secrets engine and syncs to Kubernetes via External Secrets Operator CRDs.

## Installation

Use the upstream install or setup path that matches your environment:
- $ make bootstrap
- To compile a development version of Vault, run make or make dev. This will
- $ make dev
- To compile a development version of Vault with the UI, run make static-dist dev-ui. This will

Requirements and caveats from upstream:
- A modern system requires access to a multitude of secrets: database credentials, API keys for external services, credentials for service-oriented architecture communication, etc. Understanding who is accessing what se...
- To run tests, type make test. Note: this requires Docker to be installed. If

Basic usage or getting-started notes:
- systems, such as AWS or SQL databases. For example, when an application
- can revoke not only single secrets, but a tree of secrets, for example,
- Documentation, Getting Started, and Certification Exams

- Source: https://github.com/hashicorp/vault
- Extracted from upstream docs: https://raw.githubusercontent.com/hashicorp/vault/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vault-secrets-rotator/)
