---
title: "Turn Lark meeting transcripts into action items and follow-up tasks"
description: "Read a Lark Minutes transcript, extract explicit and implied follow-ups, then let the agent execute selected tasks instead of leaving them as notes."
verification: "security_reviewed"
source: "https://github.com/zarazhangrui/lark-minutes-tasks"
category:
  - "Calendar, Email & Productivity"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "zarazhangrui/lark-minutes-tasks"
  github_stars: 40
---

# Turn Lark meeting transcripts into action items and follow-up tasks

Lark Minutes Tasks is a post-meeting execution workflow. The agent reads a Lark Minutes transcript or notes document, extracts explicit and implied action items, lets the user choose which ones matter, and then carries out the selected follow-up work. Invoke this when the meeting transcript is the handoff artifact and you want the agent to turn discussion into concrete next actions, messages, documents, research, or calendar follow-through. That is different from using Lark Minutes normally, because the transcript is not the end product here, it is the trigger for execution. The boundary is narrow: transcript-to-task extraction and follow-up execution from Lark meeting records. It is not a generic meeting platform listing and not a broad productivity suite card.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/turn-lark-meeting-transcripts-into-action-items-and-follow-up-tasks/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/turn-lark-meeting-transcripts-into-action-items-and-follow-up-tasks
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/turn-lark-meeting-transcripts-into-action-items-and-follow-up-tasks`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/turn-lark-meeting-transcripts-into-action-items-and-follow-up-tasks/)
