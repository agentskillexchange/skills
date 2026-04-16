---
title: "Microsoft Learn MCP Server"
description: "Microsoft Learn MCP Server gives agents and IDE assistants direct access to official Microsoft documentation and code samples through a hosted MCP endpoint. It is built to reduce hallucinations around Azure, .NET, Microsoft 365, and other Microsoft platforms by grounding answers in first-party docs."
verification: "security_reviewed"
source: "https://github.com/MicrosoftDocs/mcp"
category:
  - "Library & API Reference"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "MicrosoftDocs/mcp"
  github_stars: 1536
---

# Microsoft Learn MCP Server

Microsoft Learn MCP Server is Microsoft's official MCP service for retrieving trusted documentation and code samples from Microsoft Learn. The upstream repository describes it as a free, no-auth way to connect MCP-capable assistants to real Microsoft documentation instead of relying on stale training data or random web results. Its core job-to-be-done is to help agents answer technical Microsoft questions with current, first-party material.


The server exposes tools for semantic documentation search, page fetching, and official code sample discovery. In the README, Microsoft documents three core capabilities: microsoft_docs_search, microsoft_docs_fetch, and microsoft_code_sample_search. That means an assistant can locate official Azure guidance, fetch the exact page in markdown form, and search Microsoft-maintained snippets for runnable examples. For teams building on Azure, .NET, Microsoft 365, or AI Foundry, that is a practical reference layer rather than a generic search wrapper.


The project also includes the @microsoft/learn-cli package for terminal use, and the hosted MCP endpoint works with any client that supports Streamable HTTP. Microsoft explicitly calls out clients such as Claude, Cursor, Copilot, and Codex. Because it is tied to first-party documentation and does not require separate credentials, this skill is especially useful when an agent needs high-trust answers about SDK methods, service limits, configuration steps, regional availability, or code samples from the official Microsoft ecosystem.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/microsoft-learn-mcp-server/)
