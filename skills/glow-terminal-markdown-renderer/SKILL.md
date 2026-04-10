---
name: "Glow Terminal Markdown Renderer"
description: "Glow is a terminal-based markdown reader by Charm that renders markdown files with syntax highlighting, word wrapping, and styled formatting directly in the CLI. It includes a TUI for browsing local markdown files and discovering documentation."
verification: security_reviewed
source: "https://github.com/charmbracelet/glow"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "charmbracelet/glow"
  github_stars: 24096
---

# Glow Terminal Markdown Renderer

Glow is a terminal markdown reader built by Charmbracelet, the team behind Bubble Tea, Lip Gloss, and other Go-based terminal UI libraries. It renders markdown files with full styling — headings, bold, italic, code blocks with syntax highlighting, tables, links, and lists — directly in the terminal. The goal is to make reading documentation and README files as pleasant in the terminal as it is in a web browser.
The simplest usage is glow README.md, which renders the file with styled output and a pager for scrolling. Glow auto-detects terminal width and wraps text accordingly. It supports multiple style themes including dark, light, and auto-detection based on terminal background. Developers can also create custom styles using a JSON configuration file that controls colors, margins, and formatting for every markdown element.
The TUI mode, activated by running glow without arguments, provides a file browser that discovers markdown files in the current directory and subdirectories. It also detects Git repositories and shows their documentation. Users can navigate between files, search content, and read documentation without leaving the terminal. This is useful for browsing project documentation, changelogs, and internal wikis from the command line.
Glow can read from stdin (cat doc.md | glow), local files, and URLs (glow https://raw.githubusercontent.com/...). It supports line numbers, mouse wheel scrolling in TUI mode, and can be configured via a YAML config file at ~/.config/glow/glow.yml. The --pager flag enables the built-in pager for long documents.
With nearly 24,000 GitHub stars and an MIT license, Glow is one of the most popular CLI tools from the Charmbracelet ecosystem. It is available via Homebrew, apt, pacman, snap, Chocolatey, Scoop, Winget, and standalone binaries for Linux, macOS, Windows, FreeBSD, and Android (Termux).

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/glow-terminal-markdown-renderer/)
