---
title: "Remote-control tmux sessions for interactive CLI agents"
description: "Lets an agent drive existing tmux sessions by sending keystrokes and scraping pane output, which is exactly what you need for interactive CLIs that cannot be handled as one-shot shell commands. Use it for session supervision and intervention, not for general terminal automation or starting new background jobs."
slug: "remote-control-tmux-sessions-for-interactive-cli-agents"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://github.com/openclaw/skills/tree/main/skills/steipete/tmux"
---

# Remote-control tmux sessions for interactive CLI agents

Lets an agent drive existing tmux sessions by sending keystrokes and scraping pane output, which is exactly what you need for interactive CLIs that cannot be handled as one-shot shell commands. Use it for session supervision and intervention, not for general terminal automation or starting new background jobs.

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
clawhub install remote-control-tmux-sessions-for-interactive-cli-agents
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This entry is built around the tmux skill in the openclaw/skills repository. The agent behavior is precise: inspect existing tmux sessions, capture recent pane output, send text or control keys, and steer interactive terminal applications such as Claude Code, Codex, or other long-running TUIs. That makes the unit of value a concrete operator workflow, not a catalog card for tmux itself.
Use this when a user needs an agent to monitor or intervene in an already-running interactive CLI session. It is the right invocation when a plain shell command is not enough because the target process expects prompts, confirmations, navigation, or iterative input over time. In practice that means checking whether a coding agent is waiting for approval, reading the tail of a pane for status, or sending follow-up instructions without attaching manually.
The scope boundary keeps this from collapsing into a generic tmux or CLI listing. It is not a terminal multiplexer review, not a general process manager, and not a replacement for normal shell execution. The skill is specifically about controlling live tmux-backed sessions where interaction and screen scraping are the job. One-off commands should still use direct execution tools, and starting brand-new background processes belongs elsewhere.
Integration points include tmux session names, pane targeting, capture-pane output, send-keys flows, and agent orchestration patterns that rely on persistent interactive sessions. It fits naturally into runbooks, coding-agent supervision, and diagnostics workflows.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/remote-control-tmux-sessions-for-interactive-cli-agents/)
