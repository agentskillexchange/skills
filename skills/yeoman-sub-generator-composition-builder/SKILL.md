---
title: "Yeoman Sub-Generator Composition Builder"
description: "Orchestrates Yeoman generator composition by chaining sub-generators via the Yeoman Environment API. Manages yo run loops, priority queues, and cross-generator dependency resolution."
slug: "yeoman-sub-generator-composition-builder"
category:
  - "Templates &amp; Workflows"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://github.com/yeoman/yo"
tool_ecosystem:
  github_repo: "yeoman/yo"
  github_stars: 3953
  npm_package: "yo"
  npm_weekly_downloads: 343306
listed: true
---

# Yeoman Sub-Generator Composition Builder

Orchestrates Yeoman generator composition by chaining sub-generators via the Yeoman Environment API. Manages yo run loops, priority queues, and cross-generator dependency resolution.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install yeoman-sub-generator-composition-builder
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Yeoman Sub-Generator Composition Builder automates complex project generation workflows by orchestrating multiple Yeoman sub-generators through the yeoman-environment API. It uses the composeWith() method to chain generators in dependency order, managing the Yeoman run loop priority queue to ensure initializing, prompting, configuring, writing, and install phases execute correctly across composed generators. The skill resolves generator dependencies from the npm registry, checking for locally installed generators via yo –generators and installing missing ones on demand. It handles cross-generator conflict resolution using the Yeoman conflicter with configurable merge strategies for shared files like package.json and tsconfig.json. The skill supports both local generators in the generators/ directory and published npm generator packages prefixed with generator-. It can replay stored answers from .yo-rc.json for reproducible scaffolding and manages the Yeoman storage API for persisting configuration across sub-generator boundaries.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/yeoman-sub-generator-composition-builder/)
