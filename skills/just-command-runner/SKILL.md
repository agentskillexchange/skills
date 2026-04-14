---
title: "Just Command Runner"
description: "Just is a command runner written in Rust that provides a convenient way to save and run project-specific commands. It uses a justfile syntax inspired by Make but focused on running commands rather than building targets, with support for parameters, dependencies, and multi-language recipes."
verification: security_reviewed
source: "https://github.com/casey/just"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "casey/just"
  github_stars: 32526
---

# Just Command Runner

Just is a command runner written in Rust by Casey Rodarmor. It provides a convenient way to save and run project-specific commands using a justfile, similar to Make but focused purely on running commands rather than building targets. Just uses a syntax inspired by make but removes the quirks: no need for .PHONY targets, tab-vs-spaces issues, or dealing with build graph semantics when all you want is to run scripts.

A justfile contains recipes that define named commands with optional parameters, dependencies, and documentation. Recipes can be written in any language using shebangs, accept arguments with default values and type checking, and support conditional logic. Just automatically loads .env files, supports recipe listing with descriptions, and provides features like command echoing, error handling, and confirmation prompts.

Just stands out in the developer tools ecosystem for several reasons. It supports recipes in any language (bash, python, node, etc.) via shebang lines. It provides excellent error messages with source location information. It supports recipe parameters with default values, variadic arguments, and environment variable integration. The justfile format supports includes, imports, and modules for organizing complex command sets across projects.

The tool has become a standard part of many development workflows, replacing ad-hoc shell scripts and Makefiles that are used purely as command runners. It integrates well with CI/CD systems and developer onboarding: new team members can run just –list to see all available project commands with descriptions. Just is cross-platform, running on Linux, macOS, and Windows.

Installation is available via cargo install just, Homebrew, apt, pacman, conda, and prebuilt binaries. With over 24,000 GitHub stars, Just is one of the most popular developer productivity tools on GitHub. It is licensed under CC0 (public domain). The project has active maintenance with frequent releases, a comprehensive manual, and strong community support.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/just-command-runner/)
