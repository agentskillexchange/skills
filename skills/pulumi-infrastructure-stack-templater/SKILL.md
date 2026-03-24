---
name: "Pulumi Infrastructure Stack Templater"
description: "Generates Pulumi infrastructure-as-code stacks in TypeScript and Python using @pulumi/aws, @pulumi/azure-native, and @pulumi/gcp SDKs. Includes Pulumi Automation API integration for programmatic stack lifecycle management."
category: "Templates & Workflows"
framework: "Claude Code"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/pulumi-infrastructure-stack-templater/"
---

# Pulumi Infrastructure Stack Templater

Generates Pulumi infrastructure-as-code stacks in TypeScript and Python using @pulumi/aws, @pulumi/azure-native, and @pulumi/gcp SDKs. Includes Pulumi Automation API integration for programmatic stack lifecycle management.

## Overview

The Pulumi Infrastructure Stack Templater creates production-ready infrastructure-as-code projects using Pulumi’s multi-language SDKs. Unlike traditional IaC tools, Pulumi leverages real programming languages, and this skill generates TypeScript and Python stack definitions using @pulumi/aws, @pulumi/azure-native, and @pulumi/gcp provider packages with proper type safety and IDE autocomplete support. The Pulumi Automation API is integrated for programmatic stack lifecycle management, enabling creation, update, preview, and destruction of infrastructure stacks from within application code or CI pipelines. Generated stacks include Pulumi policy packs written with @pulumi/policy for automated compliance checking against organizational standards including cost limits, security baselines, and naming conventions. State management is configured with Pulumi Cloud backend or self-hosted S3-compatible backends with encryption and access controls. Stack references enable cross-stack resource sharing for microservices architectures where networking, compute, and application stacks are managed independently. The templater produces stack transformation functions that modify resource properties at deployment time, enabling environment-specific configurations without code duplication. Secret management integrates with AWS KMS, Azure Key Vault, or GCP KMS for encrypting sensitive configuration values within stack state.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pulumi-infrastructure-stack-templater
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pulumi-infrastructure-stack-templater -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pulumi-infrastructure-stack-templater -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pulumi-infrastructure-stack-templater -a codex
```

### OpenClaw

```bash
clawhub install pulumi-infrastructure-stack-templater
```

## Source

- Marketplace: https://agentskillexchange.com/skills/pulumi-infrastructure-stack-templater/
