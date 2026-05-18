---
name: "Manage ElevenLabs agents as versioned local config files instead of hand-editing them in the dashboard with ElevenLabs CLI"
slug: "manage-elevenlabs-agents-as-versioned-local-config-files-instead-of-hand-editing-them-in-the-dashboard-with-elevenlabs-cli"
description: "Initialize, authenticate, and edit ElevenLabs agent configs from local files when you want agent definitions in code review instead of only in a hosted UI."
github_stars: 49
verification: "security_reviewed"
source: "https://github.com/elevenlabs/cli"
author: "ElevenLabs"
publisher_type: "vendor"
category: "Integrations & Connectors"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "elevenlabs/cli"
  github_stars: 49
  npm_package: "@elevenlabs/cli"
  npm_weekly_downloads: 10433
---

# Manage ElevenLabs agents as versioned local config files instead of hand-editing them in the dashboard with ElevenLabs CLI

Initialize, authenticate, and edit ElevenLabs agent configs from local files when you want agent definitions in code review instead of only in a hosted UI.

## Prerequisites

Node.js, elevenlabs CLI, ElevenLabs API key

## Installation

Use the upstream install or setup path that matches your environment:
- pnpm install -g @elevenlabs/cli
- npm install -g @elevenlabs/cli
- pnpm dlx @elevenlabs/cli agents init
- npx @elevenlabs/cli agents init

Requirements and caveats from upstream:
- **Note**: For now, your API key must be unrestricted to work with the CLI, as ElevenLabs-restricted keys are not available yet.
- **CRITICAL**: E2E tests require a **dedicated, empty test account**.

Basic usage or getting-started notes:
- bash
- # Global installation
- # OR

- Source: https://github.com/elevenlabs/cli
- Extracted from upstream docs: https://raw.githubusercontent.com/elevenlabs/cli/HEAD/README.md

## Documentation

- https://github.com/elevenlabs/cli

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/manage-elevenlabs-agents-as-versioned-local-config-files-instead-of-hand-editing-them-in-the-dashboard-with-elevenlabs-cli/)
