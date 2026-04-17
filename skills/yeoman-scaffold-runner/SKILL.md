---
title: "Yeoman Scaffold Runner"
description: "The Yeoman Scaffold Runner skill provides automated project and component scaffolding through the Yeoman ecosystem. It uses the yo CLI and yeoman-environment API to discover, install, and execute generators from the npm registry.\nThe skill manages generator lifecycles including prompting, file generation, conflict resolution, and installation phases. It supports sub-generator composition for adding features to existing projects, such as adding API routes, database models, or authentication modules to a previously scaffolded application.\nKey capabilities include batch scaffolding across multiple generators, custom prompt answering for non-interactive execution, and integration with yeoman-assert for testing generated output. The skill handles generator versioning, allows pinning specific generator versions for reproducible scaffolding, and supports private generator registries for enterprise template management."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/yeoman-scaffold-runner/"
framework:
  - "OpenClaw"
---

# Yeoman Scaffold Runner

The Yeoman Scaffold Runner skill provides automated project and component scaffolding through the Yeoman ecosystem. It uses the yo CLI and yeoman-environment API to discover, install, and execute generators from the npm registry.
The skill manages generator lifecycles including prompting, file generation, conflict resolution, and installation phases. It supports sub-generator composition for adding features to existing projects, such as adding API routes, database models, or authentication modules to a previously scaffolded application.
Key capabilities include batch scaffolding across multiple generators, custom prompt answering for non-interactive execution, and integration with yeoman-assert for testing generated output. The skill handles generator versioning, allows pinning specific generator versions for reproducible scaffolding, and supports private generator registries for enterprise template management.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/yeoman-scaffold-runner
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/yeoman-scaffold-runner` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/yeoman-scaffold-runner/)
