---
title: "Yeoman Generator Builder"
description: "Creates custom Yeoman generators using the yeoman-generator API and yo CLI. Scaffolds generator packages with prompting, writing, and install phases, supporting composability via this.composeWith() for multi-generator workflows."
verification: "security_reviewed"
source: "https://github.com/yeoman/generator"
category:
  - "Templates & Workflows"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "yeoman/generator"
  github_stars: 1262
  npm_package: "yeoman-generator"
  npm_weekly_downloads: 5021257
---

# Yeoman Generator Builder

The Yeoman Generator Builder skill helps create custom project scaffolding generators using the Yeoman ecosystem. It leverages the yeoman-generator base class to define generators with proper lifecycle phases: initializing, prompting, configuring, writing, conflicts, install, and end. The skill scaffolds generator npm packages with the required generator-* naming convention and proper directory structure. It creates sub-generators for modular scaffolding and configures the yeoman-environment for generator discovery and execution via the yo CLI. Prompting phases use Inquirer.js question objects with support for input, confirm, list, checkbox, and expand prompt types. The skill generates dynamic prompts that adapt based on previous answers using the when property and validates input with custom validation functions. Template writing uses this.fs.copyTpl() with EJS syntax for dynamic content generation. The skill handles file conflict resolution via the conflicter, manages destination paths with this.destinationPath(), and implements composability using this.composeWith() to chain multiple generators. It also integrates with yeoman-assert and yeoman-test for generator unit testing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/yeoman-generator-builder/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/yeoman-generator-builder
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/yeoman-generator-builder`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/yeoman-generator-builder/)
