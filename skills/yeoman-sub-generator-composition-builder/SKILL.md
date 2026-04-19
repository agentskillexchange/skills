---
title: "Yeoman Sub-Generator Composition Builder"
description: "The Yeoman Sub-Generator Composition Builder automates complex project generation workflows by orchestrating multiple Yeoman sub-generators through the yeoman-environment API. It uses the composeWith() method to chain generators in dependency order, managing the Yeoman run loop priority queue to ensure initializing, prompting, configuring, writing, and install phases execute correctly across composed generators. The skill resolves generator dependencies from the npm registry, checking for locally installed generators via yo &#8211;generators and installing missing ones on demand. It handles cross-generator conflict resolution using the Yeoman conflicter with configurable merge strategies for shared files like package.json and tsconfig.json. The skill supports both local generators in the generators/ directory and published npm generator packages prefixed with generator-. It can replay stored answers from .yo-rc.json for reproducible scaffolding and manages the Yeoman storage API for persisting configuration across sub-generator boundaries."
source: "https://github.com/yeoman/yo"
verification: "security_reviewed"
category:
  - "Templates &amp; Workflows"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "yeoman/yo"
  github_stars: 3953
  npm_package: "yo"
  npm_weekly_downloads: 402691
---

# Yeoman Sub-Generator Composition Builder

The Yeoman Sub-Generator Composition Builder automates complex project generation workflows by orchestrating multiple Yeoman sub-generators through the yeoman-environment API. It uses the composeWith() method to chain generators in dependency order, managing the Yeoman run loop priority queue to ensure initializing, prompting, configuring, writing, and install phases execute correctly across composed generators. The skill resolves generator dependencies from the npm registry, checking for locally installed generators via yo &#8211;generators and installing missing ones on demand. It handles cross-generator conflict resolution using the Yeoman conflicter with configurable merge strategies for shared files like package.json and tsconfig.json. The skill supports both local generators in the generators/ directory and published npm generator packages prefixed with generator-. It can replay stored answers from .yo-rc.json for reproducible scaffolding and manages the Yeoman storage API for persisting configuration across sub-generator boundaries.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/yeoman-sub-generator-composition-builder/)
