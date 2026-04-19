---
title: "bat Syntax-Highlighting Cat Replacement"
description: "bat is a command-line file viewer created by David Peter (sharkdp) and written in Rust. It reads files and prints their contents to the terminal with syntax highlighting, line numbers, Git change markers, and automatic paging. When piped to another command or redirected to a file, bat falls back to plain text output identical to cat, making it safe to use as an alias. Syntax highlighting covers over 200 programming and markup languages using the same Sublime Text syntax definitions that power the syntect library. Users can add custom .sublime-syntax files for unsupported formats. The &#8211;language (-l) flag forces a specific syntax when automatic detection fails. The &#8211;list-languages flag shows all supported syntaxes. Themes control the color scheme, with options matching popular editor themes like Monokai, Dracula, and GitHub. The &#8211;list-themes flag previews all available themes and custom ones can be added as .tmTheme files. Git integration is built in. A left-side gutter shows lines that have been added, modified, or removed relative to the git index. This works automatically in any git repository without additional configuration. The &#8211;diff flag shows only modified lines, similar to git diff but with full syntax highlighting of the surrounding context. bat automatically detects non-interactive terminals and disables paging and color when output goes to a pipe. The &#8211;paging flag controls this explicitly (always, never, auto). The -A/&#8211;show-all flag renders non-printable characters like tabs, newlines, and Unicode control characters as visible symbols, useful for debugging whitespace issues in configuration files. The tool integrates with fzf as a preview command (fzf &#8211;preview &#8220;bat &#8211;color=always {}&#8221;), with ripgrep through batgrep for highlighted search results, and with git diff through delta which uses bat&#8217;s syntax themes. bat is available via Homebrew, apt, pacman, Scoop, cargo, and GitHub releases for Linux, macOS, and Windows. It is licensed under MIT/Apache-2.0."
source: "https://github.com/sharkdp/bat"
verification: "security_reviewed"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "sharkdp/bat"
  github_stars: 57909
---

# bat Syntax-Highlighting Cat Replacement

bat is a command-line file viewer created by David Peter (sharkdp) and written in Rust. It reads files and prints their contents to the terminal with syntax highlighting, line numbers, Git change markers, and automatic paging. When piped to another command or redirected to a file, bat falls back to plain text output identical to cat, making it safe to use as an alias. Syntax highlighting covers over 200 programming and markup languages using the same Sublime Text syntax definitions that power the syntect library. Users can add custom .sublime-syntax files for unsupported formats. The &#8211;language (-l) flag forces a specific syntax when automatic detection fails. The &#8211;list-languages flag shows all supported syntaxes. Themes control the color scheme, with options matching popular editor themes like Monokai, Dracula, and GitHub. The &#8211;list-themes flag previews all available themes and custom ones can be added as .tmTheme files. Git integration is built in. A left-side gutter shows lines that have been added, modified, or removed relative to the git index. This works automatically in any git repository without additional configuration. The &#8211;diff flag shows only modified lines, similar to git diff but with full syntax highlighting of the surrounding context. bat automatically detects non-interactive terminals and disables paging and color when output goes to a pipe. The &#8211;paging flag controls this explicitly (always, never, auto). The -A/&#8211;show-all flag renders non-printable characters like tabs, newlines, and Unicode control characters as visible symbols, useful for debugging whitespace issues in configuration files. The tool integrates with fzf as a preview command (fzf &#8211;preview &#8220;bat &#8211;color=always {}&#8221;), with ripgrep through batgrep for highlighted search results, and with git diff through delta which uses bat&#8217;s syntax themes. bat is available via Homebrew, apt, pacman, Scoop, cargo, and GitHub releases for Linux, macOS, and Windows. It is licensed under MIT/Apache-2.0.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bat-syntax-highlighting-cat-replacement/)
