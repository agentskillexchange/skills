---
title: "D2 Modern Diagram Scripting Language and CLI"
description: "D2 is a modern diagram scripting language that turns text into diagrams. It compiles declarative text files into SVG, PNG, and PDF outputs with automatic layout, multiple themes, and support for sequence diagrams, class diagrams, and network topologies."
verification: "security_reviewed"
source: "https://github.com/terrastruct/d2"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "terrastruct/d2"
  github_stars: 23316
  license: "MPL-2.0"
---

# D2 Modern Diagram Scripting Language and CLI

D2 is an open-source diagram scripting language created by Terrastruct that converts human-readable text into production-quality diagrams. Unlike visual drag-and-drop tools, D2 lets you define diagrams as code, making them versionable, diffable, and easy to maintain alongside your source code.

The D2 CLI reads .d2 files and produces SVG, PNG, or PDF output. It includes a built-in live-reload watcher mode that opens a browser preview and updates automatically as you edit. The language supports a wide range of diagram types including flowcharts, sequence diagrams, class diagrams, entity-relationship diagrams, and network topologies.

D2 features multiple layout engines including dagre (default), ELK, and TALA. It ships with over 100 built-in themes ranging from professional to playful, and supports custom fonts. The declarative syntax is designed to be readable without documentation — shapes, connections, labels, and styles are expressed in a natural text format.

As a Go library, D2 can also be embedded programmatically into applications. The project provides a playground at play.d2lang.com for experimenting with diagrams in the browser. D2 is used by notable open-source projects for their documentation diagrams.

Installation is straightforward via curl, Homebrew, or go install. The tool produces clean SVG output suitable for documentation sites, README files, architecture decision records, and technical presentations. With its text-to-diagram approach, D2 integrates naturally into CI/CD pipelines and documentation-as-code workflows.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/d2-diagram-scripting-language-cli/)
