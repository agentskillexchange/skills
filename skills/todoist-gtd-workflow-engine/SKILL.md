---
name: "Todoist GTD Workflow Engine"
description: "Implements Getting Things Done methodology on Todoist using the Sync API v9. Automates weekly reviews, context tagging, and project decomposition into next actions."
category: "Calendar, Email & Productivity"
framework: "MCP-compatible"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/todoist-gtd-workflow-engine/"
---

# Todoist GTD Workflow Engine

Implements Getting Things Done methodology on Todoist using the Sync API v9. Automates weekly reviews, context tagging, and project decomposition into next actions.

## Overview

The Todoist GTD Workflow Engine skill implements David Allen’s Getting Things Done methodology on top of the Todoist Sync API v9. It automates the five GTD phases: capture, clarify, organize, reflect, and engage through programmable task processing pipelines.

The capture phase monitors the Todoist inbox for new items and applies clarification rules to determine actionability, delegation potential, and project assignment. Organization uses Todoist labels as GTD contexts (phone, computer, errands, home) and projects as outcome-based containers. Two-minute rule detection flags quick tasks for immediate execution.

Weekly review automation generates a structured checklist that walks through all projects, waiting-for items, and someday-maybe lists. The engine creates review tasks with embedded queries showing stale items and projects without next actions. Sync API v9 batch commands handle bulk updates efficiently, processing hundreds of task modifications in single API calls with proper temp_id resolution for new items.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill todoist-gtd-workflow-engine
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill todoist-gtd-workflow-engine -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill todoist-gtd-workflow-engine -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill todoist-gtd-workflow-engine -a codex
```

### OpenClaw

```bash
clawhub install todoist-gtd-workflow-engine
```

## Source

- Marketplace: https://agentskillexchange.com/skills/todoist-gtd-workflow-engine/
