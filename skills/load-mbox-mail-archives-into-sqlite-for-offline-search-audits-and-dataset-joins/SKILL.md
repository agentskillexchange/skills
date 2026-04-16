---
title: "Load .mbox mail archives into SQLite for offline search, audits, and dataset joins"
description: "Use mbox-to-sqlite when an agent needs to work across an email archive as structured data instead of parsing one message at a time. The agent imports a mailbox into SQLite, then hands the resulting database to search, reporting, and cross-dataset workflows without depending on a live mail provider."
verification: "security_reviewed"
source: "https://github.com/simonw/mbox-to-sqlite"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "simonw/mbox-to-sqlite"
  github_stars: 39
---

# Load .mbox mail archives into SQLite for offline search, audits, and dataset joins

Tool: mbox-to-sqlite by Simon Willison.

This skill gives an agent a bounded workflow for turning an email archive in .mbox format into a local SQLite database. The upstream tool does not try to be an email client. Its purpose is narrower and more useful for automation: ingest one or more mailbox exports into structured tables so an agent can query messages, inspect patterns, build reports, and join mail records against other datasets. That is especially handy for legacy archive review, compliance checks, incident reconstruction, migration prep, or research projects built on exported mailboxes.

Invoke this when the user already has an .mbox file and the next step is analysis, not sending mail. If an agent needs to find patterns across thousands of archived messages, answer questions about a historical mailbox, or combine email metadata with other SQLite tables, this workflow beats opening a desktop mail app or writing one-off parsers. It creates a stable database that can be searched repeatedly and inspected with SQL, Datasette, Python, or other local tools.

The scope boundary is what makes this skill-shaped. It is not a generic email platform listing, not an IMAP client, and not a live inbox triage system. It does one job well: import .mbox archives into SQLite so downstream agents can analyze them offline.

Integration points are practical. The resulting database can feed reporting notebooks, legal review workflows, entity extraction pipelines, or internal audit tools. Because the output is SQLite, it also pairs cleanly with other local tables when the user needs cross-reference work rather than another isolated mailbox viewer.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/load-mbox-mail-archives-into-sqlite-for-offline-search-audits-and-dataset-joins/)
