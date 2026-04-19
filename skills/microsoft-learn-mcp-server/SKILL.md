---
title: "Microsoft Learn MCP Server"
description: "Microsoft Learn MCP Server is Microsoft&apos;s official MCP service for retrieving trusted documentation and code samples from Microsoft Learn. The upstream repository describes it as a free, no-auth way to connect MCP-capable assistants to real Microsoft documentation instead of relying on stale training data or random web results. Its core job-to-be-done is to help agents answer technical Microsoft questions with current, first-party material. The server exposes tools for semantic documentation search, page fetching, and official code sample discovery. In the README, Microsoft documents three core capabilities: microsoft_docs_search , microsoft_docs_fetch , and microsoft_code_sample_search . That means an assistant can locate official Azure guidance, fetch the exact page in markdown form, and search Microsoft-maintained snippets for runnable examples. For teams building on Azure, .NET, Microsoft 365, or AI Foundry, that is a practical reference layer rather than a generic search wrapper. The project also includes the @microsoft/learn-cli package for terminal use, and the hosted MCP endpoint works with any client that supports Streamable HTTP. Microsoft explicitly calls out clients such as Claude, Cursor, Copilot, and Codex. Because it is tied to first-party documentation and does not require separate credentials, this skill is especially useful when an agent needs high-trust answers about SDK methods, service limits, configuration steps, regional availability, or code samples from the official Microsoft ecosystem."
source: "https://github.com/MicrosoftDocs/mcp"
verification: "security_reviewed"
category:
  - "Library &amp; API Reference"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "MicrosoftDocs/mcp"
  github_stars: 1536
---

# Microsoft Learn MCP Server

Microsoft Learn MCP Server is Microsoft&apos;s official MCP service for retrieving trusted documentation and code samples from Microsoft Learn. The upstream repository describes it as a free, no-auth way to connect MCP-capable assistants to real Microsoft documentation instead of relying on stale training data or random web results. Its core job-to-be-done is to help agents answer technical Microsoft questions with current, first-party material. The server exposes tools for semantic documentation search, page fetching, and official code sample discovery. In the README, Microsoft documents three core capabilities: microsoft_docs_search , microsoft_docs_fetch , and microsoft_code_sample_search . That means an assistant can locate official Azure guidance, fetch the exact page in markdown form, and search Microsoft-maintained snippets for runnable examples. For teams building on Azure, .NET, Microsoft 365, or AI Foundry, that is a practical reference layer rather than a generic search wrapper. The project also includes the @microsoft/learn-cli package for terminal use, and the hosted MCP endpoint works with any client that supports Streamable HTTP. Microsoft explicitly calls out clients such as Claude, Cursor, Copilot, and Codex. Because it is tied to first-party documentation and does not require separate credentials, this skill is especially useful when an agent needs high-trust answers about SDK methods, service limits, configuration steps, regional availability, or code samples from the official Microsoft ecosystem.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/microsoft-learn-mcp-server/)
