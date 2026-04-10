---
title: "fx Terminal JSON Viewer and Processor"
description: "fx is a terminal-based JSON viewer and processor that provides an interactive TUI for navigating, filtering, and transforming JSON, YAML, and TOML data. Built in Go with support for JavaScript/Python expressions, it replaces piping through jq for quick data exploration."
slug: "fx-terminal-json-viewer-processor"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/antonmedv/fx"
tool_ecosystem:
  github_repo: "antonmedv/fx"
  github_stars: 20376
  npm_package: "fx"
  npm_weekly_downloads: 190694
---

# fx Terminal JSON Viewer and Processor

fx is a terminal-based JSON viewer and processor that provides an interactive TUI for navigating, filtering, and transforming JSON, YAML, and TOML data. Built in Go with support for JavaScript/Python expressions, it replaces piping through jq for quick data exploration.

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
clawhub install fx-terminal-json-viewer-processor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

fx is a terminal JSON viewer and processor created by Anton Medvedev. Written in Go, it provides both a rich text-based user interface (TUI) for interactively browsing structured data and a command-line processing mode for scripted transformations. It supports JSON, YAML, and TOML formats out of the box.
The interactive TUI mode lets developers navigate deeply nested JSON structures with keyboard shortcuts, expand and collapse nodes, search within the document, and copy paths or values. This makes it particularly valuable when exploring unfamiliar API responses or debugging configuration files where the structure is complex or undocumented. The interface renders syntax highlighting and handles very large files efficiently.
In processing mode, fx accepts JavaScript or Python expressions as arguments, enabling quick transformations without writing separate scripts. Developers can pipe data through fx with expressions like fx .users[0].name to extract specific values, or chain multiple transformations. This makes it a lightweight alternative to jq for teams that prefer JavaScript-style syntax over jq filter language.
fx integrates into standard Unix pipelines: curl https://api.example.com | fx opens the response in the interactive viewer, while curl https://api.example.com | fx .data.items extracts and outputs a specific field. It is available via Homebrew, npm, snap, and standalone binaries for Linux, macOS, and Windows.
With over 20,000 GitHub stars and an MIT license, fx is one of the most popular terminal JSON tools in the ecosystem. Key integration points include shell aliases, editor terminal panels, CI/CD log inspection, and API development workflows where rapid data exploration reduces iteration time.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/fx-terminal-json-viewer-processor/)
