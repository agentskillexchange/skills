---
title: "Scan MCP servers for security findings before connecting them to agents with MCP Scanner"
description: "Run MCP Scanner against a remote or local MCP server before trusting it, so the agent gets a bounded security review of tools, prompts, resources, dependencies, and supply-chain risk."
verification: "security_reviewed"
source: "https://github.com/cisco-ai-defense/mcp-scanner"
category:
  - "Security & Verification"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "cisco-ai-defense/mcp-scanner"
  github_stars: 889
---

# Scan MCP servers for security findings before connecting them to agents with MCP Scanner

MCP Scanner is a pre-connection security review workflow for Model Context Protocol servers. The agent uses it to inspect an MCP server, its tools, prompts, resources, dependencies, and bundled files before that server is connected to a broader agent environment.

Invoke this when you are evaluating whether an MCP server is safe enough to trust, especially before adding it to a production agent setup, CI gate, or shared team catalog. This is different from using the MCP server normally, because the job here is to audit the server first, not to consume its capabilities.

The scope boundary is narrow and skill-shaped: security scanning of MCP servers and their attached surfaces. It is not a general SDK, not a generic security platform card, and not a broad AI product listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/scan-mcp-servers-for-security-findings-before-connecting-them-to-agents-with-mcp-scanner/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/scan-mcp-servers-for-security-findings-before-connecting-them-to-agents-with-mcp-scanner
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/scan-mcp-servers-for-security-findings-before-connecting-them-to-agents-with-mcp-scanner`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-mcp-servers-for-security-findings-before-connecting-them-to-agents-with-mcp-scanner/)
