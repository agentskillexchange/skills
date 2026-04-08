---
title: Grounded Docs MCP Server
description: 'Grounded Docs MCP Server is an open-source documentation retrieval system
  for AI coding assistants and other MCP-compatible tools. The project is published
  as @arabold/docs-mcp-server and positions itself as an alternative to hosted documentation
  tools like Context7 and Ref.Tools. Its practical job-to-be-done is simple: give
  an agent reliable, version-specific documentation instead of making it guess from
  stale model memory or generic web search. The server can ingest documentation from
  official websites, GitHub repositories, npm packages, PyPI packages, local folders,
  and archive files. According to the upstream README, it supports a wide range of
  formats including HTML, Markdown, PDF, Office documents, notebooks, source code,
  structured data files, and configuration files. That makes it useful for teams that
  need one knowledge layer across SDK docs, internal docs, and code-adjacent reference
  material. Grounded Docs supports both CLI-first and long-running MCP usage. You
  can scrape a library, query the local index, fetch a single page as Markdown, or
  run the service as an MCP endpoint and connect it to clients such as Claude, Cline,
  Copilot, or Gemini CLI. The README also documents a local web UI and optional embedding-model
  configuration for better semantic search. In practice, this skill is a good fit
  for developers who want grounded library and API answers, repeatable doc indexing,
  and safer coding workflows built on current upstream documentation rather than hallucinated
  references.'
verification: security_reviewed
source: https://github.com/arabold/docs-mcp-server
category:
- Library &amp; API Reference
framework:
- MCP
tool_ecosystem:
  github_repo: arabold/docs-mcp-server
  github_stars: 1209
---

# Grounded Docs MCP Server

Grounded Docs MCP Server is an open-source documentation retrieval system for AI coding assistants and other MCP-compatible tools. The project is published as @arabold/docs-mcp-server and positions itself as an alternative to hosted documentation tools like Context7 and Ref.Tools. Its practical job-to-be-done is simple: give an agent reliable, version-specific documentation instead of making it guess from stale model memory or generic web search. The server can ingest documentation from official websites, GitHub repositories, npm packages, PyPI packages, local folders, and archive files. According to the upstream README, it supports a wide range of formats including HTML, Markdown, PDF, Office documents, notebooks, source code, structured data files, and configuration files. That makes it useful for teams that need one knowledge layer across SDK docs, internal docs, and code-adjacent reference material. Grounded Docs supports both CLI-first and long-running MCP usage. You can scrape a library, query the local index, fetch a single page as Markdown, or run the service as an MCP endpoint and connect it to clients such as Claude, Cline, Copilot, or Gemini CLI. The README also documents a local web UI and optional embedding-model configuration for better semantic search. In practice, this skill is a good fit for developers who want grounded library and API answers, repeatable doc indexing, and safer coding workflows built on current upstream documentation rather than hallucinated references.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grounded-docs-mcp-server/)
