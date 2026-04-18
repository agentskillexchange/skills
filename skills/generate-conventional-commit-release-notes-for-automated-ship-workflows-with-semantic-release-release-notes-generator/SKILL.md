---
title: "Generate conventional-commit release notes for automated ship workflows with semantic-release release-notes-generator"
description: "Generate structured release notes from Conventional Commits inside automated release pipelines when changelog generation is the specific job to do."
verification: listed
source: "https://github.com/semantic-release/release-notes-generator"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "semantic-release/release-notes-generator"
  github_stars: 361
  ase_npm_package: "@semantic-release/release-notes-generator"
  npm_weekly_downloads: 10982193
---

# Generate conventional-commit release notes for automated ship workflows with semantic-release release-notes-generator

Use this skill when a release pipeline already has semantic-release in place and the missing job is dependable release-note generation from commit history. The boundary is narrow and operator-facing: configure the release-notes-generator plugin, choose the preset and parsing rules, and emit changelog-ready notes during CI. That keeps it from being a plain product listing. The skill is not about adopting semantic-release as a whole. It is about the specific release-artifact step that turns commit metadata into publishable notes during ship automation.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/generate-conventional-commit-release-notes-for-automated-ship-workflows-with-semantic-release-release-notes-generator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/generate-conventional-commit-release-notes-for-automated-ship-workflows-with-semantic-release-release-notes-generator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-conventional-commit-release-notes-for-automated-ship-workflows-with-semantic-release-release-notes-generator/)
