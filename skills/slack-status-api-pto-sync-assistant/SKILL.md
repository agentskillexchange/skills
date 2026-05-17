---
name: "Slack Status API PTO Sync Assistant"
slug: "slack-status-api-pto-sync-assistant"
description: "Syncs away-state updates through Slack users.profile APIs, status fields, and directory lookups so agents can keep status text aligned with calendar-based time off. Useful for teams that want cleaner presence signals without manually editing every Slack profile."
verification: "security_reviewed"
source: "https://api.slack.com/"
author: "Slack"
category: "Calendar, Email & Productivity"
framework: "Custom Agents"
---

# Slack Status API PTO Sync Assistant

Syncs away-state updates through Slack users.profile APIs, status fields, and directory lookups so agents can keep status text aligned with calendar-based time off. Useful for teams that want cleaner presence signals without manually editing every Slack profile.

## Prerequisites

Slack workspace, Slack app, and the required user profile or status scopes

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Create a Slack app, grant the required scopes, install it to your workspace, then call the Slack Web API endpoints documented at the source URL.
```

## Documentation

- https://api.slack.com/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-status-api-pto-sync-assistant/)
