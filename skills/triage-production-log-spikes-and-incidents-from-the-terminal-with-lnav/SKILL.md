---
title: "Triage production log spikes and incidents from the terminal with lnav"
description: "Open raw logs, jump to error clusters, query structured fields, and summarize incident clues without shipping data to a separate platform."
verification: "listed"
source: "https://github.com/tstack/lnav"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "tstack/lnav"
  github_stars: 10159
---

# Triage production log spikes and incidents from the terminal with lnav

Use lnav when an agent needs to investigate raw log files during an incident instead of guessing from `tail` output. The agent can open mixed log sources, pivot on structured fields, jump straight to error bursts, and summarize what changed around the spike. The scope is terminal-first incident triage on existing logs, not generic observability hosting or log-platform administration.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/triage-production-log-spikes-and-incidents-from-the-terminal-with-lnav/)
