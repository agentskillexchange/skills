---
name: "Block agent egress, MCP prompt injection, and secret exfiltration before agents touch the open internet with Pipelock"
slug: "block-agent-egress-mcp-prompt-injection-and-secret-exfiltration-before-agents-touch-the-open-internet-with-pipelock"
description: "Put an inline firewall and containment layer in front of agent network traffic, tool calls, and MCP traffic before you trust an agent with local secrets."
github_stars: 333
verification: "security_reviewed"
source: "https://github.com/luckyPipewrench/pipelock"
author: "luckyPipewrench"
publisher_type: "individual"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "luckyPipewrench/pipelock"
  github_stars: 333
---

# Block agent egress, MCP prompt injection, and secret exfiltration before agents touch the open internet with Pipelock

Put an inline firewall and containment layer in front of agent network traffic, tool calls, and MCP traffic before you trust an agent with local secrets.

## Prerequisites

Homebrew or Go, terminal, supported agent runtime or IDE integration

## Installation

Use the upstream install or setup path that matches your environment:
- brew install luckyPipewrench/tap/pipelock
- docker pull ghcr.io/luckypipewrench/pipelock:latest
- go install github.com/luckyPipewrench/pipelock/cmd/pipelock@latest
- docker run -p 8888:8888 -v ./pipelock.yaml:/config/pipelock.yaml:ro \

Requirements and caveats from upstream:
- pipelock check --url "https://docs.python.org/3/" # allowed
- # Docker
- # From source (requires Go 1.25+)

Basic usage or getting-started notes:
- [Quick Start](#quick-start) · [What It Does](#what-it-does) · [Docs](docs/) · [Blog](https://pipelab.org/blog/) · [Ask Dosu](https://app.dosu.dev/bcccd1cf-be85-4c0e-ae05-edeb0ff50b59/ask)
- bash
- # Set up (discovers IDE configs, generates config, verifies detection)

- Source: https://github.com/luckyPipewrench/pipelock
- Extracted from upstream docs: https://raw.githubusercontent.com/luckyPipewrench/pipelock/HEAD/README.md

## Documentation

- https://pipelab.org

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/block-agent-egress-mcp-prompt-injection-and-secret-exfiltration-before-agents-touch-the-open-internet-with-pipelock/)
