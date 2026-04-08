---
title: Yeoman Generator Builder
description: 'The Yeoman Generator Builder skill helps create custom project scaffolding
  generators using the Yeoman ecosystem. It leverages the yeoman-generator base class
  to define generators with proper lifecycle phases: initializing, prompting, configuring,
  writing, conflicts, install, and end. The skill scaffolds generator npm packages
  with the required generator-* naming convention and proper directory structure.
  It creates sub-generators for modular scaffolding and configures the yeoman-environment
  for generator discovery and execution via the yo CLI. Prompting phases use Inquirer.js
  question objects with support for input, confirm, list, checkbox, and expand prompt
  types. The skill generates dynamic prompts that adapt based on previous answers
  using the when property and validates input with custom validation functions. Template
  writing uses this.fs.copyTpl() with EJS syntax for dynamic content generation. The
  skill handles file conflict resolution via the conflicter, manages destination paths
  with this.destinationPath(), and implements composability using this.composeWith()
  to chain multiple generators. It also integrates with yeoman-assert and yeoman-test
  for generator unit testing.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/yeoman-generator-builder/
category:
- Templates &amp; Workflows
framework:
- OpenClaw
---

# Yeoman Generator Builder

The Yeoman Generator Builder skill helps create custom project scaffolding generators using the Yeoman ecosystem. It leverages the yeoman-generator base class to define generators with proper lifecycle phases: initializing, prompting, configuring, writing, conflicts, install, and end. The skill scaffolds generator npm packages with the required generator-* naming convention and proper directory structure. It creates sub-generators for modular scaffolding and configures the yeoman-environment for generator discovery and execution via the yo CLI. Prompting phases use Inquirer.js question objects with support for input, confirm, list, checkbox, and expand prompt types. The skill generates dynamic prompts that adapt based on previous answers using the when property and validates input with custom validation functions. Template writing uses this.fs.copyTpl() with EJS syntax for dynamic content generation. The skill handles file conflict resolution via the conflicter, manages destination paths with this.destinationPath(), and implements composability using this.composeWith() to chain multiple generators. It also integrates with yeoman-assert and yeoman-test for generator unit testing.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/yeoman-generator-builder/)
