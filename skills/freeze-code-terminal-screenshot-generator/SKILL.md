---
title: "Freeze Code and Terminal Screenshot Generator"
description: "Freeze by Charmbracelet generates polished PNG and SVG images of code snippets and terminal output. It supports syntax highlighting for over 200 languages, configurable themes, shadows, padding, and window chrome styling."
slug: "freeze-code-terminal-screenshot-generator"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/charmbracelet/freeze"
tool_ecosystem:
  github_repo: "charmbracelet/freeze"
  github_stars: 4409
---

# Freeze Code and Terminal Screenshot Generator

Freeze by Charmbracelet generates polished PNG and SVG images of code snippets and terminal output. It supports syntax highlighting for over 200 languages, configurable themes, shadows, padding, and window chrome styling.

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
clawhub install freeze-code-terminal-screenshot-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Freeze is a command-line tool from Charmbracelet that generates publication-quality images of source code and terminal output. It takes a file path or piped input and produces a PNG or SVG image with syntax highlighting, window chrome, configurable shadows, and padding. The output is suitable for documentation, blog posts, presentations, and social media without needing to open a graphical editor or take manual screenshots.
The tool supports syntax highlighting for over 200 programming languages through the Chroma library, with multiple built-in themes including Dracula, Monokai, Nord, and GitHub styles. Users can control the visual appearance through command-line flags — freeze main.go --theme dracula --shadow.blur 20 produces a Dracula-themed code image with a soft drop shadow. Font family, font size, line height, and padding are all configurable, giving fine-grained control over the final image dimensions and appearance.
Beyond static code files, Freeze can capture terminal output by integrating with tmux. Running tmux capture-pane piped into Freeze generates screenshots of terminal user interfaces, which is particularly useful for documenting CLI tools, monitoring dashboards, or recording the output of interactive programs. The tool also supports reading from STDIN, so the output of any command can be piped directly into Freeze for immediate image generation.
Freeze is written in Go and distributed as a single binary with no dependencies. It is installable through Homebrew, Nix, AUR, and Go install, with prebuilt binaries available on GitHub releases for macOS, Linux, and Windows. Configuration can be saved to reusable JSON config files, enabling consistent styling across an entire documentation project. The tool is MIT licensed and actively maintained as part of the Charmbracelet ecosystem alongside tools like Glow, Gum, VHS, and Bubbletea.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/freeze-code-terminal-screenshot-generator/)
