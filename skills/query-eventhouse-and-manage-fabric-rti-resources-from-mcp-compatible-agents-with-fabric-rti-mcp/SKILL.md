---
title: "Query Eventhouse and manage Fabric RTI resources from MCP-compatible agents with Fabric RTI MCP"
description: "Use Fabric RTI MCP when an agent needs tool-callable access to Microsoft Fabric Real-Time Intelligence services such as Eventhouse, Eventstreams, Activator, and Map instead of sending the user back to the Fabric UI or wiring custom SDK glue."
verification: "listed"
source: "https://github.com/microsoft/fabric-rti-mcp"
category:
  - "Integrations & Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "microsoft/fabric-rti-mcp"
  github_stars: 111
---

# Query Eventhouse and manage Fabric RTI resources from MCP-compatible agents with Fabric RTI MCP

Fabric RTI MCP is an MCP server that exposes Microsoft Fabric Real-Time Intelligence operations as agent-callable tools, including KQL querying for Eventhouse or Azure Data Explorer, Eventstream management, Activator trigger setup, and Map operations. It gives an agent a concrete invoke surface for analytics and streaming tasks inside an MCP workflow. Invoke this instead of using the product normally when the user wants an MCP-compatible agent to inspect schemas, run KQL, manage streaming resources, or prepare alerts from the same conversational loop. The scope boundary is the MCP bridge and agent tool workflow; that keeps it from being merely a Microsoft Fabric product listing or generic cloud platform card.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/query-eventhouse-and-manage-fabric-rti-resources-from-mcp-compatible-agents-with-fabric-rti-mcp/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/query-eventhouse-and-manage-fabric-rti-resources-from-mcp-compatible-agents-with-fabric-rti-mcp
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/query-eventhouse-and-manage-fabric-rti-resources-from-mcp-compatible-agents-with-fabric-rti-mcp`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/query-eventhouse-and-manage-fabric-rti-resources-from-mcp-compatible-agents-with-fabric-rti-mcp/)
