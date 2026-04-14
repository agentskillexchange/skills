---
title: "Yeoman Scaffold Runner"
description: "Executes Yeoman generators via the yo CLI and yeoman-environment API to scaffold applications, components, and microservices. Manages generator discovery through the npm registry and supports sub-generator composition."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/yeoman-scaffold-runner/"
category:
  - "Templates &amp; Workflows"
framework:
  - "OpenClaw"
---

# Yeoman Scaffold Runner

The Yeoman Scaffold Runner skill provides automated project and component scaffolding through the Yeoman ecosystem. It uses the yo CLI and yeoman-environment API to discover, install, and execute generators from the npm registry.

The skill manages generator lifecycles including prompting, file generation, conflict resolution, and installation phases. It supports sub-generator composition for adding features to existing projects, such as adding API routes, database models, or authentication modules to a previously scaffolded application.

Key capabilities include batch scaffolding across multiple generators, custom prompt answering for non-interactive execution, and integration with yeoman-assert for testing generated output. The skill handles generator versioning, allows pinning specific generator versions for reproducible scaffolding, and supports private generator registries for enterprise template management.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/yeoman-scaffold-runner/)
