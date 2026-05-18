---
name: "Provision OAuth-capable Microsoft agent identities with Entra Agent ID"
slug: "provision-oauth-capable-microsoft-agent-identities-with-entra-agent-id"
description: "Create Microsoft Entra Agent Identity blueprints, principals, and agent identities with the right beta Graph permissions, sponsor rules, and sidecar-based auth patterns."
verification: "listed"
source: "https://github.com/microsoft/skills/tree/main/.github/skills/entra-agent-id"
author: "Microsoft"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
---

# Provision OAuth-capable Microsoft agent identities with Entra Agent ID

Create Microsoft Entra Agent Identity blueprints, principals, and agent identities with the right beta Graph permissions, sponsor rules, and sidecar-based auth patterns.

## Prerequisites

Microsoft Graph beta API, Microsoft Entra roles and app registration or PowerShell Graph modules, optional Entra Agent ID sidecar

## Installation

Use the upstream install or setup path that matches your environment:
- npx skills add microsoft/skills
- git clone https://github.com/microsoft/skills.git
- pnpm install
- pnpm harness --list

Requirements and caveats from upstream:
- | [Python](#python) | 39 | -py |
- ├── plugins/ # Language-based plugin bundles (azure-sdk-python, etc.)
- ├── python/ # -> ../.github/skills/*-py

Basic usage or getting-started notes:
- bash
- Select the skills you need from the wizard. Skills are installed to your chosen agent's directory (e.g., .github/skills/ for GitHub Copilot) and symlinked if you use multiple agents.
- <details>

- Source: https://github.com/microsoft/skills/tree/main/.github/skills/entra-agent-id
- Extracted from upstream docs: https://raw.githubusercontent.com/microsoft/skills/HEAD/README.md

## Documentation

- https://microsoft.github.io/skills/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/provision-oauth-capable-microsoft-agent-identities-with-entra-agent-id/)
