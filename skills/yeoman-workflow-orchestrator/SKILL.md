---
name: "Yeoman Workflow Orchestrator"
description: "Orchestrates Yeoman generator workflows with composable sub-generators and mem-fs-editor file transformations. Manages generator dependencies via yo env and supports custom inquirer.js prompt chains."
category: "Templates &amp; Workflows"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/yeoman-workflow-orchestrator/"
---
# Yeoman Workflow Orchestrator

Orchestrates Yeoman generator workflows with composable sub-generators and mem-fs-editor file transformations. Manages generator dependencies via yo env and supports custom inquirer.js prompt chains.

The Yeoman Workflow Orchestrator streamlines complex scaffolding workflows using Yeoman generators with composable sub-generator patterns. It manages the mem-fs-editor virtual file system for safe, transactional file transformations that can be previewed before writing to disk. The orchestrator handles generator dependencies through the yo environment, resolving and installing required generators automatically from npm. Custom inquirer.js prompt chains with conditional logic, validation, and dynamic choices guide users through project configuration. The tool supports generator composition where multiple generators run in sequence, sharing context and configuration. It includes a workflow definition format for defining multi-step scaffolding processes that combine Yeoman generators with custom transformation steps. Template conflict resolution handles cases where generated files already exist, offering diff views and merge options. Integration with the Yeoman store persists user preferences across generator runs for consistent defaults.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill yeoman-workflow-orchestrator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill yeoman-workflow-orchestrator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill yeoman-workflow-orchestrator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill yeoman-workflow-orchestrator -a codex
```

### OpenClaw

```bash
clawhub install yeoman-workflow-orchestrator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/yeoman-workflow-orchestrator/)
