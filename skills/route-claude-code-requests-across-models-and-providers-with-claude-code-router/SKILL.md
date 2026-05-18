---
name: "Route Claude Code requests across models and providers with Claude Code Router"
slug: "route-claude-code-requests-across-models-and-providers-with-claude-code-router"
description: "Run Claude Code through Claude Code Router to route coding-agent requests by task, provider, or model while preserving terminal workflows and adding provider-specific transformations."
github_stars: 33863
verification: "security_reviewed"
source: "https://github.com/musistudio/claude-code-router"
author: "musistudio"
publisher_type: "open_source"
category: "Developer Tools"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "musistudio/claude-code-router"
  github_stars: 33863
  npm_package: "@musistudio/claude-code-router"
  npm_weekly_downloads: 211046
---

# Route Claude Code requests across models and providers with Claude Code Router

Run Claude Code through Claude Code Router to route coding-agent requests by task, provider, or model while preserving terminal workflows and adding provider-specific transformations.

## Prerequisites

Claude Code; Node.js/npm; one or more model provider API keys or local provider endpoints

## Installation

Use the upstream install or setup path that matches your environment:
- npm install -g @anthropic-ai/claude-code
- npm install -g @musistudio/claude-code-router

Requirements and caveats from upstream:
- **APIKEY** (optional): You can set a secret key to authenticate requests. When set, clients must provide this key in the Authorization header (e.g., Bearer your-secret-key) or the x-api-key header. Example: "APIKEY":...
- **NON_INTERACTIVE_MODE** (optional): When set to true, enables compatibility with non-interactive environments like GitHub Actions, Docker containers, or other CI/CD systems. This sets appropriate environment variable...
- The Providers array is where you define the different model providers you want to use. Each provider object requires:

Basic usage or getting-started notes:
- ## 🚀 Getting Started
- Create and configure your ~/.claude-code-router/config.json file. For more details, you can refer to config.example.json.
- **PROXY_URL** (optional): You can set a proxy for API requests, for example: "PROXY_URL": "http://127.0.0.1:7890".

- Source: https://github.com/musistudio/claude-code-router
- Extracted from upstream docs: https://raw.githubusercontent.com/musistudio/claude-code-router/HEAD/README.md

## Documentation

- https://github.com/musistudio/claude-code-router

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/route-claude-code-requests-across-models-and-providers-with-claude-code-router/)
