---
name: "GitHub MCP Server for AI-Powered Repository Management"
slug: "github-mcp-server-ai-repository-management"
description: "GitHub's official Model Context Protocol (MCP) server that connects AI agents, assistants, and chatbots directly to GitHub's platform. Enables natural language repository management, code search, issue triage, PR automation, and CI/CD workflow intelligence through a standardized protocol."
github_stars: 28462
verification: "security_reviewed"
source: "https://github.com/github/github-mcp-server"
category: "Developer Tools"
framework: "MCP"
tool_ecosystem:
  github_repo: "github/github-mcp-server"
  github_stars: 28462
---

# GitHub MCP Server for AI-Powered Repository Management

GitHub's official Model Context Protocol (MCP) server that connects AI agents, assistants, and chatbots directly to GitHub's platform. Enables natural language repository management, code search, issue triage, PR automation, and CI/CD workflow intelligence through a standardized protocol.

## Installation

Use the upstream install or setup path that matches your environment:
- [![Install with Docker in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&inpu...
- Example (color output requires a TTY; use docker run -t (or -it) when running in Docker):
- docker run -it --rm ghcr.io/github/github-mcp-server tool-search "issue" --max-results 5
- docker run -i --rm \

Requirements and caveats from upstream:
- To run the server in a container, you will need to have [Docker](https://www.docker.com/) installed.
- Once Docker is installed, you will also need to ensure Docker is running. The Docker image is available at ghcr.io/github/github-mcp-server. The image is public; if you get errors on pull, you may have an expired toke...
- **Note**: Environment variable support varies by host app and IDE. Some applications (like Windsurf) require hardcoded tokens in config files.

Basic usage or getting-started notes:
- Lastly you will need to [Create a GitHub Personal Access Token](https://github.com/settings/personal-access-tokens/new).
- The MCP server can use many of the GitHub APIs, so enable the permissions that you feel comfortable granting your AI tools (to learn more about access tokens, please check out the [documentation](https://docs.github.c...
- <details><summary><b>Handling PATs Securely</b></summary>

- Source: https://github.com/github/github-mcp-server
- Extracted from upstream docs: https://raw.githubusercontent.com/github/github-mcp-server/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-mcp-server-ai-repository-management/)
