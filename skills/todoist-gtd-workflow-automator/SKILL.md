---
title: "Todoist GTD Workflow Automator"
description: "Implements Getting Things Done methodology on Todoist using the Todoist Sync API v9. Automates inbox processing, context labeling, weekly reviews, and project-to-next-action extraction with natural language parsing."
slug: "todoist-gtd-workflow-automator"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/todoist-gtd-workflow-automator/"
listed: true
---

# Todoist GTD Workflow Automator

Implements Getting Things Done methodology on Todoist using the Todoist Sync API v9. Automates inbox processing, context labeling, weekly reviews, and project-to-next-action extraction with natural language parsing.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install todoist-gtd-workflow-automator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Todoist GTD Workflow Automator brings David Allen’s Getting Things Done methodology to life within Todoist using the Todoist Sync API v9 and REST API v2. It automates the core GTD workflows that are tedious to maintain manually: inbox capture and processing, context-based labeling, horizon-of-focus project reviews, and next-action identification.
The inbox processor analyzes each captured item using natural language parsing to extract: project assignment (matching against existing Todoist projects via fuzzy search), context labels (@computer, @phone, @errands, @waiting_for), energy level tags, and time estimates. Two-minute tasks are flagged for immediate action. Items requiring delegation are moved to a @waiting_for label with a follow-up date. Reference materials are extracted and filed to linked Notion pages or Google Drive folders.
The weekly review module generates a structured review checklist: orphaned tasks without projects, projects without next actions, stale @waiting_for items past their follow-up dates, and someday/maybe items ready for activation. It produces a Markdown review summary and can schedule the next review as a recurring Todoist task. Advanced features include: natural language date parsing via Todoist’s date recognition, bulk operations for project reorganization, and integration with Toggl Track API for time tracking correlation.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/todoist-gtd-workflow-automator/)
