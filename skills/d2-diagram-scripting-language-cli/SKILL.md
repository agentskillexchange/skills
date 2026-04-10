---
title: "D2 Modern Diagram Scripting Language and CLI"
description: "D2 is a modern diagram scripting language that turns text into diagrams. It compiles declarative text files into SVG, PNG, and PDF outputs with automatic layout, multiple themes, and support for sequence diagrams, class diagrams, and network topologies."
slug: "d2-diagram-scripting-language-cli"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/terrastruct/d2"
tool_ecosystem:
  github_repo: "terrastruct/d2"
  github_stars: 23316
listed: true
---

# D2 Modern Diagram Scripting Language and CLI

D2 is a modern diagram scripting language that turns text into diagrams. It compiles declarative text files into SVG, PNG, and PDF outputs with automatic layout, multiple themes, and support for sequence diagrams, class diagrams, and network topologies.

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
clawhub install d2-diagram-scripting-language-cli
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

D2 is an open-source diagram scripting language created by Terrastruct that converts human-readable text into production-quality diagrams. Unlike visual drag-and-drop tools, D2 lets you define diagrams as code, making them versionable, diffable, and easy to maintain alongside your source code.
The D2 CLI reads .d2 files and produces SVG, PNG, or PDF output. It includes a built-in live-reload watcher mode that opens a browser preview and updates automatically as you edit. The language supports a wide range of diagram types including flowcharts, sequence diagrams, class diagrams, entity-relationship diagrams, and network topologies.
D2 features multiple layout engines including dagre (default), ELK, and TALA. It ships with over 100 built-in themes ranging from professional to playful, and supports custom fonts. The declarative syntax is designed to be readable without documentation — shapes, connections, labels, and styles are expressed in a natural text format.
As a Go library, D2 can also be embedded programmatically into applications. The project provides a playground at play.d2lang.com for experimenting with diagrams in the browser. D2 is used by notable open-source projects for their documentation diagrams.
Installation is straightforward via curl, Homebrew, or go install. The tool produces clean SVG output suitable for documentation sites, README files, architecture decision records, and technical presentations. With its text-to-diagram approach, D2 integrates naturally into CI/CD pipelines and documentation-as-code workflows.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/d2-diagram-scripting-language-cli/)
