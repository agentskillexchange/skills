---
name: "Qdrant MCP Server for Vector Search and Semantic Memory"
slug: "qdrant-mcp-server-vector-search-semantic-memory"
description: "An official Qdrant MCP server implementation that provides semantic memory capabilities for AI agents. Enables storing and retrieving information using vector search, acting as a persistent knowledge layer on top of the Qdrant vector database."
github_stars: 1314
verification: "security_reviewed"
source: "https://github.com/qdrant/mcp-server-qdrant"
category: "Integrations & Connectors"
framework: "MCP"
tool_ecosystem:
  github_repo: "qdrant/mcp-server-qdrant"
  github_stars: 1314
---

# Qdrant MCP Server for Vector Search and Semantic Memory

An official Qdrant MCP server implementation that provides semantic memory capabilities for AI agents. Enables storing and retrieving information using vector search, acting as a persistent knowledge layer on top of the Qdrant vector database.

## Installation

Use the upstream install or setup path that matches your environment:
- docker build -t mcp-server-qdrant .
- docker run -p 8000:8000 \
- npx @smithery/cli install mcp-server-qdrant --client claude
- [![Install with Docker in VS Code](https://img.shields.io/badge/VS_Code-Docker-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=qdrant&config=%7B%2...

Requirements and caveats from upstream:
- ### Using Docker
- necessary when running the server in a Docker container.
- The value of 'metadata' is a Python dictionary with strings as keys. \

Basic usage or getting-started notes:
- This repository is an example of how to create a MCP server for [Qdrant](https://qdrant.tech/), a vector search engine.
- | FASTMCP_SERVER_PORT | Port to run the server on | 8000 |
- ### Using uvx

- Source: https://github.com/qdrant/mcp-server-qdrant
- Extracted from upstream docs: https://raw.githubusercontent.com/qdrant/mcp-server-qdrant/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/qdrant-mcp-server-vector-search-semantic-memory/)
