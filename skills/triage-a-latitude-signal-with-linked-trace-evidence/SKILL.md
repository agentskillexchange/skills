---
name: "Triage a Latitude signal with linked trace evidence"
slug: "triage-a-latitude-signal-with-linked-trace-evidence"
description: "Investigate one agent failure signal through lifecycle, trends, model slices and spans, then return an evidence-backed engineering brief."
github_stars: 4755
verification: "security_reviewed"
source: "https://github.com/latitude-dev/latitude-llm"
author: "Latitude"
publisher_type: "Organization"
category: "Runbooks & Diagnostics"
framework: "MCP"
tool_ecosystem:
  github_repo: "latitude-dev/latitude-llm"
  github_stars: 4755
---

# Triage a Latitude signal with linked trace evidence

Investigate one agent failure signal through lifecycle, trends, model slices and spans, then return an evidence-backed engineering brief.

## Prerequisites

Latitude organization with existing traces; authorized Latitude MCP connection; MCP-capable agent

## Installation

Install or set up from the source-backed instructions:

Use the official Latitude MCP guide at https://docs.latitude.so/getting-started/mcp to configure a Remote Streamable HTTP MCP connection to https://api.latitude.so/v1/mcp in an MCP-capable runtime. An authorized operator must connect the intended live organization before invocation. Verify the connection exposes getSignal, getSignalTrend, listSignalTraces and trace/span read tools; inspect current schemas. No telemetry SDK installation is required for an already instrumented project. Read the pinned workflow reference https://github.com/latitude-dev/latitude-llm/blob/f81de983fcb63a6c4c1094014c92c5bd9e52244d/docs/agent-dispatch/overview.mdx. No authentication or installation was performed during discovery.

- Source: https://github.com/latitude-dev/latitude-llm

## Documentation

- https://github.com/latitude-dev/latitude-llm/blob/f81de983fcb63a6c4c1094014c92c5bd9e52244d/docs/agent-dispatch/overview.mdx

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/triage-a-latitude-signal-with-linked-trace-evidence/)
