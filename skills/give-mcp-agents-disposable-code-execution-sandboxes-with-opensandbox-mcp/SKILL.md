---
name: "Give MCP agents disposable code execution sandboxes with OpenSandbox MCP"
slug: "give-mcp-agents-disposable-code-execution-sandboxes-with-opensandbox-mcp"
description: "Expose sandbox creation, command execution, and file operations to MCP-capable agents so they can run untrusted code inside disposable Docker or Kubernetes-backed runtimes."
github_stars: 10207
verification: "security_reviewed"
source: "https://github.com/alibaba/OpenSandbox"
author: "Alibaba"
publisher_type: "organization"
category: "Security & Verification"
framework: "MCP"
tool_ecosystem:
  github_repo: "alibaba/OpenSandbox"
  github_stars: 10207
---

# Give MCP agents disposable code execution sandboxes with OpenSandbox MCP

Expose sandbox creation, command execution, and file operations to MCP-capable agents so they can run untrusted code inside disposable Docker or Kubernetes-backed runtimes.

## Prerequisites

Docker for local runtime or Kubernetes for cluster runtime, plus an MCP-capable client such as Claude Code or Cursor.

## Installation

Use the upstream install or setup path that matches your environment:
- pip install opensandbox
- npm install @alibaba-group/opensandbox
- pip install opensandbox-cli
- uv tool install opensandbox-cli

Requirements and caveats from upstream:
- OpenSandbox is a **general-purpose sandbox platform** for AI applications, offering multi-language SDKs, unified sandbox APIs, and Docker/Kubernetes runtimes for scenarios like Coding Agents, GUI Agents, Agent Evaluat...
- **Multi-language SDKs**: Provides sandbox SDKs in Python, Java/Kotlin, JavaScript/TypeScript, C#/.NET, Go.
- **Sandbox Runtime**: Built-in lifecycle management supporting Docker and [high-performance Kubernetes runtime](./kubernetes), enabling both local runs and large-scale distributed scheduling.

Basic usage or getting-started notes:
- OpenSandbox also provides osb, a terminal CLI for the common sandbox workflow: create sandboxes, run commands, move files, inspect diagnostics, and manage runtime egress policy.
- bash
- # or

- Source: https://github.com/alibaba/OpenSandbox
- Extracted from upstream docs: https://raw.githubusercontent.com/alibaba/OpenSandbox/HEAD/README.md

## Documentation

- https://open-sandbox.ai

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/give-mcp-agents-disposable-code-execution-sandboxes-with-opensandbox-mcp/)
