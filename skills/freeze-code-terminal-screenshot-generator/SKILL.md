---
title: "Freeze Code and Terminal Screenshot Generator"
description: "Freeze by Charmbracelet generates polished PNG and SVG images of code snippets and terminal output. It supports syntax highlighting for over 200 languages, configurable themes, shadows, padding, and window chrome styling."
verification: security_reviewed
source: "https://github.com/charmbracelet/freeze"
category:
  - "Developer Tools"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/freeze-code-terminal-screenshot-generator/)
