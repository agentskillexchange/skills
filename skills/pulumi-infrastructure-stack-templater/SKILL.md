---
name: Pulumi Infrastructure Stack Templater
description: Generates Pulumi infrastructure-as-code stacks in TypeScript and Python
  using @pulumi/aws, @pulumi/azure-native, and @pulumi/gcp SDKs. Includes Pulumi Automation
  API integration for programmatic stack lifecycle management.
verification: security_reviewed
source: https://github.com/pulumi/pulumi
category:
- Templates &amp; Workflows
framework:
- Claude Code
tool_ecosystem:
  github_repo: pulumi/pulumi
  github_stars: 24984
---
# Pulumi Infrastructure Stack Templater

The Pulumi Infrastructure Stack Templater creates production-ready infrastructure-as-code projects using Pulumi's multi-language SDKs. Unlike traditional IaC tools, Pulumi leverages real programming languages, and this skill generates TypeScript and Python stack definitions using @pulumi/aws, @pulumi/azure-native, and @pulumi/gcp provider packages with proper type safety and IDE autocomplete support. The Pulumi Automation API is integrated for programmatic stack lifecycle management, enabling creation, update, preview, and destruction of infrastructure stacks from within application code or CI pipelines. Generated stacks include Pulumi policy packs written with @pulumi/policy for automated compliance checking against organizational standards including cost limits, security baselines, and naming conventions. State management is configured with Pulumi Cloud backend or self-hosted S3-compatible backends with encryption and access controls. Stack references enable cross-stack resource sharing for microservices architectures where networking, compute, and application stacks are managed independently. The templater produces stack transformation functions that modify resource properties at deployment time, enabling environment-specific configurations without code duplication. Secret management integrates with AWS KMS, Azure Key Vault, or GCP KMS for encrypting sensitive configuration values within stack state.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pulumi-infrastructure-stack-templater/)
