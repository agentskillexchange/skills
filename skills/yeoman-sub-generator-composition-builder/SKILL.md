---
title: "Yeoman Sub-Generator Composition Builder"
description: "Orchestrates Yeoman generator composition by chaining sub-generators via the Yeoman Environment API. Manages yo run loops, priority queues, and cross-generator dependency resolution."
verification: "security_reviewed"
source: "https://github.com/yeoman/yo"
category:
  - "Templates & Workflows"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "yeoman/yo"
  github_stars: 3953
  npm_package: "yo"
  npm_weekly_downloads: 402691
---

# Yeoman Sub-Generator Composition Builder

The Yeoman Sub-Generator Composition Builder automates complex project generation workflows by orchestrating multiple Yeoman sub-generators through the yeoman-environment API. It uses the composeWith() method to chain generators in dependency order, managing the Yeoman run loop priority queue to ensure initializing, prompting, configuring, writing, and install phases execute correctly across composed generators. The skill resolves generator dependencies from the npm registry, checking for locally installed generators via yo –generators and installing missing ones on demand. It handles cross-generator conflict resolution using the Yeoman conflicter with configurable merge strategies for shared files like package.json and tsconfig.json. The skill supports both local generators in the generators/ directory and published npm generator packages prefixed with generator-. It can replay stored answers from .yo-rc.json for reproducible scaffolding and manages the Yeoman storage API for persisting configuration across sub-generator boundaries.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/yeoman-sub-generator-composition-builder/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/yeoman-sub-generator-composition-builder
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/yeoman-sub-generator-composition-builder`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/yeoman-sub-generator-composition-builder/)
