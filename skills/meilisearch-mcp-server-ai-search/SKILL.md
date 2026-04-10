---
name: "Meilisearch MCP Server for AI-Powered Search Integration"
description: "Official Model Context Protocol server that connects LLMs to Meilisearch for lightning-fast search, index management, and document operations via natural language. Enables AI agents to manage search infrastructure through conversation."
verification: security_reviewed
source: "https://github.com/meilisearch/meilisearch-mcp"
category:
  - "Developer Tools"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "meilisearch/meilisearch-mcp"
  github_stars: 181
---

# Meilisearch MCP Server for AI-Powered Search Integration

The Meilisearch MCP Server is the official Model Context Protocol server published by the Meilisearch team that enables any MCP-compatible client — including Claude, OpenAI agents, and other LLM interfaces — to interact directly with Meilisearch search instances. Built in Python and available on PyPI as meilisearch-mcp, it uses stdio transport to expose the full Meilisearch API surface through natural language conversation.
This skill allows AI agents to perform the complete range of Meilisearch operations without writing a single line of code. Agents can create and configure search indices, add and update documents, execute searches with advanced filtering and faceted navigation, tune ranking rules, manage API keys, and monitor task progress. The server supports dynamic connections, letting agents switch between multiple Meilisearch instances on the fly — useful for multi-tenant applications or staging/production workflows.
Meilisearch itself is a lightning-fast, typo-tolerant search engine with over 50,000 GitHub stars. It provides AI-powered hybrid search combining keyword and semantic search, making it a popular choice for e-commerce product search, documentation sites, and application search features. The MCP server brings all of these capabilities into the agent workflow, enabling use cases like automated index rebuilding after content updates, search relevancy tuning through conversation, and batch document ingestion from various data sources.
Installation is straightforward via pip install meilisearch-mcp or using uvx. Configuration requires only adding the server to your MCP client config (e.g., Claude Desktop or Cursor) and pointing it at a running Meilisearch instance. The server handles connection management, authentication via API keys, and graceful error handling. A TypeScript implementation is also available for Node.js environments.
Key technical features include full index and document CRUD operations, multi-index search, settings configuration for synonyms, stop words, ranking rules, and filterable/sortable attributes, task monitoring for async operations, health checks, and API key management with fine-grained permissions.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/meilisearch-mcp-server-ai-search/)
