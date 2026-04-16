---
title: "Helix Post-Modern Modal Text Editor with LSP and Tree-sitter"
description: "Helix is a post-modern terminal-based modal text editor written in Rust. It features built-in language server protocol (LSP) support, smart syntax highlighting and code editing via Tree-sitter, and a Kakoune-inspired editing model with multiple selections."
verification: "security_reviewed"
source: "https://github.com/helix-editor/helix"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "helix-editor/helix"
  github_stars: 43690
  license: "MPL-2.0"
---

# Helix Post-Modern Modal Text Editor with LSP and Tree-sitter

Helix is an open-source modal text editor that brings modern IDE features to the terminal without requiring plugins. Written in Rust, Helix combines the efficiency of modal editing with built-in language intelligence that works out of the box.


The editor’s design is heavily inspired by Kakoune’s selection-first editing model, where you first select text and then apply operations — the inverse of Vim’s verb-object approach. This makes editing operations visual and predictable. Multiple selections are a first-class feature, allowing you to edit many locations simultaneously.


Helix ships with built-in Language Server Protocol (LSP) support, providing autocompletion, go-to-definition, find references, rename refactoring, diagnostics, and code actions for dozens of languages without configuration. Tree-sitter integration powers incremental syntax highlighting, structural text objects, and intelligent code navigation.


The editor supports over 200 languages with syntax highlighting grammars and has LSP configurations for most popular languages. It includes a built-in file picker with fuzzy finding, a buffer and symbol picker, and an integrated terminal. Themes are built-in with over 30 options available.


Installation is available through most package managers including Homebrew, pacman, Chocolatey, and Nix. Pre-built binaries are provided for Linux, macOS, and Windows. The project has over 43,000 GitHub stars and releases regular updates with new features and language support. Helix is licensed under MPL-2.0.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/helix-post-modern-modal-text-editor-lsp-treesitter/)
