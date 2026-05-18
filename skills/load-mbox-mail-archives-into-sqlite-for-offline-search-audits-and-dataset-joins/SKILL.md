---
name: "Load .mbox mail archives into SQLite for offline search, audits, and dataset joins"
slug: "load-mbox-mail-archives-into-sqlite-for-offline-search-audits-and-dataset-joins"
description: "Use mbox-to-sqlite when an agent needs to work across an email archive as structured data instead of parsing one message at a time. The agent imports a mailbox into SQLite, then hands the resulting database to search, reporting, and cross-dataset workflows without depending on a live mail provider."
github_stars: 39
verification: "listed"
source: "https://github.com/simonw/mbox-to-sqlite"
author: "Simon Willison"
category: "Calendar, Email & Productivity"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "simonw/mbox-to-sqlite"
  github_stars: 39
---

# Load .mbox mail archives into SQLite for offline search, audits, and dataset joins

Use mbox-to-sqlite when an agent needs to work across an email archive as structured data instead of parsing one message at a time. The agent imports a mailbox into SQLite, then hands the resulting database to search, reporting, and cross-dataset workflows without depending on a live mail provider.

## Prerequisites

Python 3, pip, a .mbox mailbox export, and SQLite-compatible analysis tooling.

## Installation

Use the upstream install or setup path that matches your environment:
- pip install mbox-to-sqlite
- pip install -e '.[test]'

Requirements and caveats from upstream:
- python -m venv venv

Basic usage or getting-started notes:
- Use the mbox command to import a .mbox file into a SQLite database:
- mbox-to-sqlite mbox emails.db path/to/messages.mbox
- You can try this out against an example containing a sample of 3,266 emails from the [Enron corpus](https://en.wikipedia.org/wiki/Enron_Corpus) like this:

- Source: https://github.com/simonw/mbox-to-sqlite
- Extracted from upstream docs: https://raw.githubusercontent.com/simonw/mbox-to-sqlite/HEAD/README.md

## Documentation

- https://github.com/simonw/mbox-to-sqlite

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/load-mbox-mail-archives-into-sqlite-for-offline-search-audits-and-dataset-joins/)
