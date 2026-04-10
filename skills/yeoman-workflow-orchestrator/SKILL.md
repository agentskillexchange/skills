---
title: "Yeoman Workflow Orchestrator"
description: "Orchestrates Yeoman generator workflows with composable sub-generators and mem-fs-editor file transformations. Manages generator dependencies via yo env and supports custom inquirer.js prompt chains."
slug: "yeoman-workflow-orchestrator"
category:
  - "Templates &amp; Workflows"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/yeoman-workflow-orchestrator/"
listed: true
---

# Yeoman Workflow Orchestrator

Orchestrates Yeoman generator workflows with composable sub-generators and mem-fs-editor file transformations. Manages generator dependencies via yo env and supports custom inquirer.js prompt chains.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install yeoman-workflow-orchestrator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Yeoman Workflow Orchestrator streamlines complex scaffolding workflows using Yeoman generators with composable sub-generator patterns. It manages the mem-fs-editor virtual file system for safe, transactional file transformations that can be previewed before writing to disk. The orchestrator handles generator dependencies through the yo environment, resolving and installing required generators automatically from npm. Custom inquirer.js prompt chains with conditional logic, validation, and dynamic choices guide users through project configuration. The tool supports generator composition where multiple generators run in sequence, sharing context and configuration. It includes a workflow definition format for defining multi-step scaffolding processes that combine Yeoman generators with custom transformation steps. Template conflict resolution handles cases where generated files already exist, offering diff views and merge options. Integration with the Yeoman store persists user preferences across generator runs for consistent defaults.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/yeoman-workflow-orchestrator/)
