---
title: "Todoist GTD Workflow Engine"
description: "The Todoist GTD Workflow Engine skill implements David Allen’s Getting Things Done methodology on top of the Todoist Sync API v9. It automates the five GTD phases: capture, clarify, organize, reflect, and engage through programmable task processing pipelines.\nThe capture phase monitors the Todoist inbox for new items and applies clarification rules to determine actionability, delegation potential, and project assignment. Organization uses Todoist labels as GTD contexts (phone, computer, errands, home) and projects as outcome-based containers. Two-minute rule detection flags quick tasks for immediate execution.\nWeekly review automation generates a structured checklist that walks through all projects, waiting-for items, and someday-maybe lists. The engine creates review tasks with embedded queries showing stale items and projects without next actions. Sync API v9 batch commands handle bulk updates efficiently, processing hundreds of task modifications in single API calls with proper temp_id resolution for new items."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/todoist-gtd-workflow-engine/"
framework:
  - "MCP"
---

# Todoist GTD Workflow Engine

The Todoist GTD Workflow Engine skill implements David Allen’s Getting Things Done methodology on top of the Todoist Sync API v9. It automates the five GTD phases: capture, clarify, organize, reflect, and engage through programmable task processing pipelines.
The capture phase monitors the Todoist inbox for new items and applies clarification rules to determine actionability, delegation potential, and project assignment. Organization uses Todoist labels as GTD contexts (phone, computer, errands, home) and projects as outcome-based containers. Two-minute rule detection flags quick tasks for immediate execution.
Weekly review automation generates a structured checklist that walks through all projects, waiting-for items, and someday-maybe lists. The engine creates review tasks with embedded queries showing stale items and projects without next actions. Sync API v9 batch commands handle bulk updates efficiently, processing hundreds of task modifications in single API calls with proper temp_id resolution for new items.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/todoist-gtd-workflow-engine
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/todoist-gtd-workflow-engine` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/todoist-gtd-workflow-engine/)
