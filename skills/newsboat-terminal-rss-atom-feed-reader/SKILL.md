---
name: "Newsboat Terminal RSS and Atom Feed Reader"
slug: "newsboat-terminal-rss-atom-feed-reader"
description: "Newsboat is an actively maintained RSS/Atom feed reader for the text console. A fork of the discontinued Newsbeuter, it provides a fast, keyboard-driven interface for subscribing to, reading, and managing feeds with powerful filtering, macro support, and scriptable automation."
github_stars: 3750
verification: "security_reviewed"
source: "https://github.com/newsboat/newsboat"
category: "Data Extraction & Transformation"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "newsboat/newsboat"
  github_stars: 3750
---

# Newsboat Terminal RSS and Atom Feed Reader

Newsboat is an actively maintained RSS/Atom feed reader for the text console. A fork of the discontinued Newsbeuter, it provides a fast, keyboard-driven interface for subscribing to, reading, and managing feeds with powerful filtering, macro support, and scriptable automation.

## Installation

Use the upstream install or setup path that matches your environment:
- $ git clone https://github.com/newsboat/newsboat.git
- $ make # pass -jN to use N CPU cores, e.g. -j8

Requirements and caveats from upstream:
- Newsboat depends on a number of libraries, which need to be installed before
- [build from source with Docker](doc/docker.md). Note that the resulting binary
- might not run outside of that same Docker container if your system doesn't

Basic usage or getting-started notes:
- ------------
- <!--
- UPDATE doc/newsboat.asciidoc IF YOU CHANGE THIS LIST

- Source: https://github.com/newsboat/newsboat
- Extracted from upstream docs: https://raw.githubusercontent.com/newsboat/newsboat/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/newsboat-terminal-rss-atom-feed-reader/)
