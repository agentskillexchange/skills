---
title: "Pulumi Infrastructure Stack Templater"
description: "Generates Pulumi infrastructure-as-code stacks in TypeScript and Python using @pulumi/aws, @pulumi/azure-native, and @pulumi/gcp SDKs. Includes Pulumi Automation API integration for programmatic stack lifecycle management."
verification: "security_reviewed"
source: "https://github.com/pulumi/pulumi"
category:
  - "Templates & Workflows"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "pulumi/pulumi"
  github_stars: 24984
---

# Pulumi Infrastructure Stack Templater

The Pulumi Infrastructure Stack Templater creates production-ready infrastructure-as-code projects using Pulumi’s multi-language SDKs. Unlike traditional IaC tools, Pulumi leverages real programming languages, and this skill generates TypeScript and Python stack definitions using @pulumi/aws, @pulumi/azure-native, and @pulumi/gcp provider packages with proper type safety and IDE autocomplete support. The Pulumi Automation API is integrated for programmatic stack lifecycle management, enabling creation, update, preview, and destruction of infrastructure stacks from within application code or CI pipelines. Generated stacks include Pulumi policy packs written with @pulumi/policy for automated compliance checking against organizational standards including cost limits, security baselines, and naming conventions. State management is configured with Pulumi Cloud backend or self-hosted S3-compatible backends with encryption and access controls. Stack references enable cross-stack resource sharing for microservices architectures where networking, compute, and application stacks are managed independently. The templater produces stack transformation functions that modify resource properties at deployment time, enabling environment-specific configurations without code duplication. Secret management integrates with AWS KMS, Azure Key Vault, or GCP KMS for encrypting sensitive configuration values within stack state.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/pulumi-infrastructure-stack-templater/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/pulumi-infrastructure-stack-templater
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/pulumi-infrastructure-stack-templater`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pulumi-infrastructure-stack-templater/)
