---
title: "Pulumi Infrastructure Stack Templater"
description: "Generates Pulumi infrastructure-as-code stacks in TypeScript and Python using @pulumi/aws, @pulumi/azure-native, and @pulumi/gcp SDKs. Includes Pulumi Automation API integration for programmatic stack lifecycle management."
slug: "pulumi-infrastructure-stack-templater"
category:
  - "Templates &amp; Workflows"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://github.com/pulumi/pulumi"
tool_ecosystem:
  github_repo: "pulumi/pulumi"
  github_stars: 24984
---

# Pulumi Infrastructure Stack Templater

Generates Pulumi infrastructure-as-code stacks in TypeScript and Python using @pulumi/aws, @pulumi/azure-native, and @pulumi/gcp SDKs. Includes Pulumi Automation API integration for programmatic stack lifecycle management.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install pulumi-infrastructure-stack-templater
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Pulumi Infrastructure Stack Templater creates production-ready infrastructure-as-code projects using Pulumi’s multi-language SDKs. Unlike traditional IaC tools, Pulumi leverages real programming languages, and this skill generates TypeScript and Python stack definitions using @pulumi/aws, @pulumi/azure-native, and @pulumi/gcp provider packages with proper type safety and IDE autocomplete support. The Pulumi Automation API is integrated for programmatic stack lifecycle management, enabling creation, update, preview, and destruction of infrastructure stacks from within application code or CI pipelines. Generated stacks include Pulumi policy packs written with @pulumi/policy for automated compliance checking against organizational standards including cost limits, security baselines, and naming conventions. State management is configured with Pulumi Cloud backend or self-hosted S3-compatible backends with encryption and access controls. Stack references enable cross-stack resource sharing for microservices architectures where networking, compute, and application stacks are managed independently. The templater produces stack transformation functions that modify resource properties at deployment time, enabling environment-specific configurations without code duplication. Secret management integrates with AWS KMS, Azure Key Vault, or GCP KMS for encrypting sensitive configuration values within stack state.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pulumi-infrastructure-stack-templater/)
