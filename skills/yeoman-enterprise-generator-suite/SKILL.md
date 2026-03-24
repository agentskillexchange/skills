---
name: "Yeoman Enterprise Generator Suite"
description: "Manages Yeoman generators for enterprise application scaffolding with custom sub-generators. Handles Angular module generation via generator-angular, Express API scaffolding, and composite generators with shared prompting and conflict resolution."
category: "Templates & Workflows"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/yeoman-enterprise-generator-suite/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "eslint"  # from ase_tool_match
  github_stars: 27186  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 109028697  # from ase_npm_downloads
  github_repo: "eslint/eslint"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Yeoman Enterprise Generator Suite

Manages Yeoman generators for enterprise application scaffolding with custom sub-generators. Handles Angular module generation via generator-angular, Express API scaffolding, and composite generators with shared prompting and conflict resolution.

## Overview

The Yeoman Enterprise Generator Suite provides standardized application scaffolding across engineering teams using the Yeoman generator ecosystem. It manages custom generators built on the yeoman-generator base class with composable sub-generators for modular project assembly.

The suite includes generators for common enterprise patterns: Angular feature modules with NgRx state management, Express.js REST APIs with OpenAPI specification generation, React component libraries with Storybook integration, and NestJS microservices with gRPC protocol buffer definitions. Each generator enforces organizational coding standards through ESLint configurations, TypeScript strict mode settings, and test coverage requirements.

Advanced generator features include composability where parent generators delegate to specialized sub-generators for database layers, authentication modules, and deployment configurations. The shared prompting system maintains user preferences across generator invocations via the Yeoman storage API. Conflict resolution handles file merging when regenerating into existing projects, with visual diff presentation for manual resolution decisions. Generator versioning ensures teams use approved template versions through a private npm registry with semver constraints.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill yeoman-enterprise-generator-suite
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill yeoman-enterprise-generator-suite -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill yeoman-enterprise-generator-suite -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill yeoman-enterprise-generator-suite -a codex
```

### OpenClaw

```bash
clawhub install yeoman-enterprise-generator-suite
```

## Source

- Marketplace: https://agentskillexchange.com/skills/yeoman-enterprise-generator-suite/
