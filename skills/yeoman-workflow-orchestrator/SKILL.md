---
title: "Yeoman Workflow Orchestrator"
description: "Orchestrates Yeoman generator workflows with composable sub-generators and mem-fs-editor file transformations. Manages generator dependencies via yo env and supports custom inquirer.js prompt chains."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/yeoman-workflow-orchestrator/"
category:
  - "Templates &amp; Workflows"
framework:
  - "Gemini"
---

# Yeoman Workflow Orchestrator

The Yeoman Workflow Orchestrator streamlines complex scaffolding workflows using Yeoman generators with composable sub-generator patterns. It manages the mem-fs-editor virtual file system for safe, transactional file transformations that can be previewed before writing to disk. The orchestrator handles generator dependencies through the yo environment, resolving and installing required generators automatically from npm. Custom inquirer.js prompt chains with conditional logic, validation, and dynamic choices guide users through project configuration. The tool supports generator composition where multiple generators run in sequence, sharing context and configuration. It includes a workflow definition format for defining multi-step scaffolding processes that combine Yeoman generators with custom transformation steps. Template conflict resolution handles cases where generated files already exist, offering diff views and merge options. Integration with the Yeoman store persists user preferences across generator runs for consistent defaults.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/yeoman-workflow-orchestrator/)
