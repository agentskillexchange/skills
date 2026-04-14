---
title: "Pulumi Infrastructure Stack Templater"
description: "Generates Pulumi infrastructure-as-code stacks in TypeScript and Python using @pulumi/aws, @pulumi/azure-native, and @pulumi/gcp SDKs. Includes Pulumi Automation API integration for programmatic stack lifecycle management."
verification: security_reviewed
source: "https://github.com/pulumi/pulumi"
category:
  - "Templates &amp; Workflows"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "pulumi/pulumi"
  github_stars: 24984
---

# Pulumi Infrastructure Stack Templater

The Pulumi Infrastructure Stack Templater creates production-ready infrastructure-as-code projects using Pulumi’s multi-language SDKs. Unlike traditional IaC tools, Pulumi leverages real programming languages, and this skill generates TypeScript and Python stack definitions using @pulumi/aws, @pulumi/azure-native, and @pulumi/gcp provider packages with proper type safety and IDE autocomplete support. The Pulumi Automation API is integrated for programmatic stack lifecycle management, enabling creation, update, preview, and destruction of infrastructure stacks from within application code or CI pipelines. Generated stacks include Pulumi policy packs written with @pulumi/policy for automated compliance checking against organizational standards including cost limits, security baselines, and naming conventions. State management is configured with Pulumi Cloud backend or self-hosted S3-compatible backends with encryption and access controls. Stack references enable cross-stack resource sharing for microservices architectures where networking, compute, and application stacks are managed independently. The templater produces stack transformation functions that modify resource properties at deployment time, enabling environment-specific configurations without code duplication. Secret management integrates with AWS KMS, Azure Key Vault, or GCP KMS for encrypting sensitive configuration values within stack state.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pulumi-infrastructure-stack-templater/)
