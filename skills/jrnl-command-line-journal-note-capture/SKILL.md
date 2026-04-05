---
name: "jrnl Command-Line Journal and Note Capture Tool"
description: "jrnl is a command-line journal application that lets you capture thoughts and notes without leaving the terminal. It stores entries as human-readable plain text with optional AES encryption, supports natural-language timestamps, and integrates with external editors and cloud sync services."
category: "Calendar, Email & Productivity"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/jrnl-org/jrnl"
tool_ecosystem:
  tool: jrnl
  github_repo: jrnl-org/jrnl
  github_stars: 7195
  license: GPL-3.0
  maintained: true
---
# jrnl Command-Line Journal and Note Capture Tool

jrnl is a command-line journal application that lets you capture thoughts and notes without leaving the terminal. It stores entries as human-readable plain text with optional AES encryption, supports natural-language timestamps, and integrates with external editors and cloud sync services.

## Overview

jrnl is a lightweight command-line journal application designed for capturing thoughts, daily logs, and notes directly from the terminal. Built in Python and available on PyPI, jrnl uses a natural-language interface that parses timestamps and structures entries automatically. Typing `jrnl yesterday: Had a great meeting. Discussed the project roadmap.` creates a timestamped entry with title and body parsed from the sentence structure.

Key Capabilities

Journals are stored as human-readable plain text files, ensuring your data remains accessible and portable across decades. jrnl supports AES-256 encryption for sensitive journals, making it suitable for private diaries and confidential work notes. Multiple journals can be maintained simultaneously for different areas of life or work.

Integration Points

jrnl works with your preferred text editor (Vim, Emacs, VS Code, nano) for longer entries via the `--edit` flag. It supports filtering entries by date range, tags, and starred status. The `--format` option exports entries as JSON, Markdown, XML, or plain text for downstream processing. Journal files can be synced across devices using Dropbox, Syncthing, or any file-sync tool.

Agent Skill Applications

AI agents can use jrnl to maintain structured logs of decisions, conversations, and task progress. The CLI interface and JSON export make it straightforward to integrate into automated workflows. Agents can query past entries by date or tag to retrieve context, and the encryption feature protects sensitive information in shared environments. Combined with shell scripting, jrnl becomes a persistent memory layer for agent systems.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill jrnl-command-line-journal-note-capture
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill jrnl-command-line-journal-note-capture -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill jrnl-command-line-journal-note-capture -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill jrnl-command-line-journal-note-capture -a codex
```

### OpenClaw

```bash
clawhub install jrnl-command-line-journal-note-capture
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jrnl-command-line-journal-note-capture/)
