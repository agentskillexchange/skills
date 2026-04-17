---
title: "Freeze Code and Terminal Screenshot Generator"
description: "Freeze is a command-line tool from Charmbracelet that generates publication-quality images of source code and terminal output. It takes a file path or piped input and produces a PNG or SVG image with syntax highlighting, window chrome, configurable shadows, and padding. The output is suitable for documentation, blog posts, presentations, and social media without needing to open a graphical editor or take manual screenshots.\nThe tool supports syntax highlighting for over 200 programming languages through the Chroma library, with multiple built-in themes including Dracula, Monokai, Nord, and GitHub styles. Users can control the visual appearance through command-line flags — freeze main.go --theme dracula --shadow.blur 20 produces a Dracula-themed code image with a soft drop shadow. Font family, font size, line height, and padding are all configurable, giving fine-grained control over the final image dimensions and appearance.\nBeyond static code files, Freeze can capture terminal output by integrating with tmux. Running tmux capture-pane piped into Freeze generates screenshots of terminal user interfaces, which is particularly useful for documenting CLI tools, monitoring dashboards, or recording the output of interactive programs. The tool also supports reading from STDIN, so the output of any command can be piped directly into Freeze for immediate image generation.\nFreeze is written in Go and distributed as a single binary with no dependencies. It is installable through Homebrew, Nix, AUR, and Go install, with prebuilt binaries available on GitHub releases for macOS, Linux, and Windows. Configuration can be saved to reusable JSON config files, enabling consistent styling across an entire documentation project. The tool is MIT licensed and actively maintained as part of the Charmbracelet ecosystem alongside tools like Glow, Gum, VHS, and Bubbletea."
verification: security_reviewed
source: "https://github.com/charmbracelet/freeze"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "charmbracelet/freeze"
  github_stars: 4409
---

# Freeze Code and Terminal Screenshot Generator

Freeze is a command-line tool from Charmbracelet that generates publication-quality images of source code and terminal output. It takes a file path or piped input and produces a PNG or SVG image with syntax highlighting, window chrome, configurable shadows, and padding. The output is suitable for documentation, blog posts, presentations, and social media without needing to open a graphical editor or take manual screenshots.
The tool supports syntax highlighting for over 200 programming languages through the Chroma library, with multiple built-in themes including Dracula, Monokai, Nord, and GitHub styles. Users can control the visual appearance through command-line flags — freeze main.go --theme dracula --shadow.blur 20 produces a Dracula-themed code image with a soft drop shadow. Font family, font size, line height, and padding are all configurable, giving fine-grained control over the final image dimensions and appearance.
Beyond static code files, Freeze can capture terminal output by integrating with tmux. Running tmux capture-pane piped into Freeze generates screenshots of terminal user interfaces, which is particularly useful for documenting CLI tools, monitoring dashboards, or recording the output of interactive programs. The tool also supports reading from STDIN, so the output of any command can be piped directly into Freeze for immediate image generation.
Freeze is written in Go and distributed as a single binary with no dependencies. It is installable through Homebrew, Nix, AUR, and Go install, with prebuilt binaries available on GitHub releases for macOS, Linux, and Windows. Configuration can be saved to reusable JSON config files, enabling consistent styling across an entire documentation project. The tool is MIT licensed and actively maintained as part of the Charmbracelet ecosystem alongside tools like Glow, Gum, VHS, and Bubbletea.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/freeze-code-terminal-screenshot-generator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/freeze-code-terminal-screenshot-generator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/freeze-code-terminal-screenshot-generator/)
