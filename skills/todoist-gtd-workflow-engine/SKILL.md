---
title: "Todoist GTD Workflow Engine"
description: "Implements Getting Things Done methodology on Todoist using the Sync API v9. Automates weekly reviews, context tagging, and project decomposition into next actions."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/todoist-gtd-workflow-engine/"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "MCP"
---

# Todoist GTD Workflow Engine

The Todoist GTD Workflow Engine skill implements David Allen’s Getting Things Done methodology on top of the Todoist Sync API v9. It automates the five GTD phases: capture, clarify, organize, reflect, and engage through programmable task processing pipelines.

The capture phase monitors the Todoist inbox for new items and applies clarification rules to determine actionability, delegation potential, and project assignment. Organization uses Todoist labels as GTD contexts (phone, computer, errands, home) and projects as outcome-based containers. Two-minute rule detection flags quick tasks for immediate execution.

Weekly review automation generates a structured checklist that walks through all projects, waiting-for items, and someday-maybe lists. The engine creates review tasks with embedded queries showing stale items and projects without next actions. Sync API v9 batch commands handle bulk updates efficiently, processing hundreds of task modifications in single API calls with proper temp_id resolution for new items.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/todoist-gtd-workflow-engine/)
