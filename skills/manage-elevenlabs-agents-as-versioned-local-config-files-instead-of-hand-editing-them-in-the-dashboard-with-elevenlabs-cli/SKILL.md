---
title: "Manage ElevenLabs agents as versioned local config files instead of hand-editing them in the dashboard with ElevenLabs CLI"
description: "Initialize, authenticate, and edit ElevenLabs agent configs from local files when you want agent definitions in code review instead of only in a hosted UI."
verification: security_reviewed
source: "https://github.com/elevenlabs/cli"
category:
  - "Integrations & Connectors"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "elevenlabs/cli"
  github_stars: 49
  npm_package: "@elevenlabs/cli"
  npm_weekly_downloads: 10433
---

# Manage ElevenLabs agents as versioned local config files instead of hand-editing them in the dashboard with ElevenLabs CLI

ElevenLabs CLI is only publishable when framed narrowly around agents-as-code workflows. The useful operator job is to initialize an ElevenLabs agent locally, authenticate, edit its config in files, and sync changes with more structure than hand-editing in the dashboard. That is the moment to invoke this skill instead of using the hosted product normally.

The scope boundary is important. This is not a generic ElevenLabs product listing, not a voice platform overview, and not a general SDK card. The bounded workflow is local configuration management for ElevenLabs agents, with templates and schema-backed edits. It is the weakest approved finalist because it sits closer to a vendor CLI listing than the other approvals.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/manage-elevenlabs-agents-as-versioned-local-config-files-instead-of-hand-editing-them-in-the-dashboard-with-elevenlabs-cli
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/manage-elevenlabs-agents-as-versioned-local-config-files-instead-of-hand-editing-them-in-the-dashboard-with-elevenlabs-cli` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/manage-elevenlabs-agents-as-versioned-local-config-files-instead-of-hand-editing-them-in-the-dashboard-with-elevenlabs-cli/)
