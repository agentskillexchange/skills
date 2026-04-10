---
title: "Context7 MCP Documentation Server for LLM Code Editors"
description: "Context7 by Upstash injects up-to-date, version-specific library documentation and code examples directly into AI prompts. Eliminates hallucinated APIs and outdated code generation by pulling documentation straight from the source at query time."
slug: "context7-mcp-documentation-server-llm-code-editors"
category:
  - "Library &amp; API Reference"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://github.com/upstash/context7"
tool_ecosystem:
  github_repo: "upstash/context7"
  github_stars: 51326
---

# Context7 MCP Documentation Server for LLM Code Editors

Context7 by Upstash injects up-to-date, version-specific library documentation and code examples directly into AI prompts. Eliminates hallucinated APIs and outdated code generation by pulling documentation straight from the source at query time.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install context7-mcp-documentation-server-llm-code-editors
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Context7 is an MCP server and CLI tool developed by Upstash that solves one of the most persistent problems in AI-assisted coding: outdated and hallucinated API references. With over 13,900 GitHub stars and an npm package (@upstash/context7-mcp) actively maintained with recent releases, it has become the most-starred documentation-focused MCP server available.
The core mechanism works by intercepting documentation-related queries from AI coding agents and fetching the actual, current documentation from upstream library sources. When a developer asks their AI assistant to implement something using Next.js middleware or configure a Cloudflare Worker, Context7 retrieves the relevant docs for the specific version in use and injects them directly into the prompt context. This prevents the AI from generating code based on stale training data or inventing APIs that don’t exist.
Context7 operates in two modes. The CLI + Skills mode installs a skill file that guides coding agents to fetch docs using ctx7 CLI commands, requiring no MCP infrastructure. The MCP mode registers a Context7 MCP server so agents can call documentation tools natively through the Model Context Protocol. Setup is a single command: npx ctx7 setup, which handles OAuth authentication, API key generation, and skill installation automatically.
The server exposes three primary tools: resolve-library-id for matching library names to Context7-compatible identifiers, query-docs for retrieving documentation by library ID, and a search tool for finding libraries in the Context7 index. It supports version-specific queries and works with Cursor, Claude Code, VS Code with Copilot, and other MCP-compatible clients. Released under the Apache-2.0 license, it’s available via npm and directly from the GitHub repository at upstash/context7.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/context7-mcp-documentation-server-llm-code-editors/)
