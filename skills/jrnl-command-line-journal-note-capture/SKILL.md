---
title: "jrnl Command-Line Journal and Note Capture Tool"
description: "jrnl is a command-line journal application that lets you capture thoughts and notes without leaving the terminal. It stores entries as human-readable plain text with optional AES encryption, supports natural-language timestamps, and integrates with external editors and cloud sync services."
slug: "jrnl-command-line-journal-note-capture"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/jrnl-org/jrnl"
tool_ecosystem:
  github_repo: "jrnl-org/jrnl"
  github_stars: 7195
---

# jrnl Command-Line Journal and Note Capture Tool

jrnl is a command-line journal application that lets you capture thoughts and notes without leaving the terminal. It stores entries as human-readable plain text with optional AES encryption, supports natural-language timestamps, and integrates with external editors and cloud sync services.

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
clawhub install jrnl-command-line-journal-note-capture
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

jrnl is a lightweight command-line journal application designed for capturing thoughts, daily logs, and notes directly from the terminal. Built in Python and available on PyPI, jrnl uses a natural-language interface that parses timestamps and structures entries automatically. Typing jrnl yesterday: Had a great meeting. Discussed the project roadmap. creates a timestamped entry with title and body parsed from the sentence structure.
Key Capabilities
Journals are stored as human-readable plain text files, ensuring your data remains accessible and portable across decades. jrnl supports AES-256 encryption for sensitive journals, making it suitable for private diaries and confidential work notes. Multiple journals can be maintained simultaneously for different areas of life or work.
Integration Points
jrnl works with your preferred text editor (Vim, Emacs, VS Code, nano) for longer entries via the --edit flag. It supports filtering entries by date range, tags, and starred status. The --format option exports entries as JSON, Markdown, XML, or plain text for downstream processing. Journal files can be synced across devices using Dropbox, Syncthing, or any file-sync tool.
Agent Skill Applications
AI agents can use jrnl to maintain structured logs of decisions, conversations, and task progress. The CLI interface and JSON export make it straightforward to integrate into automated workflows. Agents can query past entries by date or tag to retrieve context, and the encryption feature protects sensitive information in shared environments. Combined with shell scripting, jrnl becomes a persistent memory layer for agent systems.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jrnl-command-line-journal-note-capture/)
