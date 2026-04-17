---
title: "Yeoman Generator Builder"
description: "The Yeoman Generator Builder skill helps create custom project scaffolding generators using the Yeoman ecosystem. It leverages the yeoman-generator base class to define generators with proper lifecycle phases: initializing, prompting, configuring, writing, conflicts, install, and end.\nThe skill scaffolds generator npm packages with the required generator-* naming convention and proper directory structure. It creates sub-generators for modular scaffolding and configures the yeoman-environment for generator discovery and execution via the yo CLI.\nPrompting phases use Inquirer.js question objects with support for input, confirm, list, checkbox, and expand prompt types. The skill generates dynamic prompts that adapt based on previous answers using the when property and validates input with custom validation functions.\nTemplate writing uses this.fs.copyTpl() with EJS syntax for dynamic content generation. The skill handles file conflict resolution via the conflicter, manages destination paths with this.destinationPath(), and implements composability using this.composeWith() to chain multiple generators. It also integrates with yeoman-assert and yeoman-test for generator unit testing."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/yeoman-generator-builder/"
framework:
  - "OpenClaw"
---

# Yeoman Generator Builder

The Yeoman Generator Builder skill helps create custom project scaffolding generators using the Yeoman ecosystem. It leverages the yeoman-generator base class to define generators with proper lifecycle phases: initializing, prompting, configuring, writing, conflicts, install, and end.
The skill scaffolds generator npm packages with the required generator-* naming convention and proper directory structure. It creates sub-generators for modular scaffolding and configures the yeoman-environment for generator discovery and execution via the yo CLI.
Prompting phases use Inquirer.js question objects with support for input, confirm, list, checkbox, and expand prompt types. The skill generates dynamic prompts that adapt based on previous answers using the when property and validates input with custom validation functions.
Template writing uses this.fs.copyTpl() with EJS syntax for dynamic content generation. The skill handles file conflict resolution via the conflicter, manages destination paths with this.destinationPath(), and implements composability using this.composeWith() to chain multiple generators. It also integrates with yeoman-assert and yeoman-test for generator unit testing.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/yeoman-generator-builder
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/yeoman-generator-builder` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/yeoman-generator-builder/)
