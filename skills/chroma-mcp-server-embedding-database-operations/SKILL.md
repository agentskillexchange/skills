---
title: Chroma MCP Server for Embedding Database Operations
description: 'The Chroma MCP Server is an official Model Context Protocol integration
  from the Chroma team that brings the power of the Chroma embedding database to AI
  assistants. Available at github.com/chroma-core/chroma-mcp , this server allows
  LLMs to create and manage vector collections, store documents with embeddings, and
  perform sophisticated retrieval operations — all through MCP tool calls. The server
  provides a comprehensive set of tools covering collection management (create, modify,
  delete, list, peek, get info, get count) and document operations (add, query, get,
  update, delete). Query capabilities include semantic vector search, full-text search,
  and advanced metadata filtering, giving AI agents flexible retrieval options depending
  on the use case. Collection creation supports configuring HNSW parameters for optimized
  vector search performance. Multiple embedding functions are supported out of the
  box: default, Cohere, OpenAI, Jina, VoyageAI, and Roboflow. The server leverages
  Chroma’s collection configuration persistence (introduced in v1.0.0), which means
  once a collection is created with a specific embedding function, subsequent queries
  and inserts automatically use the same function without re-specification. Deployment
  flexibility is a key strength. The server supports four client types: ephemeral
  (in-memory for testing), persistent (file-based storage), HTTP (for self-hosted
  Chroma instances), and cloud (automatic connection to Chroma Cloud at api.trychroma.com).
  Installation is as simple as running uvx chroma-mcp, and configuration is done through
  claude_desktop_config.json or equivalent MCP client settings. With 515+ stars and
  backing from the Chroma core team, this server provides a production-ready way to
  give AI agents long-term memory and knowledge retrieval capabilities.'
verification: security_reviewed
source: https://github.com/chroma-core/chroma-mcp
category:
- Integrations &amp; Connectors
framework:
- MCP
tool_ecosystem:
  github_repo: chroma-core/chroma-mcp
  github_stars: 527
---

# Chroma MCP Server for Embedding Database Operations

The Chroma MCP Server is an official Model Context Protocol integration from the Chroma team that brings the power of the Chroma embedding database to AI assistants. Available at github.com/chroma-core/chroma-mcp , this server allows LLMs to create and manage vector collections, store documents with embeddings, and perform sophisticated retrieval operations — all through MCP tool calls. The server provides a comprehensive set of tools covering collection management (create, modify, delete, list, peek, get info, get count) and document operations (add, query, get, update, delete). Query capabilities include semantic vector search, full-text search, and advanced metadata filtering, giving AI agents flexible retrieval options depending on the use case. Collection creation supports configuring HNSW parameters for optimized vector search performance. Multiple embedding functions are supported out of the box: default, Cohere, OpenAI, Jina, VoyageAI, and Roboflow. The server leverages Chroma’s collection configuration persistence (introduced in v1.0.0), which means once a collection is created with a specific embedding function, subsequent queries and inserts automatically use the same function without re-specification. Deployment flexibility is a key strength. The server supports four client types: ephemeral (in-memory for testing), persistent (file-based storage), HTTP (for self-hosted Chroma instances), and cloud (automatic connection to Chroma Cloud at api.trychroma.com). Installation is as simple as running uvx chroma-mcp, and configuration is done through claude_desktop_config.json or equivalent MCP client settings. With 515+ stars and backing from the Chroma core team, this server provides a production-ready way to give AI agents long-term memory and knowledge retrieval capabilities.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/chroma-mcp-server-embedding-database-operations/)
