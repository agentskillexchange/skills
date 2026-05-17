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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install in an MCP client using the upstream Python package, for example with `uvx microsoft-fabric-rti-mcp`, then authenticate with Azure Identity and configure access to the target Fabric RTI resources.
```

## Documentation

- https://github.com/microsoft/fabric-rti-mcp

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/query-eventhouse-and-manage-fabric-rti-resources-from-mcp-compatible-agents-with-fabric-rti-mcp/)
