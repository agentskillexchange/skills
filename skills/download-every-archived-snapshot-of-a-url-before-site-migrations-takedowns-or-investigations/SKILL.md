---
title: "Download every archived snapshot of a URL before site migrations, takedowns, or investigations"
description: "Use waybackpack when an agent needs the full historical record for a URL, not a few clicks through the Wayback Machine UI. The agent can list or download snapshots, constrain by date, deduplicate archives, and preserve evidence locally before a site changes or disappears."
verification: "security_reviewed"
source: "https://github.com/jsvine/waybackpack"
author: "Jeremy Singer-Vine"
category:
  - "Research & Scraping"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "jsvine/waybackpack"
  github_stars: 3173
---

# Download every archived snapshot of a URL before site migrations, takedowns, or investigations

Use waybackpack when an agent needs the full historical record for a URL, not a few clicks through the Wayback Machine UI. The agent can list or download snapshots, constrain by date, deduplicate archives, and preserve evidence locally before a site changes or disappears.

## Prerequisites

Python 3, pip, a target URL, local disk space for archived snapshots, and optional tqdm for progress output.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
pip install waybackpack
```

## Documentation

- https://github.com/jsvine/waybackpack

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/download-every-archived-snapshot-of-a-url-before-site-migrations-takedowns-or-investigations/)
