---
name: "Yeoman Generator Builder"
description: "Creates custom Yeoman generators using the yeoman-generator API and yo CLI. Scaffolds generator packages with prompting, writing, and install phases, supporting composability via this.composeWith() for multi-generator workflows."
category: "Templates &amp; Workflows"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/yeoman-generator-builder/"
---
# Yeoman Generator Builder

Creates custom Yeoman generators using the yeoman-generator API and yo CLI. Scaffolds generator packages with prompting, writing, and install phases, supporting composability via this.composeWith() for multi-generator workflows.

The Yeoman Generator Builder skill helps create custom project scaffolding generators using the Yeoman ecosystem. It leverages the yeoman-generator base class to define generators with proper lifecycle phases: initializing, prompting, configuring, writing, conflicts, install, and end.

The skill scaffolds generator npm packages with the required generator-* naming convention and proper directory structure. It creates sub-generators for modular scaffolding and configures the yeoman-environment for generator discovery and execution via the yo CLI.

Prompting phases use Inquirer.js question objects with support for input, confirm, list, checkbox, and expand prompt types. The skill generates dynamic prompts that adapt based on previous answers using the when property and validates input with custom validation functions.

Template writing uses this.fs.copyTpl() with EJS syntax for dynamic content generation. The skill handles file conflict resolution via the conflicter, manages destination paths with this.destinationPath(), and implements composability using this.composeWith() to chain multiple generators. It also integrates with yeoman-assert and yeoman-test for generator unit testing.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill yeoman-generator-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill yeoman-generator-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill yeoman-generator-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill yeoman-generator-builder -a codex
```

### OpenClaw

```bash
clawhub install yeoman-generator-builder
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/yeoman-generator-builder/)
