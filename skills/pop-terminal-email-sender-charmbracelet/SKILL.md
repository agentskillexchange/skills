---
title: "Pop Terminal Email Sender and TUI by Charmbracelet"
description: "Pop is a terminal-based email sending tool by Charmbracelet with both a TUI composer and CLI mode. It supports Resend API and SMTP backends, file attachments, Markdown body rendering, and integrates with other Charm tools."
slug: "pop-terminal-email-sender-charmbracelet"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/charmbracelet/pop"
tool_ecosystem:
  github_repo: "charmbracelet/pop"
  github_stars: 2809
listed: true
---

# Pop Terminal Email Sender and TUI by Charmbracelet

Pop is a terminal-based email sending tool by Charmbracelet with both a TUI composer and CLI mode. It supports Resend API and SMTP backends, file attachments, Markdown body rendering, and integrates with other Charm tools.

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
clawhub install pop-terminal-email-sender-charmbracelet
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Overview
Pop is a command-line email sending tool built by Charmbracelet, the team behind Bubble Tea, Gum, Glow, and other popular terminal tools. Pop provides two modes: a beautiful TUI (terminal user interface) for composing emails interactively, and a CLI mode for sending emails from scripts and automation pipelines. It supports both the Resend API and traditional SMTP as delivery backends.
Key Features
Pop supports Markdown email bodies that render beautifully in recipients’ inboxes. It handles file attachments via the --attach flag, supports piping content from stdin for the email body, and can set From/To/Subject/CC/BCC fields via flags or interactively in the TUI. The --preview flag lets you review emails before sending. Email signatures can be configured via the POP_SIGNATURE environment variable.
How It Works
For quick sends: pop --from me@example.com --to you@example.com --subject "Hello" --body "Message here". For the interactive TUI, just run pop. To pipe content: cat message.md | pop --to recipient@example.com. Pop supports two backends: set RESEND_API_KEY for the Resend service, or configure POP_SMTP_HOST, POP_SMTP_PORT, POP_SMTP_USERNAME, and POP_SMTP_PASSWORD for SMTP delivery.
Tool Integrations
Pop integrates naturally with other Charmbracelet tools. Use mods to generate email content with AI: pop . Use gum for interactive recipient selection: pop --to $(gum filter . Use invoice to generate and email invoices entirely from the terminal. These composable pipelines make Pop a powerful building block for terminal-based workflows.
Installation
Install via Homebrew: brew install pop. Via Nix: nix-env -iA nixpkgs.pop. Via AUR: yay -S charm-pop-bin. Via Go: go install github.com/charmbracelet/pop@latest. Binary releases are available on GitHub for Linux, macOS, and Windows. The tool is written in Go and distributed as a single binary.
Agent Integration
Agents can use Pop to send emails directly from automated workflows without needing complex email library integrations. The CLI mode with piped input makes it trivial for agents to compose and send notifications, reports, or alerts. Combined with AI tools like mods for content generation, agents can create complete email workflows entirely from the command line with minimal configuration.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pop-terminal-email-sender-charmbracelet/)
