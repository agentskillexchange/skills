---
name: nb CLI Note-Taking Bookmarking and Knowledge Base Application
description: nb is a command-line and local web note-taking, bookmarking, archiving,
  and knowledge base application. It stores everything as plain text with Git-backed
  versioning and syncing, supports wiki-style linking, encryption, tagging, search,
  and Pandoc-powered import/export — all in a single portable Bash script.
category: "Calendar, Email &amp; Productivity"
framework: Multi-Framework
verification: security_reviewed
source: "https://github.com/xwmx/nb"
tool_ecosystem:
  github_repo: "https://github.com/xwmx/nb"
  github_stars: 8088
  license: AGPL-3.0
---
# nb CLI Note-Taking Bookmarking and Knowledge Base Application

nb is a command-line and local web note-taking, bookmarking, archiving, and knowledge base application. It stores everything as plain text with Git-backed versioning and syncing, supports wiki-style linking, encryption, tagging, search, and Pandoc-powered import/export — all in a single portable Bash script.

nb is a comprehensive command-line note-taking and knowledge management application packed into a single portable Bash script. Created by xwmx, nb supports plain text formats including Markdown, Org, LaTeX, and AsciiDoc, and works with any text editor you prefer — Vim, Emacs, VS Code, or Sublime Text.

Core Features

Notes are organized into notebooks and folders with support for tagging, pinning, and wiki-style [[linking]] between entries. Every change is automatically tracked via Git, providing full revision history and multi-device syncing through any Git remote. Search works across all notebooks with full-text and regex support. Notes can be encrypted with password protection using industry-standard encryption.

Bookmarking and Archiving

nb doubles as a powerful bookmarking system. Web pages are downloaded, cleaned, and saved as structured Markdown documents with local full-text search over cached content. Broken links are automatically checked against the Internet Archive Wayback Machine. A built-in local web server provides distraction-free browsing of bookmarks in terminal or GUI browsers.

Integration and Export

Pandoc integration enables importing and exporting notes to dozens of document formats including PDF, DOCX, HTML, and EPUB. The todo and task system tracks actionable items across notebooks. Extensibility is provided through a plugin architecture that lets users add custom functionality.

Agent Skill Applications

nb is particularly well-suited as a persistent knowledge store for AI agents. Its CLI interface, Git versioning, structured plain-text storage, and full-text search make it an ideal backend for agent memory systems. Agents can create, search, link, and tag notes programmatically, while the Git sync ensures multi-agent or multi-machine consistency. The bookmarking feature lets agents archive and index web research for later retrieval.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill nb-cli-note-taking-bookmarking-knowledge-base
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill nb-cli-note-taking-bookmarking-knowledge-base -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill nb-cli-note-taking-bookmarking-knowledge-base -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill nb-cli-note-taking-bookmarking-knowledge-base -a codex
```

### OpenClaw

```bash
clawhub install nb-cli-note-taking-bookmarking-knowledge-base
```


## Source

- [GitHub](https://github.com/xwmx/nb)
