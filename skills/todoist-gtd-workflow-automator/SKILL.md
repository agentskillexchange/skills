---
name: "Todoist GTD Workflow Automator"
description: "Implements Getting Things Done methodology on Todoist using the Todoist Sync API v9. Automates inbox processing, context labeling, weekly reviews, and project-to-next-action extraction with natural language parsing."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/todoist-gtd-workflow-automator/"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Cursor"
---

# Todoist GTD Workflow Automator

The Todoist GTD Workflow Automator brings David Allen's Getting Things Done methodology to life within Todoist using the Todoist Sync API v9 and REST API v2. It automates the core GTD workflows that are tedious to maintain manually: inbox capture and processing, context-based labeling, horizon-of-focus project reviews, and next-action identification.
The inbox processor analyzes each captured item using natural language parsing to extract: project assignment (matching against existing Todoist projects via fuzzy search), context labels (@computer, @phone, @errands, @waiting_for), energy level tags, and time estimates. Two-minute tasks are flagged for immediate action. Items requiring delegation are moved to a @waiting_for label with a follow-up date. Reference materials are extracted and filed to linked Notion pages or Google Drive folders.
The weekly review module generates a structured review checklist: orphaned tasks without projects, projects without next actions, stale @waiting_for items past their follow-up dates, and someday/maybe items ready for activation. It produces a Markdown review summary and can schedule the next review as a recurring Todoist task. Advanced features include: natural language date parsing via Todoist's date recognition, bulk operations for project reorganization, and integration with Toggl Track API for time tracking correlation.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/todoist-gtd-workflow-automator/)
