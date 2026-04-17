---
title: "Google Workspace CLI (gws)"
description: "Google Workspace CLI, distributed as gws, is a broad integration layer for Google Workspace that dynamically builds its command surface from Google’s Discovery Service. Instead of hand-writing separate wrappers for Gmail, Drive, Calendar, Sheets, Docs, Chat, and Admin APIs, users can authenticate once and then call Workspace resources through one consistent CLI that returns structured JSON. The upstream project explicitly positions this as useful both for human operators and AI agents, and the repository includes a large set of agent skills for higher-level workflows.\nFor ASE, the job-to-be-done is concrete: an agent can use gws to manage inboxes, inspect calendars, create spreadsheets, query Drive files, send Chat messages, and automate cross-service productivity tasks from one toolchain. The README documents OAuth setup, local and headless authentication flows, and multiple installation paths, including prebuilt binaries, npm, Cargo, Nix, and Homebrew. That makes it practical in both local desktop and server-style automation contexts.\nThe project has clear adoption and maintenance signals: a public GitHub repository, an npm package, release artifacts, Apache-2.0 licensing, and strong star activity with recent upstream commits. The documented npm install command is npm install -g @googleworkspace/cli, after which users can run authentication commands such as gws auth setup and gws auth login. Because it spans many Google services through a single automation entry point, it fits ASE’s productivity category as a real, source-verifiable integration tool."
verification: security_reviewed
source: "https://github.com/googleworkspace/cli"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "googleworkspace/cli"
  github_stars: 24348
---

# Google Workspace CLI (gws)

Google Workspace CLI, distributed as gws, is a broad integration layer for Google Workspace that dynamically builds its command surface from Google’s Discovery Service. Instead of hand-writing separate wrappers for Gmail, Drive, Calendar, Sheets, Docs, Chat, and Admin APIs, users can authenticate once and then call Workspace resources through one consistent CLI that returns structured JSON. The upstream project explicitly positions this as useful both for human operators and AI agents, and the repository includes a large set of agent skills for higher-level workflows.
For ASE, the job-to-be-done is concrete: an agent can use gws to manage inboxes, inspect calendars, create spreadsheets, query Drive files, send Chat messages, and automate cross-service productivity tasks from one toolchain. The README documents OAuth setup, local and headless authentication flows, and multiple installation paths, including prebuilt binaries, npm, Cargo, Nix, and Homebrew. That makes it practical in both local desktop and server-style automation contexts.
The project has clear adoption and maintenance signals: a public GitHub repository, an npm package, release artifacts, Apache-2.0 licensing, and strong star activity with recent upstream commits. The documented npm install command is npm install -g @googleworkspace/cli, after which users can run authentication commands such as gws auth setup and gws auth login. Because it spans many Google services through a single automation entry point, it fits ASE’s productivity category as a real, source-verifiable integration tool.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/google-workspace-cli-gws
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/google-workspace-cli-gws` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/google-workspace-cli-gws/)
