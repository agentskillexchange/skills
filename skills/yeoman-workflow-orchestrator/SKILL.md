---
title: "Yeoman Workflow Orchestrator"
description: "Orchestrates Yeoman generator workflows with composable sub-generators and mem-fs-editor file transformations. Manages generator dependencies via yo env and supports custom inquirer.js prompt chains."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/yeoman-workflow-orchestrator/"
category:
  - "Templates &amp; Workflows"
framework:
  - "Gemini"
---

# Yeoman Workflow Orchestrator

The Yeoman Workflow Orchestrator streamlines complex scaffolding workflows using Yeoman generators with composable sub-generator patterns. It manages the mem-fs-editor virtual file system for safe, transactional file transformations that can be previewed before writing to disk. The orchestrator handles generator dependencies through the yo environment, resolving and installing required generators automatically from npm. Custom inquirer.js prompt chains with conditional logic, validation, and dynamic choices guide users through project configuration. The tool supports generator composition where multiple generators run in sequence, sharing context and configuration. It includes a workflow definition format for defining multi-step scaffolding processes that combine Yeoman generators with custom transformation steps. Template conflict resolution handles cases where generated files already exist, offering diff views and merge options. Integration with the Yeoman store persists user preferences across generator runs for consistent defaults.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/yeoman-workflow-orchestrator/)
