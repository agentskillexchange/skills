---
title: "Load .mbox mail archives into SQLite for offline search, audits, and dataset joins"
description: "Use mbox-to-sqlite when an agent needs to work across an email archive as structured data instead of parsing one message at a time. The agent imports a mailbox into SQLite, then hands the resulting database to search, reporting, and cross-dataset workflows without depending on a live mail provider."
verification: "security_reviewed"
source: "https://github.com/simonw/mbox-to-sqlite"
author: "Simon Willison"
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

## Prerequisites

Python 3, pip, a .mbox mailbox export, and SQLite-compatible analysis tooling.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
pip install mbox-to-sqlite
```

## Documentation

- https://github.com/simonw/mbox-to-sqlite

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/load-mbox-mail-archives-into-sqlite-for-offline-search-audits-and-dataset-joins/)
