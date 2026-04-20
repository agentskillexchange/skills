---
title: "Vault Secrets Rotator"
description: "Manages secret lifecycle through the HashiCorp Vault HTTP API v1. Rotates database credentials via Vault dynamic secrets engine and syncs to Kubernetes via External Secrets Operator CRDs."
verification: security_reviewed
source: "https://github.com/hashicorp/vault"
category:
  - "Security &amp; Verification"
framework:
  - "MCP"
---

# Vault Secrets Rotator

Manages secret lifecycle through the HashiCorp Vault HTTP API v1. Rotates database credentials via Vault dynamic secrets engine and syncs to Kubernetes via External Secrets Operator CRDs.

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
