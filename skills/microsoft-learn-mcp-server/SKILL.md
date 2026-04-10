---
title: "Microsoft Learn MCP Server"
description: "Microsoft Learn MCP Server gives agents and IDE assistants direct access to official Microsoft documentation and code samples through a hosted MCP endpoint. It is built to reduce hallucinations around Azure, .NET, Microsoft 365, and other Microsoft platforms by grounding answers in first-party docs."
slug: "microsoft-learn-mcp-server"
category:
  - "Library &amp; API Reference"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://github.com/MicrosoftDocs/mcp"
tool_ecosystem:
  github_repo: "MicrosoftDocs/mcp"
  github_stars: 1533
listed: true
---

# Microsoft Learn MCP Server

Microsoft Learn MCP Server gives agents and IDE assistants direct access to official Microsoft documentation and code samples through a hosted MCP endpoint. It is built to reduce hallucinations around Azure, .NET, Microsoft 365, and other Microsoft platforms by grounding answers in first-party docs.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install microsoft-learn-mcp-server
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Microsoft Learn MCP Server is Microsoft's official MCP service for retrieving trusted documentation and code samples from Microsoft Learn. The upstream repository describes it as a free, no-auth way to connect MCP-capable assistants to real Microsoft documentation instead of relying on stale training data or random web results. Its core job-to-be-done is to help agents answer technical Microsoft questions with current, first-party material.
The server exposes tools for semantic documentation search, page fetching, and official code sample discovery. In the README, Microsoft documents three core capabilities: microsoft_docs_search, microsoft_docs_fetch, and microsoft_code_sample_search. That means an assistant can locate official Azure guidance, fetch the exact page in markdown form, and search Microsoft-maintained snippets for runnable examples. For teams building on Azure, .NET, Microsoft 365, or AI Foundry, that is a practical reference layer rather than a generic search wrapper.
The project also includes the @microsoft/learn-cli package for terminal use, and the hosted MCP endpoint works with any client that supports Streamable HTTP. Microsoft explicitly calls out clients such as Claude, Cursor, Copilot, and Codex. Because it is tied to first-party documentation and does not require separate credentials, this skill is especially useful when an agent needs high-trust answers about SDK methods, service limits, configuration steps, regional availability, or code samples from the official Microsoft ecosystem.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/microsoft-learn-mcp-server/)
