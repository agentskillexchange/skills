---
title: "Sync calendars between providers with a stateless CalendarSync job"
description: "Run a one-shot calendar sync or migration between Google, Outlook, CalDAV, ICS, and related systems without standing up a long-lived sync service."
verification: "listed"
source: "https://github.com/inovex/CalendarSync"
author: "inovex"
publisher_type: "organization"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "inovex/CalendarSync"
  github_stars: 217
---

# Sync calendars between providers with a stateless CalendarSync job

Run a one-shot calendar sync or migration between Google, Outlook, CalDAV, ICS, and related systems without standing up a long-lived sync service.

## Prerequisites

CalendarSync binary, calendar provider credentials, sync.yaml config

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install CalendarSync from GitHub releases or the documented asdf plugin, create a `sync.yaml` from the example config, set `CALENDARSYNC_ENCRYPTION_KEY`, then run `calendarsync --config sync.yaml`.
```

## Documentation

- https://github.com/inovex/CalendarSync

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sync-calendars-between-providers-with-a-stateless-calendarsync-job/)
