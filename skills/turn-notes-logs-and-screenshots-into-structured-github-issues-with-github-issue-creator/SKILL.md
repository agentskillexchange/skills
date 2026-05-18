---
name: "Turn notes, logs, and screenshots into structured GitHub issues with GitHub Issue Creator"
slug: "turn-notes-logs-and-screenshots-into-structured-github-issues-with-github-issue-creator"
description: "Convert messy bug notes, error logs, voice dictation, and screenshots into crisp GitHub issue reports with clear repro steps, impact, and evidence."
verification: "security_reviewed"
source: "https://github.com/microsoft/skills/tree/main/.github/skills/github-issue-creator"
author: "Microsoft"
publisher_type: "organization"
category: "Developer Tools"
framework: "Multi-Framework"
---

# Turn notes, logs, and screenshots into structured GitHub issues with GitHub Issue Creator

Convert messy bug notes, error logs, voice dictation, and screenshots into crisp GitHub issue reports with clear repro steps, impact, and evidence.

## Prerequisites

GitHub issue markdown format, bug notes or logs, optional screenshots or GIF attachments

## Installation

Use the upstream install or setup path that matches your environment:
- npx skills add microsoft/skills
- git clone https://github.com/microsoft/skills.git
- pnpm install
- pnpm harness --list

Requirements and caveats from upstream:
- | [Python](#python) | 39 | -py |
- ├── plugins/ # Language-based plugin bundles (azure-sdk-python, etc.)
- ├── python/ # -> ../.github/skills/*-py

Basic usage or getting-started notes:
- bash
- Select the skills you need from the wizard. Skills are installed to your chosen agent's directory (e.g., .github/skills/ for GitHub Copilot) and symlinked if you use multiple agents.
- <details>

- Source: https://github.com/microsoft/skills/tree/main/.github/skills/github-issue-creator
- Extracted from upstream docs: https://raw.githubusercontent.com/microsoft/skills/HEAD/README.md

## Documentation

- https://microsoft.github.io/skills/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/turn-notes-logs-and-screenshots-into-structured-github-issues-with-github-issue-creator/)
