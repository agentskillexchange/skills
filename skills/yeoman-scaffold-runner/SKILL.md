---
name: "Yeoman Scaffold Runner"
description: "Executes Yeoman generators via the yo CLI and yeoman-environment API to scaffold applications, components, and microservices. Manages generator discovery through the npm registry and supports sub-generator composition."
category: "Templates & Workflows"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/yeoman-scaffold-runner/"
---
# Yeoman Scaffold Runner

Executes Yeoman generators via the yo CLI and yeoman-environment API to scaffold applications, components, and microservices. Manages generator discovery through the npm registry and supports sub-generator composition.

## Overview

The Yeoman Scaffold Runner skill provides automated project and component scaffolding through the Yeoman ecosystem. It uses the yo CLI and yeoman-environment API to discover, install, and execute generators from the npm registry.

The skill manages generator lifecycles including prompting, file generation, conflict resolution, and installation phases. It supports sub-generator composition for adding features to existing projects, such as adding API routes, database models, or authentication modules to a previously scaffolded application.

Key capabilities include batch scaffolding across multiple generators, custom prompt answering for non-interactive execution, and integration with yeoman-assert for testing generated output. The skill handles generator versioning, allows pinning specific generator versions for reproducible scaffolding, and supports private generator registries for enterprise template management.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill yeoman-scaffold-runner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill yeoman-scaffold-runner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill yeoman-scaffold-runner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill yeoman-scaffold-runner -a codex
```

### OpenClaw

```bash
clawhub install yeoman-scaffold-runner
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/yeoman-scaffold-runner/)
