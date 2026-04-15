---
title: "aerc Extensible Terminal Email Client with IMAP JMAP and Notmuch"
description: "aerc is a terminal-based email client written in Go with first-class support for IMAP, SMTP, JMAP, Maildir, and Notmuch. It features Vim-like keybindings, email threading, HTML rendering, built-in patch management, and deep UNIX integration through pipes and commands."
verification: security_reviewed
source: "https://git.sr.ht/~rjarry/aerc"
category:
  - "Calendar, Email & Productivity"
framework:
  - "Custom Agents"
---

# aerc Extensible Terminal Email Client with IMAP JMAP and Notmuch

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

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/aerc-extensible-terminal-email-client
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/aerc-extensible-terminal-email-client` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aerc-extensible-terminal-email-client/)
