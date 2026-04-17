---
title: "Qdrant MCP Server for Vector Search and Semantic Memory"
description: "The Qdrant MCP Server is an official Model Context Protocol implementation from the Qdrant team that turns the Qdrant vector search engine into a semantic memory layer for AI agents. Available at github.com/qdrant/mcp-server-qdrant, it provides two core tools: qdrant-store for saving information with optional metadata, and qdrant-find for retrieving relevant information using semantic similarity search.\nThe server works by embedding text using configurable embedding models (defaulting to sentence-transformers/all-MiniLM-L6-v2 via FastEmbed) and storing the vectors in Qdrant collections. When an AI agent needs to recall information, it sends a natural language query, and the server returns the most semantically similar stored items. This creates a persistent, searchable memory that survives across conversation sessions.\nConfiguration is handled entirely through environment variables: QDRANT_URL for connecting to a remote Qdrant instance, QDRANT_LOCAL_PATH for local file-based storage, COLLECTION_NAME for specifying the default collection, and EMBEDDING_MODEL for choosing the embedding model. The server supports stdio, SSE, and streamable-http transports, making it compatible with both local and remote MCP client setups.\nBuilt on FastMCP, the server can be run instantly with uvx (no installation needed) and integrates with Claude Desktop, Cursor, and other MCP clients through standard configuration. With over 1,100 GitHub stars and 187 forks, it serves as both a production-ready memory solution and a reference implementation for building custom MCP servers on top of vector databases."
verification: security_reviewed
source: "https://github.com/qdrant/mcp-server-qdrant"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "qdrant/mcp-server-qdrant"
  github_stars: 1314
---

# Qdrant MCP Server for Vector Search and Semantic Memory

The Qdrant MCP Server is an official Model Context Protocol implementation from the Qdrant team that turns the Qdrant vector search engine into a semantic memory layer for AI agents. Available at github.com/qdrant/mcp-server-qdrant, it provides two core tools: qdrant-store for saving information with optional metadata, and qdrant-find for retrieving relevant information using semantic similarity search.
The server works by embedding text using configurable embedding models (defaulting to sentence-transformers/all-MiniLM-L6-v2 via FastEmbed) and storing the vectors in Qdrant collections. When an AI agent needs to recall information, it sends a natural language query, and the server returns the most semantically similar stored items. This creates a persistent, searchable memory that survives across conversation sessions.
Configuration is handled entirely through environment variables: QDRANT_URL for connecting to a remote Qdrant instance, QDRANT_LOCAL_PATH for local file-based storage, COLLECTION_NAME for specifying the default collection, and EMBEDDING_MODEL for choosing the embedding model. The server supports stdio, SSE, and streamable-http transports, making it compatible with both local and remote MCP client setups.
Built on FastMCP, the server can be run instantly with uvx (no installation needed) and integrates with Claude Desktop, Cursor, and other MCP clients through standard configuration. With over 1,100 GitHub stars and 187 forks, it serves as both a production-ready memory solution and a reference implementation for building custom MCP servers on top of vector databases.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/qdrant-mcp-server-vector-search-semantic-memory
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/qdrant-mcp-server-vector-search-semantic-memory` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/qdrant-mcp-server-vector-search-semantic-memory/)
