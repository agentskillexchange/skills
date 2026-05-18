---
name: "Compose typed OpenClaw workflows with approval gates and resumable steps using Lobster"
slug: "compose-typed-openclaw-workflows-with-approval-gates-and-resumable-steps-using-lobster"
description: "Use Lobster when an OpenClaw operator wants one deterministic typed workflow step, with approval gates and resumable execution, instead of re-planning the same multi-step tool sequence in chat."
github_stars: 1128
verification: "listed"
source: "https://github.com/openclaw/lobster"
author: "OpenClaw"
publisher_type: "company"
category: "Templates & Workflows"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "openclaw/lobster"
  github_stars: 1128
---

# Compose typed OpenClaw workflows with approval gates and resumable steps using Lobster

Use Lobster when an OpenClaw operator wants one deterministic typed workflow step, with approval gates and resumable execution, instead of re-planning the same multi-step tool sequence in chat.

## Prerequisites

OpenClaw, Lobster, any local commands or data sources the workflow will call, and workflow definitions with optional approval gates.

## Installation

Requirements and caveats from upstream:
- node bin/lobster.js "workflows.run --name github.pr.monitor --args-json '{\"repo\":\"openclaw/openclaw\",\"pr\":1152}'"
- node bin/lobster.js "workflows.run --name github.pr.monitor --args-json '{\"repo\":\"openclaw/openclaw\",\"pr\":1200}'"
- node ./bin/lobster.js --help

Basic usage or getting-started notes:
- ## Example of Lobster at work
- From this folder:
- pnpm install

- Source: https://github.com/openclaw/lobster
- Extracted from upstream docs: https://raw.githubusercontent.com/openclaw/lobster/HEAD/README.md

## Documentation

- https://docs.openclaw.ai/tools/lobster

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/compose-typed-openclaw-workflows-with-approval-gates-and-resumable-steps-using-lobster/)
