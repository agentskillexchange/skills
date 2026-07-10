---
title: "Scan agentic codebases for exposed tools MCP usage and mapped security findings with Agentic Radar"
description: "Generate a reviewable security report for a supported agent workflow before deployment by scanning its code, tools, MCP usage, and known vulnerability surface."
verification: "security_reviewed"
source: "https://github.com/splx-ai/agentic-radar"
author: "SPLX AI"
publisher_type: "organization"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "splx-ai/agentic-radar"
  github_stars: 953
---

# Scan agentic codebases for exposed tools MCP usage and mapped security findings with Agentic Radar

Generate a reviewable security report for a supported agent workflow before deployment by scanning its code, tools, MCP usage, and known vulnerability surface.

## Prerequisites

Python with pip, Agentic Radar CLI, a supported agent framework codebase such as LangGraph, CrewAI, n8n, OpenAI Agents, or AutoGen, local shell access

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with pip install agentic-radar, add any documented framework extras if needed, then run the scan command against the target workflow folder to generate and review the HTML security report before deployment.
```

## Documentation

- https://github.com/splx-ai/agentic-radar

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-agentic-codebases-for-exposed-tools-mcp-usage-and-mapped-security-findings-with-agentic-radar/)
