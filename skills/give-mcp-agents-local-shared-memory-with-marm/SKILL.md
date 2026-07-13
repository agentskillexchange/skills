---
name: "Give MCP agents local shared memory with MARM"
slug: "give-mcp-agents-local-shared-memory-with-marm"
description: "Use MARM Memory to give Claude Code, Cursor, Codex, Gemini, and other MCP clients a local-first shared memory server with sessions, semantic recall, notebooks, summaries, and code graph context."
github_stars: 307
verification: "security_reviewed"
source: "https://github.com/Lyellr88/marm-memory"
author: "MARM Memory contributors"
publisher_type: "open_source"
category: "Integrations & Connectors"
framework: "MCP"
tool_ecosystem:
  github_repo: "Lyellr88/marm-memory"
  github_stars: 307
---

# Give MCP agents local shared memory with MARM

Use MARM Memory to give Claude Code, Cursor, Codex, Gemini, and other MCP clients a local-first shared memory server with sessions, semantic recall, notebooks, summaries, and code graph context.

## Prerequisites

MARM MCP server, Python or Docker runtime, SQLite-backed local storage, MCP-compatible clients such as Claude Code, Cursor, Codex, Gemini, Qwen, or VS Code agents

## Installation

Use the upstream install or setup path that matches your environment:
- npx degit Lyellr88/marm-memory/skills
- pip install marm-mcp-server
- Docker uses the same unified image and key:
- docker run -d --name marm-mcp-server \

Requirements and caveats from upstream:
- [![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
- [![Docker Pulls](https://img.shields.io/docker/pulls/lyellr88/marm-mcp-server)](https://hub.docker.com/r/lyellr88/marm-mcp-server)
- | **Deployment layer** | Pip, Docker, STDIO, HTTP, --swarm, --swarm-max, and --trusted | Lets you run private local memory or shared multi-agent memory with the same MCP surface |

Basic usage or getting-started notes:
- [Quick Start](#-quick-start-for-mcp-http--stdio)
- "server_url": "https://your-marm-domain.example.com/mcp",
- MARM handles lifecycle work internally. Docs and session state initialize on the first real tool call, and packaged docs are indexed into the marm_system memory namespace with source-file hash tracking, so your agent...

- Source: https://github.com/Lyellr88/marm-memory
- Extracted from upstream docs: https://raw.githubusercontent.com/Lyellr88/marm-memory/HEAD/README.md

## Documentation

- https://github.com/Lyellr88/marm-memory

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/give-mcp-agents-local-shared-memory-with-marm/)
