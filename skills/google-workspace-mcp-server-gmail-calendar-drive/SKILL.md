---
title: "Google Workspace MCP Server for Gmail Calendar and Drive"
description: "The Google Workspace MCP Server provides comprehensive natural language control over Gmail, Google Calendar, Drive, Docs, Sheets, Slides, Forms, Tasks, Contacts, and Chat through any MCP-compatible AI assistant. It supports OAuth 2.1 multi-user authentication and includes a CLI for coding agents."
slug: "google-workspace-mcp-server-gmail-calendar-drive"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://github.com/taylorwilsdon/google_workspace_mcp"
tool_ecosystem:
  github_repo: "taylorwilsdon/google_workspace_mcp"
  github_stars: 1986
listed: true
---

# Google Workspace MCP Server for Gmail Calendar and Drive

The Google Workspace MCP Server provides comprehensive natural language control over Gmail, Google Calendar, Drive, Docs, Sheets, Slides, Forms, Tasks, Contacts, and Chat through any MCP-compatible AI assistant. It supports OAuth 2.1 multi-user authentication and includes a CLI for coding agents.

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
clawhub install google-workspace-mcp-server-gmail-calendar-drive
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Google Workspace MCP Server is the most feature-complete Model Context Protocol integration for Google’s productivity suite. With nearly 2,000 GitHub stars and active development, it provides full natural language control over Gmail, Google Calendar, Drive, Docs, Sheets, Slides, Forms, Tasks, Contacts, and Chat through any MCP-compatible client including Claude Desktop, Cursor, Claude Code, and Codex CLI.
The server provides deep coverage across all major Workspace services. Gmail management includes reading, sending, replying, forwarding, labeling, searching, and organizing email with full thread support. Calendar features cover event creation, editing, deletion, availability checking, and multi-calendar management. Drive operations support file upload, download, search, sharing, and folder management with Office format compatibility. Docs, Sheets, and Slides support creation, editing, formatting, and commenting. Additional services include Forms creation, Tasks management, Contacts lookup, and Google Chat integration.
A key architectural strength is the OAuth 2.1 authentication system with multi-user support and native stateless mode. The server uses Google Desktop OAuth clients, eliminating complex redirect URI configuration. For organizations, it can be hosted centrally with external auth server support, making it the only Workspace MCP server designed for team-wide deployment. One-click Claude installation is supported for individual users.
The project includes a full-featured CLI for use with terminal-based coding agents like Claude Code and Codex. Installation is via PyPI (pip install workspace-mcp) or Docker. It is MIT-licensed, actively maintained, and includes comprehensive documentation at workspacemcp.com. Built with FastMCP for performance, the server features service caching and streamlined development patterns suitable for production use.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/google-workspace-mcp-server-gmail-calendar-drive/)
