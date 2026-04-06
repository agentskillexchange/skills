---
name: "lsd Next-Generation ls Directory Listing Tool"
description: "lsd (LSDeluxe) is a modern rewrite of the classic ls command written in Rust, adding color coding, file-type icons via Nerd Fonts, tree view, and extensive formatting options while maintaining familiar ls command syntax."
category: "Developer Tools"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/lsd-rs/lsd"
tool_ecosystem:
  github_repo: "https://github.com/lsd-rs/lsd"
  github_stars: 15622
---
# lsd Next-Generation ls Directory Listing Tool

lsd (LSDeluxe) is a modern rewrite of the classic ls command written in Rust, adding color coding, file-type icons via Nerd Fonts, tree view, and extensive formatting options while maintaining familiar ls command syntax.

lsd (LSDeluxe) is a feature-rich replacement for the traditional Unix ls command, rewritten from scratch in Rust. It produces colorful, icon-enhanced directory listings that make it immediately obvious what types of files exist in a directory. File types are indicated by both color and Nerd Font icons, so source code files, images, archives, and executables are visually distinguishable at a glance.

The tool supports all the standard ls flags that developers rely on, including -l for long format, -a for showing hidden files, and -R for recursive listing. It adds a built-in tree view mode activated with --tree that renders directory hierarchies with connecting lines, similar to the standalone tree command but with all of lsd’s visual enhancements. Columns in long format are aligned and colored for readability, with file sizes displayed in human-readable units by default.

Customization is handled through YAML configuration files for colors, icons, and general behavior. Users can define custom color schemes to match their terminal theme, map specific file extensions to custom icons, and control layout details like date formats and size units. The configuration system supports per-directory overrides, which is useful for teams that want consistent listing styles within a project.

lsd is available through package managers on every major platform — pacman on Arch, dnf on Fedora, brew on macOS, apt on Debian/Ubuntu, and scoop or winget on Windows. It is also installable through cargo and available as precompiled binaries from GitHub releases. Most users set up a shell alias like alias ls='lsd' to use it as a transparent ls replacement. The project is licensed under Apache 2.0 and has an active contributor community maintaining support for new file types, icon sets, and platform-specific features.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill lsd-next-gen-ls-directory-listing
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill lsd-next-gen-ls-directory-listing -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill lsd-next-gen-ls-directory-listing -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill lsd-next-gen-ls-directory-listing -a codex
```

### OpenClaw

```bash
clawhub install lsd-next-gen-ls-directory-listing
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lsd-next-gen-ls-directory-listing/)
