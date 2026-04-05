---
name: "Shiori Self-Hosted Bookmark Manager with CLI and Web Interface"
description: "Shiori is a simple, portable bookmark manager written in Go inspired by Pocket. It provides both a command-line interface and a clean web UI for adding, editing, searching, and organizing bookmarks with automatic offline archive generation and readable content extraction."
category: "Calendar, Email &amp; Productivity"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/go-shiori/shiori"
tool_ecosystem:
  github_repo: "go-shiori/shiori"
  github_stars: 11399
  license: "MIT"
---
# Shiori Self-Hosted Bookmark Manager with CLI and Web Interface

Shiori is a simple, portable bookmark manager written in Go inspired by Pocket. It provides both a command-line interface and a clean web UI for adding, editing, searching, and organizing bookmarks with automatic offline archive generation and readable content extraction.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill shiori-self-hosted-bookmark-manager-cli-web
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill shiori-self-hosted-bookmark-manager-cli-web -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill shiori-self-hosted-bookmark-manager-cli-web -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill shiori-self-hosted-bookmark-manager-cli-web -a codex
```

### OpenClaw

```bash
clawhub install shiori-self-hosted-bookmark-manager-cli-web
```

## Details

Shiori is an open-source bookmark manager written in Go, designed as a self-hosted alternative to Pocket. It ships as a single binary that can be used as either a command-line application or a web application with a clean, intuitive interface. The tool focuses on simplicity, portability, and offline access to saved content.

Bookmark Management
Shiori provides full bookmark CRUD operations: add, edit, delete, and search across your saved links. When you save a bookmark, Shiori automatically attempts to parse the readable content from the page and create an offline archive. This means you can access the content of saved pages even when the original site is down or changed. The tool supports both a reader mode (simplified content view) and a full archive mode (complete page snapshot).

Import and Export
Shiori supports importing bookmarks from Netscape Bookmark files, which is the standard export format used by all major browsers including Chrome, Firefox, Safari, and Edge. It also supports direct import from Pocket. Bookmarks can be exported back to Netscape format for migration to other tools or browser import.

Database Support
Shiori supports multiple database backends: SQLite3 for zero-configuration portable setups, PostgreSQL for production deployments, and MySQL/MariaDB for existing database infrastructure. The SQLite option makes it trivially easy to get started — just run the binary and it creates the database file automatically.

Web Extension and API
Shiori includes a browser web extension (beta) for Firefox and Chrome that allows saving bookmarks directly from the browser to your Shiori instance. The web interface provides a responsive, searchable library view of all saved bookmarks with tag-based organization. Shiori exposes an API that AI agents can use to programmatically manage bookmarks, search saved content, and access offline archives.

Installation
Shiori is distributed as a single binary for Linux, macOS, and Windows. Docker images are available on GitHub Container Registry. For development, build from source with Go. Run shiori server to start the web interface or use CLI commands like shiori add, shiori search, and shiori export for terminal-based management.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/shiori-self-hosted-bookmark-manager-cli-web/)
