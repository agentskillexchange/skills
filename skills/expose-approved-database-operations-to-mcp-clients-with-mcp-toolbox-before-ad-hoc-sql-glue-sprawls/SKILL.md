---
name: "Expose approved database operations to MCP clients with MCP Toolbox before ad hoc SQL glue sprawls"
slug: "expose-approved-database-operations-to-mcp-clients-with-mcp-toolbox-before-ad-hoc-sql-glue-sprawls"
description: "Use MCP Toolbox to turn database access into a constrained MCP tool surface, with prebuilt or custom tools that agents can call without hand-rolled wrappers for every project."
github_stars: 14664
verification: "security_reviewed"
source: "https://github.com/googleapis/mcp-toolbox"
author: "Google Cloud"
publisher_type: "organization"
category: "Integrations & Connectors"
framework: "MCP"
tool_ecosystem:
  github_repo: "googleapis/mcp-toolbox"
  github_stars: 14664
---

# Expose approved database operations to MCP clients with MCP Toolbox before ad hoc SQL glue sprawls

Use MCP Toolbox to turn database access into a constrained MCP tool surface, with prebuilt or custom tools that agents can call without hand-rolled wrappers for every project.

## Prerequisites

MCP Toolbox server, database credentials, an MCP-capable client such as Claude Code or Codex

## Installation

Use the upstream install or setup path that matches your environment:
- pip install toolbox-core
- pip install toolbox-langchain
- pip install toolbox-llamaindex
- npm install @toolbox-sdk/core

Requirements and caveats from upstream:
- [![Python SDK](https://img.shields.io/pypi/v/toolbox-core?logo=python&logoColor=white&label=Python%20SDK)](https://pypi.org/project/toolbox-core/)
- *See the [Install & Run the Toolbox server](#install--run-the-toolbox-server) section for different execution methods like Docker or binaries.*
- <summary>Python (<a href="https://github.com/googleapis/mcp-toolbox-sdk-python">Github</a>)</summary>

Basic usage or getting-started notes:
- **Custom Tools Framework (Run-Time):** A robust framework to build specialized, highly secure AI tools for your production agents. Define structured queries, semantic search, and NL2SQL capabilities safely and easily.
- [Quick Start: Prebuilt Tools](#quick-start-prebuilt-tools)
- [Quick Start: Custom Tools](#quick-start-custom-tools)

- Source: https://github.com/googleapis/mcp-toolbox
- Extracted from upstream docs: https://raw.githubusercontent.com/googleapis/mcp-toolbox/HEAD/README.md

## Documentation

- https://mcp-toolbox.dev/documentation/introduction/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/expose-approved-database-operations-to-mcp-clients-with-mcp-toolbox-before-ad-hoc-sql-glue-sprawls/)
