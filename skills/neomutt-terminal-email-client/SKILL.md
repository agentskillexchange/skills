---
title: "NeoMutt Feature-Rich Terminal Email Client"
description: "NeoMutt is an actively maintained fork of the classic Mutt email client that brings modern features to terminal-based email management. It supports IMAP, POP3, SMTP, Maildir, notmuch search, and PGP encryption with a highly customizable ncurses interface."
slug: "neomutt-terminal-email-client"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/neomutt/neomutt"
tool_ecosystem:
  github_repo: "neomutt/neomutt"
  github_stars: 3685
listed: true
---

# NeoMutt Feature-Rich Terminal Email Client

NeoMutt is an actively maintained fork of the classic Mutt email client that brings modern features to terminal-based email management. It supports IMAP, POP3, SMTP, Maildir, notmuch search, and PGP encryption with a highly customizable ncurses interface.

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
clawhub install neomutt-terminal-email-client
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

NeoMutt is a command-line email client written in C that extends the classic Mutt mail user agent with dozens of community patches and new features. It provides a fast, keyboard-driven interface for reading, composing, and managing email directly from the terminal.
Protocol Support
NeoMutt handles IMAP, POP3, SMTP, Maildir, mstrstrstrbox, and STRSTRSTRNNTP (Usenet) protocols natively. It integrates with notmuch for full-text email search across large mailboxes and supports compressed folder storage for space efficiency. The client handles MIME types, attachments, and multipart messages with configurable mailcap rendering.
Security and Encryption
Built-in support for PGP/GPG and S/MIME allows signing, encrypting, and verifying messages. The encrypt-to-self feature ensures you can always decrypt your own sent messages. TLS/SSL connections with SNI negotiation provide secure transport for all protocols.
Customization and Productivity Features
NeoMutt includes a sidebar panel showing mailbox lists, conditional date formatting for smarter display, index coloring with custom rules, nested conditional format strings, and Vi-style keybindings. The progress bar shows visual feedback during slow operations. Custom mailbox tags work with both notmuch tags and IMAP keywords.
Agent Integration
AI agents can drive NeoMutt through its command-line interface and configuration system. Email triage, automated filtering, and batch operations are possible through NeoMutt macros and hooks. The global hooks feature allows defining actions that trigger on specific events like new mail arrival, and the account command feature enables populating credentials from external sources.
Installation
NeoMutt is packaged for most Linux distributions including Debian, Ubuntu, Fedora, Arch, and Alpine. It is also available via Homebrew on macOS. Building from source requires a C compiler and standard development libraries.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/neomutt-terminal-email-client/)
