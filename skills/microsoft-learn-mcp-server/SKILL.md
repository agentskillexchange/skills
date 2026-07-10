---
name: "Microsoft Learn MCP Server"
slug: "microsoft-learn-mcp-server"
description: "Microsoft Learn MCP Server gives agents and IDE assistants direct access to official Microsoft documentation and code samples through a hosted MCP endpoint. It is built to reduce hallucinations around Azure, .NET, Microsoft 365, and other Microsoft platforms by grounding answers in first-party docs."
github_stars: 1536
verification: "security_reviewed"
source: "https://github.com/MicrosoftDocs/mcp"
category: "Library & API Reference"
framework: "MCP"
tool_ecosystem:
  github_repo: "MicrosoftDocs/mcp"
  github_stars: 1536
---

# Microsoft Learn MCP Server

Microsoft Learn MCP Server gives agents and IDE assistants direct access to official Microsoft documentation and code samples through a hosted MCP endpoint. It is built to reduce hallucinations around Azure, .NET, Microsoft 365, and other Microsoft platforms by grounding answers in first-party docs.

## Installation

Use the upstream install or setup path that matches your environment:
- npx @microsoft/learn-cli search "azure functions timeout"
- npm install -g @microsoft/learn-cli

Requirements and caveats from upstream:
- "Show me runnable Python code to do harms eval using the Azure AI Foundry evaluation SDK."
- For applications that require OpenAI Deep Research model compatibility, you can use the OpenAI-compatible endpoint:
- If your use case requires a direct, programmatic integration, it is essential to understand that MCP is a **dynamic protocol, not a static API**. The available tools and their schemas will evolve.

Basic usage or getting-started notes:
- ### ✨ Example Prompts
- **Note:** This URL is intended for use **within a compliant MCP client** via Streamable HTTP, such as the recommended clients listed in our [Getting Started](#-installation--getting-started) section. It does not suppo...
- The Microsoft Learn MCP Server offers experimental features that are under active development. These features may change or be refined based on user feedback and usage patterns.

- Source: https://github.com/MicrosoftDocs/mcp
- Extracted from upstream docs: https://raw.githubusercontent.com/MicrosoftDocs/mcp/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/microsoft-learn-mcp-server/)
