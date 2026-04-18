---
title: "Spell-check docs and code comments with source-aware filters using pyspelling"
description: "Run filtered spell checks over Markdown, Sphinx, HTML, or code comments without flattening everything into one noisy text stream."
verification: listed
source: "https://github.com/facelessuser/pyspelling"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "facelessuser/pyspelling"
  github_stars: 94
---

# Spell-check docs and code comments with source-aware filters using pyspelling

Use pyspelling when an agent needs source-aware spell checking across documentation, generated text inputs, HTML, Markdown, or code comments with file-type-specific filters. It is especially useful when the workflow needs to preserve structure, ignore known non-prose regions, and fail CI only on meaningful spelling defects.

A user should invoke this instead of a generic spell checker when the task is configurable, format-aware spelling review across a project tree. The scope boundary is specific and skill-shaped: pyspelling orchestrates spelling scans with filters and dictionary backends such as Aspell or Hunspell, not general writing assistance, editing, or documentation publishing.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/spell-check-docs-and-code-comments-with-source-aware-filters-using-pyspelling
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/spell-check-docs-and-code-comments-with-source-aware-filters-using-pyspelling` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/spell-check-docs-and-code-comments-with-source-aware-filters-using-pyspelling/)
