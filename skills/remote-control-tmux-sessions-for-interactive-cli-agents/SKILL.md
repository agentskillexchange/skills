---
title: "Remote-control tmux sessions for interactive CLI agents"
description: "Lets an agent drive existing tmux sessions by sending keystrokes and scraping pane output, which is exactly what you need for interactive CLIs that cannot be handled as one-shot shell commands. Use it for session supervision and intervention, not for general terminal automation or starting new background jobs."
verification: "security_reviewed"
source: "https://github.com/openclaw/skills/tree/main/skills/steipete/tmux"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
---

# Remote-control tmux sessions for interactive CLI agents

Lets an agent drive existing tmux sessions by sending keystrokes and scraping pane output, which is exactly what you need for interactive CLIs that cannot be handled as one-shot shell commands. Use it for session supervision and intervention, not for general terminal automation or starting new background jobs.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/remote-control-tmux-sessions-for-interactive-cli-agents/)
