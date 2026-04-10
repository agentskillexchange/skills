---
name: Newsboat Terminal RSS and Atom Feed Reader
description: Newsboat is an actively maintained RSS/Atom feed reader for the text
  console. A fork of the discontinued Newsbeuter, it provides a fast, keyboard-driven
  interface for subscribing to, reading, and managing feeds with powerful filtering,
  macro support, and scriptable automation.
verification: security_reviewed
source: https://github.com/newsboat/newsboat
category:
- Data Extraction &amp; Transformation
framework:
- Custom Agents
tool_ecosystem:
  github_repo: newsboat/newsboat
  github_stars: 3750
  license: MIT
---
# Newsboat Terminal RSS and Atom Feed Reader

Newsboat is an open-source RSS and Atom feed reader designed for text terminals, written in C++ and Rust. It is the actively maintained successor to Newsbeuter and provides a fast, efficient way to consume web feeds entirely from the command line.
Core Features
Newsboat supports RSS 0.9x, RSS 1.0, RSS 2.0, Atom, JSON Feed, and OPML import/export. It handles multiple feed URLs defined in a simple text file, automatic feed refreshing at configurable intervals, article caching in an SQLite database, and configurable keybindings. Articles can be opened in an external browser, and the built-in search function filters across all feeds.
Filtering and Organization
A powerful query language allows creating virtual feeds based on article attributes like title, author, date, content, and feed source. Articles can be flagged, tagged, and organized into folders. Kill filters automatically hide articles matching specified criteria, reducing noise in high-volume feeds. Conditional formatting changes how articles are displayed based on their attributes.
Automation and Scripting
Newsboat supports macros that chain multiple commands into single keystrokes. The bookmark command pipes article URLs to external scripts for integration with read-later services, note-taking tools, or archival systems. The exec-url feature allows defining feeds whose content comes from the output of external commands rather than URLs, enabling custom data sources.
Agent Integration
AI agents can configure Newsboat through its text-based configuration files (urls and config), adding and removing feed subscriptions programmatically. The SQLite cache database can be queried directly for article metadata and content. The exec-url feature allows agents to inject custom feed sources. Newsboat can also export its database and OPML for further processing by downstream tools.
Installation
Newsboat is packaged for Debian, Ubuntu, Fedora, Arch, openSUSE, FreeBSD, and macOS (via Homebrew). The latest release is version 2.43, released March 22, 2026. Source tarballs with GPG signatures are available from newsboat.org.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/newsboat-terminal-rss-atom-feed-reader/)
