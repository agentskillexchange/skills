---
name: Notion Workspace Sync Engine
description: Bidirectionally syncs Notion databases with external tools via the Notion
  API and webhooks. Maps page properties to Jira issues, GitHub PRs, and Linear tickets
  in real time.
verification: security_reviewed
source: https://developers.notion.com/
category:
- Calendar, Email &amp; Productivity
framework:
- Gemini
---
# Notion Workspace Sync Engine

The Notion Workspace Sync Engine establishes bidirectional synchronization between Notion databases and external project management tools using the Notion API v1. It polls Notion databases via the /databases/{id}/query endpoint with filter and sort parameters to detect changes, comparing timestamps against a local state cache for incremental processing. Property mapping is configured through a declarative schema that translates Notion select/multi-select properties to Jira issue types and labels, Notion date ranges to GitHub milestone dates, and Notion relation properties to Linear issue parent-child hierarchies. The skill handles rich text conversion between Notion blocks (paragraphs, headings, code, callouts) and Markdown/HTML formats used by target platforms. Conflict resolution uses a last-writer-wins strategy with configurable field-level priority rules—for example, status changes in Jira always win, but description edits in Notion take precedence. Webhook endpoints receive real-time Notion database change events for near-instant propagation. The sync engine maintains an audit log of all operations, supports dry-run mode for previewing changes, and includes rollback capability to revert the last N sync operations.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/notion-workspace-sync-engine-2/)
