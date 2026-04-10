---
name: Yeoman Generator Builder
description: Creates custom Yeoman generators using the yeoman-generator API and yo
  CLI. Scaffolds generator packages with prompting, writing, and install phases, supporting
  composability via this.composeWith() for multi-generator workflows.
verification: security_reviewed
source: https://agentskillexchange.com/skills/yeoman-generator-builder/
category:
- Templates &amp; Workflows
framework:
- OpenClaw
---
# Yeoman Generator Builder

The Yeoman Generator Builder skill helps create custom project scaffolding generators using the Yeoman ecosystem. It leverages the yeoman-generator base class to define generators with proper lifecycle phases: initializing, prompting, configuring, writing, conflicts, install, and end.
The skill scaffolds generator npm packages with the required generator-* naming convention and proper directory structure. It creates sub-generators for modular scaffolding and configures the yeoman-environment for generator discovery and execution via the yo CLI.
Prompting phases use Inquirer.js question objects with support for input, confirm, list, checkbox, and expand prompt types. The skill generates dynamic prompts that adapt based on previous answers using the when property and validates input with custom validation functions.
Template writing uses this.fs.copyTpl() with EJS syntax for dynamic content generation. The skill handles file conflict resolution via the conflicter, manages destination paths with this.destinationPath(), and implements composability using this.composeWith() to chain multiple generators. It also integrates with yeoman-assert and yeoman-test for generator unit testing.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/yeoman-generator-builder/)
