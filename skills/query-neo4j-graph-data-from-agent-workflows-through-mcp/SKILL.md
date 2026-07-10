---
title: "Query Neo4j graph data from agent workflows through MCP"
description: "Connect MCP-compatible agents to Neo4j so they can inspect graph schemas, run Cypher queries, manage graph memory, and operate Aura instances from chat."
verification: "security_reviewed"
source: "https://github.com/neo4j-contrib/mcp-neo4j"
author: "Neo4j Labs"
publisher_type: "organization"
category:
  - "Data Extraction & Transformation"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "neo4j-contrib/mcp-neo4j"
  github_stars: 947
---

# Query Neo4j graph data from agent workflows through MCP

Connect MCP-compatible agents to Neo4j so they can inspect graph schemas, run Cypher queries, manage graph memory, and operate Aura instances from chat.

## Prerequisites

Neo4j database or Aura account, APOC for schema inspection, Python package or uvx, MCP-compatible client

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the needed server package such as `pip install mcp-neo4j-memory` or run it with `uvx mcp-neo4j-memory@0.4.5`, then add the server command and Neo4j URL, username, and password to the MCP client configuration.
```

## Documentation

- https://neo4j.com/developer/genai-ecosystem/model-context-protocol-mcp/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/query-neo4j-graph-data-from-agent-workflows-through-mcp/)
