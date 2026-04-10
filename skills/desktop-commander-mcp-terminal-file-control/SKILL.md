---
title: "Desktop Commander MCP Server for Terminal and File Control"
description: "Desktop Commander is an MCP server that gives AI assistants terminal command execution, file system search, diff-based file editing, and process management capabilities. It extends Claude Desktop and other MCP clients with full local development environment control."
slug: "desktop-commander-mcp-terminal-file-control"
category:
  - "Developer Tools"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://github.com/wonderwhy-er/DesktopCommanderMCP"
tool_ecosystem:
  github_repo: "wonderwhy-er/DesktopCommanderMCP"
  github_stars: 5826
---

# Desktop Commander MCP Server for Terminal and File Control

Desktop Commander is an MCP server that gives AI assistants terminal command execution, file system search, diff-based file editing, and process management capabilities. It extends Claude Desktop and other MCP clients with full local development environment control.

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
clawhub install desktop-commander-mcp-terminal-file-control
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Desktop Commander MCP is an open-source Model Context Protocol server that transforms AI assistants into full development environment controllers. With over 5,700 GitHub stars and active development, it provides terminal command execution, file system operations, diff-based file editing, and process management through any MCP-compatible client — making it one of the most popular MCP servers in the ecosystem.
The server’s core capabilities span several categories. Terminal control enables executing long-running commands with output streaming, timeout management, and background execution support. Interactive process control lets agents work with SSH sessions, database shells, and development servers. File operations include search-and-replace editing using diff markers, reading and writing files, and directory navigation. The server also supports in-memory code execution for Python, Node.js, and R — running code snippets without saving files to disk.
Desktop Commander includes native support for common file formats beyond plain text. It can read, write, edit, and search Excel files (.xlsx, .xls, .xlsm) without external tools, extract text from PDFs and create new PDFs from markdown, and handle Word documents (.docx) with surgical XML editing. Session management for long-running commands includes process output pagination with offset/length controls to prevent context window overflow.
Installation is a single command: npx @wonderwhy-er/desktop-commander. The server is published on npm, licensed under MIT, and includes Remote MCP support for connecting from ChatGPT, Claude web, and other remote AI services via mcp.desktopcommander.app. A companion desktop application is available for macOS and Windows that provides a dedicated UI with visual file previews, custom MCP support, and multi-model compatibility including Claude, GPT-4.5, and Gemini 2.5.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/desktop-commander-mcp-terminal-file-control/)
