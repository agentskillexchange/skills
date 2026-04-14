---
title: "bat Syntax-Highlighting Cat Replacement"
description: "bat is a cat(1) clone written in Rust that adds syntax highlighting for over 200 languages, Git integration showing file modifications, automatic paging, and line numbering. It serves as a drop-in replacement for cat with enhanced readability for code and configuration files."
verification: security_reviewed
source: "https://github.com/sharkdp/bat"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "sharkdp/bat"
  github_stars: 57909
---

# bat Syntax-Highlighting Cat Replacement

bat is a command-line file viewer created by David Peter (sharkdp) and written in Rust. It reads files and prints their contents to the terminal with syntax highlighting, line numbers, Git change markers, and automatic paging. When piped to another command or redirected to a file, bat falls back to plain text output identical to cat, making it safe to use as an alias.

Syntax highlighting covers over 200 programming and markup languages using the same Sublime Text syntax definitions that power the syntect library. Users can add custom .sublime-syntax files for unsupported formats. The –language (-l) flag forces a specific syntax when automatic detection fails. The –list-languages flag shows all supported syntaxes. Themes control the color scheme, with options matching popular editor themes like Monokai, Dracula, and GitHub. The –list-themes flag previews all available themes and custom ones can be added as .tmTheme files.

Git integration is built in. A left-side gutter shows lines that have been added, modified, or removed relative to the git index. This works automatically in any git repository without additional configuration. The –diff flag shows only modified lines, similar to git diff but with full syntax highlighting of the surrounding context.

bat automatically detects non-interactive terminals and disables paging and color when output goes to a pipe. The –paging flag controls this explicitly (always, never, auto). The -A/–show-all flag renders non-printable characters like tabs, newlines, and Unicode control characters as visible symbols, useful for debugging whitespace issues in configuration files.

The tool integrates with fzf as a preview command (fzf –preview “bat –color=always {}”), with ripgrep through batgrep for highlighted search results, and with git diff through delta which uses bat’s syntax themes. bat is available via Homebrew, apt, pacman, Scoop, cargo, and GitHub releases for Linux, macOS, and Windows. It is licensed under MIT/Apache-2.0.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bat-syntax-highlighting-cat-replacement/)
