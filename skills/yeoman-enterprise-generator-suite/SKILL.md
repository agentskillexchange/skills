---
title: "Yeoman Enterprise Generator Suite"
description: "Manages Yeoman generators for enterprise application scaffolding with custom sub-generators. Handles Angular module generation via generator-angular, Express API scaffolding, and composite generators with shared prompting and conflict resolution."
verification: "security_reviewed"
source: "https://github.com/yeoman/yo"
category:
  - "Templates & Workflows"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "yeoman/yo"
  github_stars: 3956
  npm_package: "yo"
  npm_weekly_downloads: 428357
---

# Yeoman Enterprise Generator Suite

The Yeoman Enterprise Generator Suite provides standardized application scaffolding across engineering teams using the Yeoman generator ecosystem. It manages custom generators built on the yeoman-generator base class with composable sub-generators for modular project assembly. The suite includes generators for common enterprise patterns: Angular feature modules with NgRx state management, Express.js REST APIs with OpenAPI specification generation, React component libraries with Storybook integration, and NestJS microservices with gRPC protocol buffer definitions. Each generator enforces organizational coding standards through ESLint configurations, TypeScript strict mode settings, and test coverage requirements. Advanced generator features include composability where parent generators delegate to specialized sub-generators for database layers, authentication modules, and deployment configurations. The shared prompting system maintains user preferences across generator invocations via the Yeoman storage API. Conflict resolution handles file merging when regenerating into existing projects, with visual diff presentation for manual resolution decisions. Generator versioning ensures teams use approved template versions through a private npm registry with semver constraints.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/yeoman-enterprise-generator-suite/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/yeoman-enterprise-generator-suite
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/yeoman-enterprise-generator-suite`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/yeoman-enterprise-generator-suite/)
