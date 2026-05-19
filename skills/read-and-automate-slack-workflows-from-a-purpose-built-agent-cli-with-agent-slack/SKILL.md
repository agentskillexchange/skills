---
name: "Read and automate Slack workflows from a purpose-built agent CLI with agent-slack"
slug: "read-and-automate-slack-workflows-from-a-purpose-built-agent-cli-with-agent-slack"
description: "Search channels, inspect threads, move files, and send or edit Slack messages through an agent-oriented CLI with structured output."
github_stars: 382
verification: "security_reviewed"
source: "https://github.com/stablyai/agent-slack"
author: "stablyai"
publisher_type: "organization"
category: "Calendar, Email & Productivity"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "stablyai/agent-slack"
  github_stars: 382
  npm_package: "agent-slack"
  npm_weekly_downloads: 5210
---

# Read and automate Slack workflows from a purpose-built agent CLI with agent-slack

Search channels, inspect threads, move files, and send or edit Slack messages through an agent-oriented CLI with structured output.

## Prerequisites

agent-slack CLI, Node.js or Bun, Slack workspace access, and either supported local auth extraction or valid Slack credentials/tokens

## Installation

Use the upstream install or setup path that matches your environment:
- npm i -g agent-slack
- npx skills add stablyai/agent-slack

Requirements and caveats from upstream:
- **Zero-config auth** — Auth just works if you have Slack Desktop (with fallbacks available). No Python dependency.
- OR npm global install (requires Node >= 22.5):
- Channel mode requires --ts:

Basic usage or getting-started notes:
- bash
- OR run via Nix flake:
- nix run github:stablyai/agent-slack

- Source: https://github.com/stablyai/agent-slack
- Extracted from upstream docs: https://raw.githubusercontent.com/stablyai/agent-slack/HEAD/README.md

## Documentation

- https://github.com/stablyai/agent-slack/tree/main/docs

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/read-and-automate-slack-workflows-from-a-purpose-built-agent-cli-with-agent-slack/)
