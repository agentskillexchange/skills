---
title: "Just Command Runner"
description: "Just is a command runner written in Rust that provides a convenient way to save and run project-specific commands. It uses a justfile syntax inspired by Make but focused on running commands rather than building targets, with support for parameters, dependencies, and multi-language recipes."
slug: "just-command-runner"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://github.com/casey/just"
tool_ecosystem:
  github_repo: "casey/just"
  github_stars: 32526
listed: true
---

# Just Command Runner

Just is a command runner written in Rust that provides a convenient way to save and run project-specific commands. It uses a justfile syntax inspired by Make but focused on running commands rather than building targets, with support for parameters, dependencies, and multi-language recipes.

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
clawhub install just-command-runner
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Just is a command runner written in Rust by Casey Rodarmor. It provides a convenient way to save and run project-specific commands using a justfile, similar to Make but focused purely on running commands rather than building targets. Just uses a syntax inspired by make but removes the quirks: no need for .PHONY targets, tab-vs-spaces issues, or dealing with build graph semantics when all you want is to run scripts.
A justfile contains recipes that define named commands with optional parameters, dependencies, and documentation. Recipes can be written in any language using shebangs, accept arguments with default values and type checking, and support conditional logic. Just automatically loads .env files, supports recipe listing with descriptions, and provides features like command echoing, error handling, and confirmation prompts.
Just stands out in the developer tools ecosystem for several reasons. It supports recipes in any language (bash, python, node, etc.) via shebang lines. It provides excellent error messages with source location information. It supports recipe parameters with default values, variadic arguments, and environment variable integration. The justfile format supports includes, imports, and modules for organizing complex command sets across projects.
The tool has become a standard part of many development workflows, replacing ad-hoc shell scripts and Makefiles that are used purely as command runners. It integrates well with CI/CD systems and developer onboarding: new team members can run just –list to see all available project commands with descriptions. Just is cross-platform, running on Linux, macOS, and Windows.
Installation is available via cargo install just, Homebrew, apt, pacman, conda, and prebuilt binaries. With over 24,000 GitHub stars, Just is one of the most popular developer productivity tools on GitHub. It is licensed under CC0 (public domain). The project has active maintenance with frequent releases, a comprehensive manual, and strong community support.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/just-command-runner/)
