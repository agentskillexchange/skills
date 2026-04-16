---
title: "Yeoman Scaffold Runner"
description: "Executes Yeoman generators via the yo CLI and yeoman-environment API to scaffold applications, components, and microservices. Manages generator discovery through the npm registry and supports sub-generator composition."
verification: "security_reviewed"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/yeoman-scaffold-runner/)
