---
name: "Query Eventhouse and manage Fabric RTI resources from MCP-compatible agents with Fabric RTI MCP"
slug: "query-eventhouse-and-manage-fabric-rti-resources-from-mcp-compatible-agents-with-fabric-rti-mcp"
description: "Use Fabric RTI MCP when an agent needs tool-callable access to Microsoft Fabric Real-Time Intelligence services such as Eventhouse, Eventstreams, Activator, and Map instead of sending the user back to the Fabric UI or wiring custom SDK glue."
github_stars: 111
verification: "security_reviewed"
source: "https://github.com/microsoft/fabric-rti-mcp"
author: "Microsoft"
publisher_type: "Organization"
category: "Integrations & Connectors"
framework: "MCP"
tool_ecosystem:
  github_repo: "microsoft/fabric-rti-mcp"
  github_stars: 111
---

# Query Eventhouse and manage Fabric RTI resources from MCP-compatible agents with Fabric RTI MCP

Use Fabric RTI MCP when an agent needs tool-callable access to Microsoft Fabric Real-Time Intelligence services such as Eventhouse, Eventstreams, Activator, and Map instead of sending the user back to the Fabric UI or wiring custom SDK glue.

## Prerequisites

MCP-compatible client; Python with uvx or equivalent; Microsoft Fabric RTI access via Azure Identity

## Installation

Use the upstream install or setup path that matches your environment:
- Install uv
- pip install -e ".[dev]"

Requirements and caveats from upstream:
- Make sure you have Python 3.10+ installed properly and added to your PATH.
- Assuming you have python installed and the repo cloned:
- Use the Python: Attach configuration in your launch.json to attach to the running server.

Basic usage or getting-started notes:
- ### 🔍 Example Prompts
- **kusto_diagnostics** - Run a best-effort suite of cluster diagnostic commands and return a unified summary. Sections: capacity (resource slots), cluster (nodes/hardware), principal roles (caller permissions), interna...
- Install either the stable or Insiders release of VS Code:

- Source: https://github.com/microsoft/fabric-rti-mcp
- Extracted from upstream docs: https://raw.githubusercontent.com/microsoft/fabric-rti-mcp/HEAD/README.md

## Documentation

- https://github.com/microsoft/fabric-rti-mcp

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/query-eventhouse-and-manage-fabric-rti-resources-from-mcp-compatible-agents-with-fabric-rti-mcp/)
