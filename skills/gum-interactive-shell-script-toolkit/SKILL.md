---
title: "Gum Interactive Shell Script Toolkit"
description: "Gum by Charmbracelet is a tool for building glamorous shell scripts. It provides configurable terminal UI components (choose, confirm, input, filter, spin, table, format) that can be used directly from bash to create interactive, visually polished CLI experiences."
verification: security_reviewed
source: "https://github.com/charmbracelet/gum"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "charmbracelet/gum"
  github_stars: 23196
---

# Gum Interactive Shell Script Toolkit

Gum is a tool for building glamorous shell scripts, created by Charmbracelet. It provides a collection of highly configurable, ready-to-use terminal UI components that you can invoke directly from shell scripts. Instead of writing complex terminal UI code in Go or Python, you can use gum commands like choose, confirm, input, write, spin, table, filter, and format to create interactive, visually polished CLI experiences with just a few lines of bash.

The tool includes components for every common interactive shell pattern. gum choose presents a selection menu, gum confirm asks yes/no questions, gum input and gum write handle single-line and multi-line text input, gum spin shows a spinner while a command runs, gum table renders tabular data with selectable rows, gum filter provides fuzzy filtering of lists, and gum format renders styled markdown, code blocks, templates, and emoji in the terminal.

Every component is heavily customizable through command-line flags. You can control colors, borders, padding, margins, fonts, cursor styles, placeholder text, and more. Gum leverages Charmbracelet’s Bubbles TUI component library and Lip Gloss styling library under the hood, giving shell scripts access to the same rich terminal UI capabilities that Go applications enjoy.

Gum is particularly useful for building interactive git commit workflows (the README demonstrates a Conventional Commits helper), deployment scripts with confirmation steps, configuration wizards, and any shell automation that benefits from user interaction. Since each gum command prints its result to stdout, it integrates seamlessly into Unix pipelines and variable assignment.

Written in Go and distributed as a single static binary, Gum is available via Homebrew (brew install gum), Go install, apt, pacman, Nix, and prebuilt binaries for Linux, macOS, and Windows. With over 19,000 GitHub stars, it is one of the most popular terminal UI tools in the ecosystem. Licensed under MIT, the project has active maintenance with regular releases from the Charmbracelet team.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gum-interactive-shell-script-toolkit
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/gum-interactive-shell-script-toolkit` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gum-interactive-shell-script-toolkit/)
