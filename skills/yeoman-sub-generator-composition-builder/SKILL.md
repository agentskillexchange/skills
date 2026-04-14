---
title: "Yeoman Sub-Generator Composition Builder"
description: "Orchestrates Yeoman generator composition by chaining sub-generators via the Yeoman Environment API. Manages yo run loops, priority queues, and cross-generator dependency resolution."
verification: security_reviewed
source: "https://github.com/yeoman/yo"
category:
  - "Templates &amp; Workflows"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "yeoman/yo"
  github_stars: 3953
  npm_package: "yo"
  npm_weekly_downloads: 402691
---

# Yeoman Sub-Generator Composition Builder

The Yeoman Sub-Generator Composition Builder automates complex project generation workflows by orchestrating multiple Yeoman sub-generators through the yeoman-environment API. It uses the composeWith() method to chain generators in dependency order, managing the Yeoman run loop priority queue to ensure initializing, prompting, configuring, writing, and install phases execute correctly across composed generators. The skill resolves generator dependencies from the npm registry, checking for locally installed generators via yo –generators and installing missing ones on demand. It handles cross-generator conflict resolution using the Yeoman conflicter with configurable merge strategies for shared files like package.json and tsconfig.json. The skill supports both local generators in the generators/ directory and published npm generator packages prefixed with generator-. It can replay stored answers from .yo-rc.json for reproducible scaffolding and manages the Yeoman storage API for persisting configuration across sub-generator boundaries.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/yeoman-sub-generator-composition-builder/)
