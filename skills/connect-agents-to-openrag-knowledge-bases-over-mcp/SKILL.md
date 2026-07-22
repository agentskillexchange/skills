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

Use the upstream install or setup path that matches your environment:
- <img src="./docs/static/img/uv_run_openrag.png" alt="Use uv run openrag to start" width="300"/>
- pip install openrag-sdk
- npm install openrag-sdk

Requirements and caveats from upstream:
- [Install the OpenRAG Python package](https://docs.openr.ag/install-options)
- [Deploy self-managed services with Docker or Podman](https://docs.openr.ag/docker)
- 📖 [Full Python SDK Documentation](https://pypi.org/project/openrag-sdk/)

Basic usage or getting-started notes:
- **Pre-packaged & ready to run** - All core tools are hooked up and ready to go, just install and run
- **Quick Example:**
- asyncio.run(main())

- Source: https://github.com/langflow-ai/openrag
- Extracted from upstream docs: https://raw.githubusercontent.com/langflow-ai/openrag/HEAD/README.md

## Documentation

- https://github.com/langflow-ai/openrag/tree/main/sdks/mcp

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/connect-agents-to-openrag-knowledge-bases-over-mcp/)
