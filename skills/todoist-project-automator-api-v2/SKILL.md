---
name: "Todoist Project Automator"
description: "Automates Todoist project management using the Todoist REST API v2 and Sync API. Creates task templates, manages recurring workflows, and syncs with external project trackers."
category: "Calendar, Email & Productivity"
framework: "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/todoist-project-automator-api-v2/"
tool_ecosystem:
  tool: jira
---

# Todoist Project Automator

Automates Todoist project management using the Todoist REST API v2 and Sync API. Creates task templates, manages recurring workflows, and syncs with external project trackers.

## Overview

Todoist Project Automator leverages both the Todoist REST API v2 and the Sync API for comprehensive task management automation. It creates project templates with pre-defined task hierarchies, labels, and due date patterns using natural language parsing. The Sync API enables batch operations for bulk task creation and modification with minimal API calls. The tool supports recurring workflow templates that automatically spawn task sequences when triggered by webhooks or calendar events. Integration with Jira and Linear APIs enables bidirectional sync of task status, keeping external project trackers aligned. It handles Todoist filter queries for generating progress reports and workload analysis across team members. Automatic priority adjustment based on due date proximity and dependency chains ensures critical path tasks surface appropriately. CSV and JSON export capabilities support external reporting dashboards.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill todoist-project-automator-api-v2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill todoist-project-automator-api-v2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill todoist-project-automator-api-v2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill todoist-project-automator-api-v2 -a codex
```

### OpenClaw

```bash
clawhub install todoist-project-automator-api-v2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/todoist-project-automator-api-v2/
