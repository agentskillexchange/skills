---
name: "Run DeepSeek-oriented terminal coding workflows with Reasonix"
slug: "run-deepseek-oriented-terminal-coding-workflows-with-reasonix"
description: "Use Reasonix when an operator wants a persistent terminal coding agent tuned for DeepSeek-style prefix caching, project memory, MCP-compatible plugins, and reviewable code-edit runs."
github_stars: 21828
verification: "security_reviewed"
source: "https://github.com/esengine/DeepSeek-Reasonix"
author: "esengine"
publisher_type: "open_source"
category: "Developer Tools"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "esengine/DeepSeek-Reasonix"
  github_stars: 21828
  npm_package: "reasonix"
  npm_weekly_downloads: 77947
---

# Run DeepSeek-oriented terminal coding workflows with Reasonix

Use Reasonix when an operator wants a persistent terminal coding agent tuned for DeepSeek-style prefix caching, project memory, MCP-compatible plugins, and reviewable code-edit runs.

## Prerequisites

reasonix CLI, DeepSeek or OpenAI-compatible API key, optional MCP-compatible plugins

## Installation

Use the upstream install or setup path that matches your environment:
- npm i -g reasonix # any OS; pulls the prebuilt native binary
- brew install esengine/reasonix/reasonix # macOS
- make build # -> bin/reasonix(.exe)
- make cross # -> dist/ (darwin|linux|windows × amd64|arm64)

Basic usage or getting-started notes:
- any OpenAI-compatible endpoint is a config entry, not new code. Optionally run
- **Plugin-driven.** External tools run as subprocesses over stdio JSON-RPC
- Prebuilt archives (darwin|linux|windows × amd64|arm64) and SHA256SUMS are on

- Source: https://github.com/esengine/DeepSeek-Reasonix
- Extracted from upstream docs: https://raw.githubusercontent.com/esengine/DeepSeek-Reasonix/HEAD/README.md

## Documentation

- https://github.com/esengine/DeepSeek-Reasonix/blob/main/docs/GUIDE.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-deepseek-oriented-terminal-coding-workflows-with-reasonix/)
