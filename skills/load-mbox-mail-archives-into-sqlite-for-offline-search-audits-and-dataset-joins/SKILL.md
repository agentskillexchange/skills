---
name: Load .mbox mail archives into SQLite for offline search, audits, and dataset
  joins
description: Use mbox-to-sqlite when an agent needs to work across an email archive
  as structured data instead of parsing one message at a time. The agent imports a
  mailbox into SQLite, then hands the resulting database to search, reporting, and
  cross-dataset workflows without depending on a live mail provider.
category: Calendar, Email & Productivity
framework: Multi-Framework
verification: security_reviewed
source: https://github.com/simonw/mbox-to-sqlite
tool_ecosystem:
  github_repo: simonw/mbox-to-sqlite
  github_stars: 39
  tool: mbox-to-sqlite
---
# Load .mbox mail archives into SQLite for offline search, audits, and dataset joins
Use mbox-to-sqlite when an agent needs to work across an email archive as structured data instead of parsing one message at a time. The agent imports a mailbox into SQLite, then hands the resulting database to search, reporting, and cross-dataset workflows without depending on a live mail provider.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/load-mbox-mail-archives-into-sqlite-for-offline-search-audits-and-dataset-joins
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/load-mbox-mail-archives-into-sqlite-for-offline-search-audits-and-dataset-joins` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/load-mbox-mail-archives-into-sqlite-for-offline-search-audits-and-dataset-joins/)
