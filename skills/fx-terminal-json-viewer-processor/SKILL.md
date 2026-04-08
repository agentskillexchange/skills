---
title: fx Terminal JSON Viewer and Processor
description: 'fx is a terminal JSON viewer and processor created by Anton Medvedev.
  Written in Go, it provides both a rich text-based user interface (TUI) for interactively
  browsing structured data and a command-line processing mode for scripted transformations.
  It supports JSON, YAML, and TOML formats out of the box. The interactive TUI mode
  lets developers navigate deeply nested JSON structures with keyboard shortcuts,
  expand and collapse nodes, search within the document, and copy paths or values.
  This makes it particularly valuable when exploring unfamiliar API responses or debugging
  configuration files where the structure is complex or undocumented. The interface
  renders syntax highlighting and handles very large files efficiently. In processing
  mode, fx accepts JavaScript or Python expressions as arguments, enabling quick transformations
  without writing separate scripts. Developers can pipe data through fx with expressions
  like fx .users[0].name to extract specific values, or chain multiple transformations.
  This makes it a lightweight alternative to jq for teams that prefer JavaScript-style
  syntax over jq filter language. fx integrates into standard Unix pipelines: curl
  https://api.example.com | fx opens the response in the interactive viewer, while
  curl https://api.example.com | fx .data.items extracts and outputs a specific field.
  It is available via Homebrew, npm, snap, and standalone binaries for Linux, macOS,
  and Windows. With over 20,000 GitHub stars and an MIT license, fx is one of the
  most popular terminal JSON tools in the ecosystem. Key integration points include
  shell aliases, editor terminal panels, CI/CD log inspection, and API development
  workflows where rapid data exploration reduces iteration time.'
verification: security_reviewed
source: https://github.com/antonmedv/fx
category:
- Data Extraction &amp; Transformation
framework:
- Custom Agents
tool_ecosystem:
  github_repo: antonmedv/fx
  github_stars: 20376
  npm_package: fx
  npm_weekly_downloads: 199995
---

# fx Terminal JSON Viewer and Processor

fx is a terminal JSON viewer and processor created by Anton Medvedev. Written in Go, it provides both a rich text-based user interface (TUI) for interactively browsing structured data and a command-line processing mode for scripted transformations. It supports JSON, YAML, and TOML formats out of the box. The interactive TUI mode lets developers navigate deeply nested JSON structures with keyboard shortcuts, expand and collapse nodes, search within the document, and copy paths or values. This makes it particularly valuable when exploring unfamiliar API responses or debugging configuration files where the structure is complex or undocumented. The interface renders syntax highlighting and handles very large files efficiently. In processing mode, fx accepts JavaScript or Python expressions as arguments, enabling quick transformations without writing separate scripts. Developers can pipe data through fx with expressions like fx .users[0].name to extract specific values, or chain multiple transformations. This makes it a lightweight alternative to jq for teams that prefer JavaScript-style syntax over jq filter language. fx integrates into standard Unix pipelines: curl https://api.example.com | fx opens the response in the interactive viewer, while curl https://api.example.com | fx .data.items extracts and outputs a specific field. It is available via Homebrew, npm, snap, and standalone binaries for Linux, macOS, and Windows. With over 20,000 GitHub stars and an MIT license, fx is one of the most popular terminal JSON tools in the ecosystem. Key integration points include shell aliases, editor terminal panels, CI/CD log inspection, and API development workflows where rapid data exploration reduces iteration time.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/fx-terminal-json-viewer-processor/)
