---
name: "Build production agent harnesses with Strands Agents"
slug: "build-production-agent-harnesses-with-strands-agents"
description: "Use Strands Agents to assemble model-agnostic Python or TypeScript agent harnesses with tools, MCP, guardrails, tracing, streaming, and provider swaps."
github_stars: 6417
verification: "security_reviewed"
source: "https://github.com/strands-agents/harness-sdk"
author: "Strands Agents"
publisher_type: "organization"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "strands-agents/harness-sdk"
  github_stars: 6417
  npm_package: "@strands-agents/sdk"
  npm_weekly_downloads: 60364
---

# Build production agent harnesses with Strands Agents

Use Strands Agents to assemble model-agnostic Python or TypeScript agent harnesses with tools, MCP, guardrails, tracing, streaming, and provider swaps.

## Prerequisites

Python 3.10+ or Node.js/TypeScript, model provider credentials, optional MCP-compatible tools

## Installation

Use the upstream install or setup path that matches your environment:
- pip install strands-agents strands-agents-tools
- npm install @strands-agents/sdk
- pip install hatch
- npm ci # install from repo root

Requirements and caveats from upstream:
- <a href="https://python.org"><img alt="Python versions" src="https://img.shields.io/pypi/pyversions/strands-agents"/></a>
- This monorepo contains the Python SDK, TypeScript SDK, documentation site, and supporting packages:
- | strands-py/ | Python SDK: agent loop, model providers, tools ([PyPI](https://pypi.org/project/strands-agents/) · [releases](https://github.com/strands-agents/harness-sdk/releases?q=python%2F&expanded=false)) |

Basic usage or getting-started notes:
- **Deliver outcomes that work.** Guardrails catch mistakes before they run. Steering handlers let agents correct themselves instead of failing silently.
- Both SDKs default to the Amazon Bedrock model provider, so you'll need AWS credentials configured and model access enabled for Claude Sonnet. The [Quickstart Guide](https://strandsagents.com/docs/user-guide/quickstart...
- from strands import Agent

- Source: https://github.com/strands-agents/harness-sdk
- Extracted from upstream docs: https://raw.githubusercontent.com/strands-agents/harness-sdk/HEAD/README.md

## Documentation

- https://strandsagents.com/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-production-agent-harnesses-with-strands-agents/)
