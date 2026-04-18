---
title: "Embed bounded Claude Code sessions into Python automation with the Claude Agent SDK"
description: "Use the Claude Agent SDK for Python when an existing script or service needs to delegate scoped repo work to Claude Code and consume structured responses programmatically."
verification: security_reviewed
source: "https://github.com/anthropics/claude-agent-sdk-python"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "anthropics/claude-agent-sdk-python"
  github_stars: 6390
  ase_npm_package: "claude-agent-sdk"
---

# Embed bounded Claude Code sessions into Python automation with the Claude Agent SDK

This skill is for Python automation that needs to call Claude Code as a component instead of as a human-operated terminal session. It covers the workflow of launching queries from Python, constraining tool permissions, setting working directories, and consuming streamed or structured responses inside a larger automation pipeline.

Invoke this instead of using Claude Code manually when the real job is orchestration from Python, such as repository maintenance tasks, coding helpers inside an internal service, or batch workflows that need a bounded coding agent step.

The scope boundary is specific: this is not a generic SDK listing and not a broad Anthropic platform card. It is about embedding Claude Code style sessions inside Python automation through the SDK boundary.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/embed-bounded-claude-code-sessions-into-python-automation-with-the-claude-agent-sdk
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/embed-bounded-claude-code-sessions-into-python-automation-with-the-claude-agent-sdk` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/embed-bounded-claude-code-sessions-into-python-automation-with-the-claude-agent-sdk/)
