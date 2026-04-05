---
name: "Qdrant MCP Server for Vector Search and Semantic Memory"
description: "An official Qdrant MCP server implementation that provides semantic memory capabilities for AI agents. Enables storing and retrieving information using vector search, acting as a persistent knowledge layer on top of the Qdrant vector database."
category: "Integrations &amp; Connectors"
framework: "MCP"
verification: security_reviewed
source: "https://github.com/qdrant/mcp-server-qdrant"
tool_ecosystem:
  github_repo: "qdrant/mcp-server-qdrant"
  github_stars: 1314
---
# Qdrant MCP Server for Vector Search and Semantic Memory

An official Qdrant MCP server implementation that provides semantic memory capabilities for AI agents. Enables storing and retrieving information using vector search, acting as a persistent knowledge layer on top of the Qdrant vector database.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill qdrant-mcp-server-vector-search-semantic-memory
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill qdrant-mcp-server-vector-search-semantic-memory -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill qdrant-mcp-server-vector-search-semantic-memory -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill qdrant-mcp-server-vector-search-semantic-memory -a codex
```

### OpenClaw

```bash
clawhub install qdrant-mcp-server-vector-search-semantic-memory
```

## Details

The Qdrant MCP Server is an official Model Context Protocol implementation from the Qdrant team that turns the Qdrant vector search engine into a semantic memory layer for AI agents. Available at github.com/qdrant/mcp-server-qdrant, it provides two core tools: qdrant-store for saving information with optional metadata, and qdrant-find for retrieving relevant information using semantic similarity search.

The server works by embedding text using configurable embedding models (defaulting to sentence-transformers/all-MiniLM-L6-v2 via FastEmbed) and storing the vectors in Qdrant collections. When an AI agent needs to recall information, it sends a natural language query, and the server returns the most semantically similar stored items. This creates a persistent, searchable memory that survives across conversation sessions.

Configuration is handled entirely through environment variables: QDRANT_URL for connecting to a remote Qdrant instance, QDRANT_LOCAL_PATH for local file-based storage, COLLECTION_NAME for specifying the default collection, and EMBEDDING_MODEL for choosing the embedding model. The server supports stdio, SSE, and streamable-http transports, making it compatible with both local and remote MCP client setups.

Built on FastMCP, the server can be run instantly with uvx (no installation needed) and integrates with Claude Desktop, Cursor, and other MCP clients through standard configuration. With over 1,100 GitHub stars and 187 forks, it serves as both a production-ready memory solution and a reference implementation for building custom MCP servers on top of vector databases.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/qdrant-mcp-server-vector-search-semantic-memory/)
