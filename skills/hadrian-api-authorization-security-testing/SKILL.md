---
name: "Test API authorization flows with Hadrian"
slug: "hadrian-api-authorization-security-testing"
description: "Lets an agent exercise REST, GraphQL, and gRPC authorization paths with YAML-defined role tests so BOLA, BFLA, broken authentication, and related API flaws are caught before release."
github_stars: 38
verification: "security_reviewed"
source: "https://github.com/praetorian-inc/hadrian"
author: "Praetorian"
publisher_type: "company"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "praetorian-inc/hadrian"
  github_stars: 38
---

# Test API authorization flows with Hadrian

Lets an agent exercise REST, GraphQL, and gRPC authorization paths with YAML-defined role tests so BOLA, BFLA, broken authentication, and related API flaws are caught before release.

## Prerequisites

Go or a prebuilt Hadrian binary, plus a target API definition or endpoint and role/auth configuration files such as roles.yaml and auth.yaml.

## Installation

Use the upstream install or setup path that matches your environment:
- go install github.com/praetorian-inc/hadrian/cmd/hadrian@latest
- git clone https://github.com/praetorian-inc/hadrian.git
- make build
- make build # Build the binary

Requirements and caveats from upstream:
- # AI-powered triage with OpenAI (requires OPENAI_API_KEY)
- # AI-powered triage with Anthropic (requires ANTHROPIC_API_KEY)
- # AI-assisted attack planning (requires OPENAI_API_KEY, or use --planner-provider for Anthropic/Ollama)

Basic usage or getting-started notes:
- bash
- ### Download Pre-Built Binary
- Download the latest binary for your platform from the [Releases](https://github.com/praetorian-inc/hadrian/releases) page.

- Source: https://github.com/praetorian-inc/hadrian
- Extracted from upstream docs: https://raw.githubusercontent.com/praetorian-inc/hadrian/HEAD/README.md

## Documentation

- https://github.com/praetorian-inc/hadrian#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hadrian-api-authorization-security-testing/)
