---
title: "Todoist GTD Workflow Engine"
description: "Implements Getting Things Done methodology on Todoist using the Sync API v9. Automates weekly reviews, context tagging, and project decomposition into next actions."
slug: "todoist-gtd-workflow-engine"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/todoist-gtd-workflow-engine/"
listed: true
---

# Todoist GTD Workflow Engine

Implements Getting Things Done methodology on Todoist using the Sync API v9. Automates weekly reviews, context tagging, and project decomposition into next actions.

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
clawhub install todoist-gtd-workflow-engine
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Todoist GTD Workflow Engine skill implements David Allen’s Getting Things Done methodology on top of the Todoist Sync API v9. It automates the five GTD phases: capture, clarify, organize, reflect, and engage through programmable task processing pipelines.
The capture phase monitors the Todoist inbox for new items and applies clarification rules to determine actionability, delegation potential, and project assignment. Organization uses Todoist labels as GTD contexts (phone, computer, errands, home) and projects as outcome-based containers. Two-minute rule detection flags quick tasks for immediate execution.
Weekly review automation generates a structured checklist that walks through all projects, waiting-for items, and someday-maybe lists. The engine creates review tasks with embedded queries showing stale items and projects without next actions. Sync API v9 batch commands handle bulk updates efficiently, processing hundreds of task modifications in single API calls with proper temp_id resolution for new items.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/todoist-gtd-workflow-engine/)
