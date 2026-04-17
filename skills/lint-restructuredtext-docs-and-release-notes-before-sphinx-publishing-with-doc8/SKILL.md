---
title: "Lint reStructuredText docs and release notes before Sphinx publishing with doc8"
description: "Catch structural and line-style problems in reStructuredText docs before release notes and Sphinx pages go out broken or noisy."
verification: listed
source: "https://github.com/PyCQA/doc8"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "PyCQA/doc8"
  github_stars: 176
---

# Lint reStructuredText docs and release notes before Sphinx publishing with doc8

Use doc8 when an agent needs to lint reStructuredText documentation, changelogs, and other docs trees for invalid RST structure, long lines, trailing whitespace, tabs, or newline issues. It is a good fit for docs QA passes before publishing, release note cleanup, and CI gates around Sphinx-oriented repositories.

A user should invoke this instead of using a generic prose editor when the task is enforcing RST-specific documentation hygiene at repository scale. The scope boundary is tight and skill-shaped: doc8 checks documentation file structure and simple style rules for RST and related text files, not broader writing assistance, site generation, or content strategy.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/lint-restructuredtext-docs-and-release-notes-before-sphinx-publishing-with-doc8
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/lint-restructuredtext-docs-and-release-notes-before-sphinx-publishing-with-doc8` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-restructuredtext-docs-and-release-notes-before-sphinx-publishing-with-doc8/)
