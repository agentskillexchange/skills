---
title: "Triage production log spikes and incidents from the terminal with lnav"
description: "Open raw logs, jump to error clusters, query structured fields, and summarize incident clues without shipping data to a separate platform."
verification: "listed"
source: "https://github.com/tstack/lnav"
author: "tstack"
publisher_type: "individual"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "tstack/lnav"
  github_stars: 10159
---

# Triage production log spikes and incidents from the terminal with lnav

Open raw logs, jump to error clusters, query structured fields, and summarize incident clues without shipping data to a separate platform.

## Prerequisites

lnav, local or remote log files, terminal access

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install lnav from your system package manager or build it from source, then open one or more log files with `lnav /path/to/log*` and use its built-in SQL, filters, and timeline views for triage.
```

## Documentation

- https://docs.lnav.org/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/triage-production-log-spikes-and-incidents-from-the-terminal-with-lnav/)
