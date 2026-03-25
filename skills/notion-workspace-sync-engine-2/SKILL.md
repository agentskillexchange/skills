---
name: "Notion Workspace Sync Engine"
description: "Bidirectionally syncs Notion databases with external tools via the Notion API and webhooks. Maps page properties to Jira issues, GitHub PRs, and Linear tickets in real time."
category: "Calendar, Email & Productivity"
framework: "Gemini"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/notion-workspace-sync-engine-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "notion"  # from ase_tool_match
  github_stars: 5562  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 1084242  # from ase_npm_downloads
  github_repo: "makenotion/notion-sdk-js"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Notion Workspace Sync Engine

Bidirectionally syncs Notion databases with external tools via the Notion API and webhooks. Maps page properties to Jira issues, GitHub PRs, and Linear tickets in real time.

## Overview

The Notion Workspace Sync Engine establishes bidirectional synchronization between Notion databases and external project management tools using the Notion API v1. It polls Notion databases via the /databases/{id}/query endpoint with filter and sort parameters to detect changes, comparing timestamps against a local state cache for incremental processing. Property mapping is configured through a declarative schema that translates Notion select/multi-select properties to Jira issue types and labels, Notion date ranges to GitHub milestone dates, and Notion relation properties to Linear issue parent-child hierarchies. The skill handles rich text conversion between Notion blocks (paragraphs, headings, code, callouts) and Markdown/HTML formats used by target platforms. Conflict resolution uses a last-writer-wins strategy with configurable field-level priority rules—for example, status changes in Jira always win, but description edits in Notion take precedence. Webhook endpoints receive real-time Notion database change events for near-instant propagation. The sync engine maintains an audit log of all operations, supports dry-run mode for previewing changes, and includes rollback capability to revert the last N sync operations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill notion-workspace-sync-engine-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill notion-workspace-sync-engine-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill notion-workspace-sync-engine-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill notion-workspace-sync-engine-2 -a codex
```

### OpenClaw

```bash
clawhub install notion-workspace-sync-engine-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/notion-workspace-sync-engine-2/
