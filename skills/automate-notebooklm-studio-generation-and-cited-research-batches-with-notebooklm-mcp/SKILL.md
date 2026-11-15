---
name: "Automate NotebookLM Studio generation and cited research batches with notebooklm-mcp"
slug: "automate-notebooklm-studio-generation-and-cited-research-batches-with-notebooklm-mcp"
description: "Use NotebookLM through MCP or a local REST API to run cited Q&A, generate Studio artifacts, and manage high-volume research batches."
github_stars: 161
verification: "security_reviewed"
source: "https://github.com/roomi-fields/notebooklm-mcp"
author: "Romain Peyrichou"
publisher_type: "individual"
category: "Research & Scraping"
framework: "MCP"
tool_ecosystem:
  github_repo: "roomi-fields/notebooklm-mcp"
  github_stars: 161
  npm_package: "@roomi-fields/notebooklm-mcp"
  npm_weekly_downloads: 3532
---

# Automate NotebookLM Studio generation and cited research batches with notebooklm-mcp

Use NotebookLM through MCP or a local REST API to run cited Q&A, generate Studio artifacts, and manage high-volume research batches.

## Prerequisites

Node.js >=18, @roomi-fields/notebooklm-mcp, MCP client or local HTTP REST API, Google NotebookLM/Gemini Notebook account

## Installation

Install or set up from the source-backed instructions:

For REST mode, clone https://github.com/roomi-fields/notebooklm-mcp, run npm install && npm run build, run npm run setup-auth once in a terminal, then start the API with npm run start:http. For MCP mode, build the same package and register dist/index.js with the MCP client, for example claude mcp add notebooklm node /path/to/notebooklm-mcp/dist/index.js. The project also publishes @roomi-fields/notebooklm-mcp on npm.

- Source: https://github.com/roomi-fields/notebooklm-mcp

## Documentation

- https://roomi-fields.github.io/notebooklm-mcp/notebooklm-rest-api

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/automate-notebooklm-studio-generation-and-cited-research-batches-with-notebooklm-mcp/)
