---
name: "Work with AFFiNE workspaces, documents, and databases from MCP-compatible agents"
slug: "work-with-affine-workspaces-documents-and-databases-from-mcp-compatible-agents"
description: "Use affine-mcp-server when an agent needs tool-callable access to AFFiNE workspaces, documents, databases, and comments inside an MCP workflow instead of sending a user back to the AFFiNE UI."
github_stars: 142
verification: "security_reviewed"
source: "https://github.com/DAWNCR0W/affine-mcp-server"
author: "DAWNCR0W"
publisher_type: "individual"
category: "Integrations & Connectors"
framework: "MCP"
tool_ecosystem:
  github_repo: "DAWNCR0W/affine-mcp-server"
  github_stars: 142
  npm_package: "affine-mcp-server"
  npm_weekly_downloads: 2148
---

# Work with AFFiNE workspaces, documents, and databases from MCP-compatible agents

Use affine-mcp-server when an agent needs tool-callable access to AFFiNE workspaces, documents, databases, and comments inside an MCP workflow instead of sending a user back to the AFFiNE UI.

## Prerequisites

Node.js, an MCP-compatible client, and access to an AFFiNE Cloud or self-hosted instance with an API token or saved credentials.

## Installation

Use the upstream install or setup path that matches your environment:
- npm i -g affine-mcp-server
- npx -y -p affine-mcp-server affine-mcp -- --version
- docker run -d \
- npm run build

Requirements and caveats from upstream:
- Includes Docker images, health probes, and end-to-end test coverage
- AFFiNE Cloud requires API-token-based access for MCP usage; programmatic email/password sign-in is blocked by Cloudflare
- | Run the server in Docker or another OCI runtime | [docs/getting-started.md#path-c-run-from-the-docker-image](docs/getting-started.md#path-c-run-from-the-docker-image) |

Basic usage or getting-started notes:
- [Quick Start](#quick-start)
- Run a local stdio MCP server for Claude Code, Codex CLI, Cursor, or Claude Desktop
- | Run the server remotely over HTTP or behind OAuth | [docs/configuration-and-deployment.md](docs/configuration-and-deployment.md) |

- Source: https://github.com/DAWNCR0W/affine-mcp-server
- Extracted from upstream docs: https://raw.githubusercontent.com/DAWNCR0W/affine-mcp-server/HEAD/README.md

## Documentation

- https://github.com/DAWNCR0W/affine-mcp-server/blob/main/docs/getting-started.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/work-with-affine-workspaces-documents-and-databases-from-mcp-compatible-agents/)
