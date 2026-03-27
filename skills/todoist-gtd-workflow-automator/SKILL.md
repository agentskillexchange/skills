---
name: "Todoist GTD Workflow Automator"
description: "Implements Getting Things Done methodology on Todoist using the Todoist Sync API v9. Automates inbox processing, context labeling, weekly reviews, and project-to-next-action extraction with natural language parsing."
category: "Calendar, Email & Productivity"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/todoist-gtd-workflow-automator/"
tool_ecosystem:
  tool: notion
  github_stars: 5562
  npm_weekly_downloads: 1084242
  github_repo: makenotion/notion-sdk-js
  license: MIT
  maintained: true
---

# Todoist GTD Workflow Automator

Implements Getting Things Done methodology on Todoist using the Todoist Sync API v9. Automates inbox processing, context labeling, weekly reviews, and project-to-next-action extraction with natural language parsing.

## Overview

The Todoist GTD Workflow Automator brings David Allen’s Getting Things Done methodology to life within Todoist using the Todoist Sync API v9 and REST API v2. It automates the core GTD workflows that are tedious to maintain manually: inbox capture and processing, context-based labeling, horizon-of-focus project reviews, and next-action identification.

The inbox processor analyzes each captured item using natural language parsing to extract: project assignment (matching against existing Todoist projects via fuzzy search), context labels (@computer, @phone, @errands, @waiting_for), energy level tags, and time estimates. Two-minute tasks are flagged for immediate action. Items requiring delegation are moved to a @waiting_for label with a follow-up date. Reference materials are extracted and filed to linked Notion pages or Google Drive folders.

The weekly review module generates a structured review checklist: orphaned tasks without projects, projects without next actions, stale @waiting_for items past their follow-up dates, and someday/maybe items ready for activation. It produces a Markdown review summary and can schedule the next review as a recurring Todoist task. Advanced features include: natural language date parsing via Todoist’s date recognition, bulk operations for project reorganization, and integration with Toggl Track API for time tracking correlation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill todoist-gtd-workflow-automator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill todoist-gtd-workflow-automator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill todoist-gtd-workflow-automator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill todoist-gtd-workflow-automator -a codex
```

### OpenClaw

```bash
clawhub install todoist-gtd-workflow-automator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/todoist-gtd-workflow-automator/
