---
title: "Yeoman Enterprise Generator Suite"
description: "Manages Yeoman generators for enterprise application scaffolding with custom sub-generators. Handles Angular module generation via generator-angular, Express API scaffolding, and composite generators with shared prompting and conflict resolution."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/yeoman-enterprise-generator-suite/"
category:
  - "Templates &amp; Workflows"
framework:
  - "Claude Code"
---

# Yeoman Enterprise Generator Suite

The Yeoman Enterprise Generator Suite provides standardized application scaffolding across engineering teams using the Yeoman generator ecosystem. It manages custom generators built on the yeoman-generator base class with composable sub-generators for modular project assembly.

The suite includes generators for common enterprise patterns: Angular feature modules with NgRx state management, Express.js REST APIs with OpenAPI specification generation, React component libraries with Storybook integration, and NestJS microservices with gRPC protocol buffer definitions. Each generator enforces organizational coding standards through ESLint configurations, TypeScript strict mode settings, and test coverage requirements.

Advanced generator features include composability where parent generators delegate to specialized sub-generators for database layers, authentication modules, and deployment configurations. The shared prompting system maintains user preferences across generator invocations via the Yeoman storage API. Conflict resolution handles file merging when regenerating into existing projects, with visual diff presentation for manual resolution decisions. Generator versioning ensures teams use approved template versions through a private npm registry with semver constraints.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/yeoman-enterprise-generator-suite/)
