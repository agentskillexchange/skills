---
name: "Connect agents to OpenRAG knowledge bases over MCP"
slug: "connect-agents-to-openrag-knowledge-bases-over-mcp"
description: "Use OpenRAG's built-in MCP endpoint so agents can ingest documents, search a knowledge base, create filters, and run RAG-backed chat against a deployed OpenRAG instance."
github_stars: 4368
verification: "security_reviewed"
source: "https://github.com/langflow-ai/openrag"
author: "Langflow AI"
publisher_type: "organization"
category: "Integrations & Connectors"
framework: "MCP"
tool_ecosystem:
  github_repo: "langflow-ai/openrag"
  github_stars: 4368
  npm_package: "openrag-sdk"
  npm_weekly_downloads: 52
---

# Connect agents to OpenRAG knowledge bases over MCP

Use OpenRAG's built-in MCP endpoint so agents can ingest documents, search a knowledge base, create filters, and run RAG-backed chat against a deployed OpenRAG instance.

## Prerequisites

OpenRAG deployment; OpenRAG API key; MCP client with streamable HTTP support such as Cursor, Claude Desktop, IBM Bob, or another MCP-capable agent runtime

## Installation

Deploy or run OpenRAG first, then connect your MCP client to the built-in HTTP endpoint.

For the documented self-managed deployment, install Python, uv, and Docker or Podman, then clone and configure the upstream project:

- git clone https://github.com/langflow-ai/openrag.git
- cd openrag
- cp .env.example .env

Configure the required .env values such as OPENSEARCH_PASSWORD, model provider credentials, and Langflow credentials. Then start Docling with the documented uv command, using scripts/docling_ctl.py start --port 5001, before launching the OpenRAG containers:

- docker compose up -d

For a terminal-managed evaluation install, upstream also documents uvx --python 3.13 openrag.

Configure your MCP client to use the running OpenRAG instance at /mcp with the same OpenRAG API key used for the REST API:

{
  "mcpServers": {
    "openrag": {
      "url": "http://localhost:3000/mcp",
      "headers": {
        "X-API-Key": "orag_your_api_key_here"
      }
    }
  }
}

Do not install the deprecated openrag-mcp package; OpenRAG now serves MCP directly from the /mcp endpoint.

- Source: https://github.com/langflow-ai/openrag
- Extracted from upstream docs: https://raw.githubusercontent.com/langflow-ai/openrag/HEAD/README.md

## Documentation

- https://github.com/langflow-ai/openrag/tree/main/sdks/mcp

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/connect-agents-to-openrag-knowledge-bases-over-mcp/)
