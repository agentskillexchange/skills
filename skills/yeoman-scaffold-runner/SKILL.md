---
title: "Yeoman Scaffold Runner"
description: "Executes Yeoman generators via the yo CLI and yeoman-environment API to scaffold applications, components, and microservices. Manages generator discovery through the npm registry and supports sub-generator composition."
verification: "security_reviewed"
source: "https://github.com/yeoman/yeoman"
category:
  - "Templates & Workflows"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "yeoman/yeoman"
  github_stars: 10120
---

# Yeoman Scaffold Runner

The Yeoman Scaffold Runner skill provides automated project and component scaffolding through the Yeoman ecosystem. It uses the yo CLI and yeoman-environment API to discover, install, and execute generators from the npm registry. The skill manages generator lifecycles including prompting, file generation, conflict resolution, and installation phases. It supports sub-generator composition for adding features to existing projects, such as adding API routes, database models, or authentication modules to a previously scaffolded application. Key capabilities include batch scaffolding across multiple generators, custom prompt answering for non-interactive execution, and integration with yeoman-assert for testing generated output. The skill handles generator versioning, allows pinning specific generator versions for reproducible scaffolding, and supports private generator registries for enterprise template management.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/yeoman-scaffold-runner/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/yeoman-scaffold-runner
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/yeoman-scaffold-runner`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/yeoman-scaffold-runner/)
