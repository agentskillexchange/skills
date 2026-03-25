---
name: "Gum Interactive Shell Script Toolkit"
description: "Gum by Charmbracelet is a tool for building glamorous shell scripts. It provides configurable terminal UI components (choose, confirm, input, filter, spin, table, format) that can be used directly from bash to create interactive, visually polished CLI experiences."
category: "Developer Tools"
framework: "Claude Code"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: true
source: "https://agentskillexchange.com/skills/gum-interactive-shell-script-toolkit/"
---
# Gum Interactive Shell Script Toolkit

Gum by Charmbracelet is a tool for building glamorous shell scripts. It provides configurable terminal UI components (choose, confirm, input, filter, spin, table, format) that can be used directly from bash to create interactive, visually polished CLI experiences.

Gum is a tool for building glamorous shell scripts, created by Charmbracelet. It provides a collection of highly configurable, ready-to-use terminal UI components that you can invoke directly from shell scripts. Instead of writing complex terminal UI code in Go or Python, you can use gum commands like choose, confirm, input, write, spin, table, filter, and format to create interactive, visually polished CLI experiences with just a few lines of bash.
The tool includes components for every common interactive shell pattern. gum choose presents a selection menu, gum confirm asks yes/no questions, gum input and gum write handle single-line and multi-line text input, gum spin shows a spinner while a command runs, gum table renders tabular data with selectable rows, gum filter provides fuzzy filtering of lists, and gum format renders styled markdown, code blocks, templates, and emoji in the terminal.
Every component is heavily customizable through command-line flags. You can control colors, borders, padding, margins, fonts, cursor styles, placeholder text, and more. Gum leverages Charmbracelet’s Bubbles TUI component library and Lip Gloss styling library under the hood, giving shell scripts access to the same rich terminal UI capabilities that Go applications enjoy.
Gum is particularly useful for building interactive git commit workflows (the README demonstrates a Conventional Commits helper), deployment scripts with confirmation steps, configuration wizards, and any shell automation that benefits from user interaction. Since each gum command prints its result to stdout, it integrates seamlessly into Unix pipelines and variable assignment.
Written in Go and distributed as a single static binary, Gum is available via Homebrew (brew install gum), Go install, apt, pacman, Nix, and prebuilt binaries for Linux, macOS, and Windows. With over 19,000 GitHub stars, it is one of the most popular terminal UI tools in the ecosystem. Licensed under MIT, the project has active maintenance with regular releases from the Charmbracelet team.

## Installation

### Any / Claude Code
```bash
npx skills add gum-interactive-shell-script-toolkit
```

### Cursor
```bash
npx skills add gum-interactive-shell-script-toolkit --cursor
```

### Codex
```bash
npx skills add gum-interactive-shell-script-toolkit --codex
```

### OpenClaw
```bash
clawhub install gum-interactive-shell-script-toolkit
```
