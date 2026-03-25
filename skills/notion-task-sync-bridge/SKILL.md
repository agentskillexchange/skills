---
name: "Notion Task Sync Bridge"
description: "Bidirectionally syncs tasks between Notion databases and external project management tools using the Notion API v2022-06-28. Handles property mapping, status updates, and relation fields."
category: "Calendar, Email & Productivity"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/notion-task-sync-bridge/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "notion"  # from ase_tool_match
  github_stars: 5562  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 1084242  # from ase_npm_downloads
  github_repo: "makenotion/notion-sdk-js"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Notion Task Sync Bridge

Bidirectionally syncs tasks between Notion databases and external project management tools using the Notion API v2022-06-28. Handles property mapping, status updates, and relation fields.

## Overview

The Notion Task Sync Bridge skill establishes real-time bidirectional synchronization between Notion databases and external task management platforms. Using the Notion API v2022-06-28 with the databases/{id}/query POST endpoint, it polls for changes using the filter and sorts parameters. Property mapping supports all Notion property types including select, multi-select, date, relation, and rollup fields. The skill handles Notion’s pagination via the start_cursor and has_more response fields for databases with thousands of entries. Status updates are pushed via the pages/{id} PATCH endpoint with property-level granularity. Relation fields are resolved by cross-referencing linked databases through the /databases/{id} GET endpoint schema. Conflict resolution uses last-write-wins with configurable merge strategies for simultaneous edits. The skill maintains a local SQLite state database for tracking sync cursors and preventing duplicate operations. Webhook support via the Notion API integration enables near-instant change detection.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill notion-task-sync-bridge
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill notion-task-sync-bridge -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill notion-task-sync-bridge -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill notion-task-sync-bridge -a codex
```

### OpenClaw

```bash
clawhub install notion-task-sync-bridge
```

## Source

- Marketplace: https://agentskillexchange.com/skills/notion-task-sync-bridge/
