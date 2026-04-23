---
title: "Load .mbox mail archives into SQLite for offline search, audits, and dataset joins"
description: "Use mbox-to-sqlite when an agent needs to work across an email archive as structured data instead of parsing one message at a time. The agent imports a mailbox into SQLite, then hands the resulting database to search, reporting, and cross-dataset workflows without depending on a live mail provider."
verification: security_reviewed
source: "https://github.com/simonw/mbox-to-sqlite"
category:
  - "Calendar, Email & Productivity"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "simonw/mbox-to-sqlite"
  github_stars: 39
---

# Load .mbox mail archives into SQLite for offline search, audits, and dataset joins

Use mbox-to-sqlite when an agent needs to work across an email archive as structured data instead of parsing one message at a time. The agent imports a mailbox into SQLite, then hands the resulting database to search, reporting, and cross-dataset workflows without depending on a live mail provider.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/load-mbox-mail-archives-into-sqlite-for-offline-search-audits-and-dataset-joins/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/load-mbox-mail-archives-into-sqlite-for-offline-search-audits-and-dataset-joins
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/load-mbox-mail-archives-into-sqlite-for-offline-search-audits-and-dataset-joins`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/load-mbox-mail-archives-into-sqlite-for-offline-search-audits-and-dataset-joins/)
