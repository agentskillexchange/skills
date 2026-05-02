---
title: "Yeoman Workflow Orchestrator"
description: "Orchestrates Yeoman generator workflows with composable sub-generators and mem-fs-editor file transformations. Manages generator dependencies via yo env and supports custom inquirer.js prompt chains."
verification: "security_reviewed"
source: "https://github.com/yeoman/yo"
category:
  - "Templates & Workflows"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "yeoman/yo"
  github_stars: 3956
  npm_package: "yo"
  npm_weekly_downloads: 428357
---

# Yeoman Workflow Orchestrator

The Yeoman Workflow Orchestrator streamlines complex scaffolding workflows using Yeoman generators with composable sub-generator patterns. It manages the mem-fs-editor virtual file system for safe, transactional file transformations that can be previewed before writing to disk. The orchestrator handles generator dependencies through the yo environment, resolving and installing required generators automatically from npm. Custom inquirer.js prompt chains with conditional logic, validation, and dynamic choices guide users through project configuration. The tool supports generator composition where multiple generators run in sequence, sharing context and configuration. It includes a workflow definition format for defining multi-step scaffolding processes that combine Yeoman generators with custom transformation steps. Template conflict resolution handles cases where generated files already exist, offering diff views and merge options. Integration with the Yeoman store persists user preferences across generator runs for consistent defaults.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/yeoman-workflow-orchestrator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/yeoman-workflow-orchestrator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/yeoman-workflow-orchestrator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/yeoman-workflow-orchestrator/)
