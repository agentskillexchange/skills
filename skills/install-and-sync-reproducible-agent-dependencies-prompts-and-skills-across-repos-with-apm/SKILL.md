---
title: "Install and sync reproducible agent dependencies, prompts, and skills across repos with APM"
description: "Use one manifest to reproduce agent setup across repositories so skills, prompts, plugins, and config stop drifting from machine to machine."
verification: "listed"
source: "https://github.com/microsoft/apm"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "microsoft/apm"
  github_stars: 1934
  npm_package: "apm-cli"
  npm_weekly_downloads: 5075
---

# Install and sync reproducible agent dependencies, prompts, and skills across repos with APM

Use APM when an agent or team needs to bootstrap the same agent setup across repositories from a manifest instead of manually reconfiguring Claude Code, Codex, Cursor, Copilot, plugins, prompts, and related agent dependencies one repo at a time. The workflow is specific: declare agent packages and primitives in apm.yml, install or sync them into a project, and keep that setup reproducible across environments. That scope boundary, manifest-driven agent dependency installation and sync, keeps this skill distinct from a general AI platform or coding agent listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/install-and-sync-reproducible-agent-dependencies-prompts-and-skills-across-repos-with-apm/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/install-and-sync-reproducible-agent-dependencies-prompts-and-skills-across-repos-with-apm
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/install-and-sync-reproducible-agent-dependencies-prompts-and-skills-across-repos-with-apm`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/install-and-sync-reproducible-agent-dependencies-prompts-and-skills-across-repos-with-apm/)
