---
name: "Grounded Docs MCP Server"
slug: "grounded-docs-mcp-server"
description: "Grounded Docs MCP Server gives AI coding assistants a version-aware documentation index built from official sources like websites, GitHub, npm, PyPI, and local files. It helps agents fetch current docs, search them semantically, and reduce hallucinations when working against real libraries and APIs."
github_stars: 1224
verification: "listed"
source: "https://github.com/arabold/docs-mcp-server"
category: "Library & API Reference"
framework: "MCP"
tool_ecosystem:
  github_repo: "arabold/docs-mcp-server"
  github_stars: 1224
---

# Grounded Docs MCP Server

Grounded Docs MCP Server gives AI coding assistants a version-aware documentation index built from official sources like websites, GitHub, npm, PyPI, and local files. It helps agents fetch current docs, search them semantically, and reduce hallucinations when working against real libraries and APIs.

## Installation

Use the upstream install or setup path that matches your environment:
- npx @arabold/docs-mcp-server@latest scrape react https://react.dev/reference/react
- npx @arabold/docs-mcp-server@latest scrape my-spa https://docs.example.com/#/guide --preserve-hashes
- npx @arabold/docs-mcp-server@latest search react "useEffect cleanup" --output yaml
- npx @arabold/docs-mcp-server@latest fetch-url https://react.dev/reference/react/useEffect

Requirements and caveats from upstream:
- **1. Index documentation** (requires Node.js 22+):

Basic usage or getting-started notes:
- ## 🚀 Quick Start
- **Example: Enable OpenAI Embeddings**

- Source: https://github.com/arabold/docs-mcp-server
- Extracted from upstream docs: https://raw.githubusercontent.com/arabold/docs-mcp-server/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grounded-docs-mcp-server/)
