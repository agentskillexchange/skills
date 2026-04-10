---
title: "aerc Extensible Terminal Email Client with IMAP JMAP and Notmuch"
description: "aerc is a terminal-based email client written in Go with first-class support for IMAP, SMTP, JMAP, Maildir, and Notmuch. It features Vim-like keybindings, email threading, HTML rendering, built-in patch management, and deep UNIX integration through pipes and commands."
slug: "aerc-extensible-terminal-email-client"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://git.sr.ht/~rjarry/aerc"
---

# aerc Extensible Terminal Email Client with IMAP JMAP and Notmuch

aerc is a terminal-based email client written in Go with first-class support for IMAP, SMTP, JMAP, Maildir, and Notmuch. It features Vim-like keybindings, email threading, HTML rendering, built-in patch management, and deep UNIX integration through pipes and commands.

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
clawhub install aerc-extensible-terminal-email-client
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

aerc is an open-source terminal email client designed for efficiency and extensibility. Originally created by Drew DeVault and now maintained by Robin Jarry, aerc runs entirely in your terminal and supports multiple email protocols including IMAP, SMTP, JMAP, Maildir, and Notmuch.
How It Works
aerc provides a multi-account email interface in the terminal with Vim-like keybindings. It supports email threading, embedded terminal commands, HTML email rendering (via w3m), and a powerful filter system for processing messages. Its configuration is file-based, making it easy to version control and automate.
Key Features
Multi-Protocol Support: IMAP for remote mailboxes, SMTP for sending, JMAP for modern mail servers, Maildir for local storage, and Notmuch for fast full-text search across large mail archives. Switch between accounts seamlessly.
Vim-Like Interface: Familiar modal keybindings for navigation, message composition, and folder management. Fully customizable key mappings via configuration files.
Embedded Terminal: Run shell commands directly within aerc and pipe email content to external tools. This makes it trivial to integrate with scripts, linters, formatters, and other CLI tools.
Patch Management: First-class support for working with patches from mailing lists. Apply, review, and manage patch series directly from your inbox, making it ideal for kernel and open-source development workflows.
HTML Rendering: Render HTML emails in the terminal using w3m or other text browsers. Configurable filters let you control how different MIME types are displayed.
Template System: Customizable Go templates for composing replies, forwards, and new messages. Automate email formatting with variables for sender, date, quoted text, and more.
Installation
aerc is packaged in most major Linux distributions (Arch, Debian, Fedora, Alpine, openSUSE) and available on macOS via Homebrew. Building from source requires Go 1.23+ and scdoc.
Agent Integration
Agents can leverage aerc’s pipe system and Maildir/Notmuch backends to automate email triage, extract information from messages, compose templated replies, and manage mailing list subscriptions. Its text-based interface and scriptable configuration make it a natural fit for terminal-based agent workflows.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aerc-extensible-terminal-email-client/)
