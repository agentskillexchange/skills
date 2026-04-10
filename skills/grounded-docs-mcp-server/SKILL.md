---
title: "Grounded Docs MCP Server"
description: "Grounded Docs MCP Server gives AI coding assistants a version-aware documentation index built from official sources like websites, GitHub, npm, PyPI, and local files. It helps agents fetch current docs, search them semantically, and reduce hallucinations when working against real libraries and APIs."
slug: "grounded-docs-mcp-server"
category:
  - "Library &amp; API Reference"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://github.com/arabold/docs-mcp-server"
tool_ecosystem:
  github_repo: "arabold/docs-mcp-server"
  github_stars: 1209
---

# Grounded Docs MCP Server

Grounded Docs MCP Server gives AI coding assistants a version-aware documentation index built from official sources like websites, GitHub, npm, PyPI, and local files. It helps agents fetch current docs, search them semantically, and reduce hallucinations when working against real libraries and APIs.

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
clawhub install grounded-docs-mcp-server
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Grounded Docs MCP Server is an open-source documentation retrieval system for AI coding assistants and other MCP-compatible tools. The project is published as @arabold/docs-mcp-server and positions itself as an alternative to hosted documentation tools like Context7 and Ref.Tools. Its practical job-to-be-done is simple: give an agent reliable, version-specific documentation instead of making it guess from stale model memory or generic web search.
The server can ingest documentation from official websites, GitHub repositories, npm packages, PyPI packages, local folders, and archive files. According to the upstream README, it supports a wide range of formats including HTML, Markdown, PDF, Office documents, notebooks, source code, structured data files, and configuration files. That makes it useful for teams that need one knowledge layer across SDK docs, internal docs, and code-adjacent reference material.
Grounded Docs supports both CLI-first and long-running MCP usage. You can scrape a library, query the local index, fetch a single page as Markdown, or run the service as an MCP endpoint and connect it to clients such as Claude, Cline, Copilot, or Gemini CLI. The README also documents a local web UI and optional embedding-model configuration for better semantic search. In practice, this skill is a good fit for developers who want grounded library and API answers, repeatable doc indexing, and safer coding workflows built on current upstream documentation rather than hallucinated references.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grounded-docs-mcp-server/)
