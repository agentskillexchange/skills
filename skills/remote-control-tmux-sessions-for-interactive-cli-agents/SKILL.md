---
title: "Remote-control tmux sessions for interactive CLI agents"
description: "This entry is built around the tmux skill in the openclaw/skills repository. The agent behavior is precise: inspect existing tmux sessions, capture recent pane output, send text or control keys, and steer interactive terminal applications such as Claude Code, Codex, or other long-running TUIs. That makes the unit of value a concrete operator workflow, not a catalog card for tmux itself. Use this when a user needs an agent to monitor or intervene in an already-running interactive CLI session. It is the right invocation when a plain shell command is not enough because the target process expects prompts, confirmations, navigation, or iterative input over time. In practice that means checking whether a coding agent is waiting for approval, reading the tail of a pane for status, or sending follow-up instructions without attaching manually. The scope boundary keeps this from collapsing into a generic tmux or CLI listing. It is not a terminal multiplexer review, not a general process manager, and not a replacement for normal shell execution. The skill is specifically about controlling live tmux-backed sessions where interaction and screen scraping are the job. One-off commands should still use direct execution tools, and starting brand-new background processes belongs elsewhere. Integration points include tmux session names, pane targeting, capture-pane output, send-keys flows, and agent orchestration patterns that rely on persistent interactive sessions. It fits naturally into runbooks, coding-agent supervision, and diagnostics workflows."
source: "https://github.com/openclaw/skills/tree/main/skills/steipete/tmux"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "openclaw/skills"
  github_stars: 4086
---

# Remote-control tmux sessions for interactive CLI agents

This entry is built around the tmux skill in the openclaw/skills repository. The agent behavior is precise: inspect existing tmux sessions, capture recent pane output, send text or control keys, and steer interactive terminal applications such as Claude Code, Codex, or other long-running TUIs. That makes the unit of value a concrete operator workflow, not a catalog card for tmux itself. Use this when a user needs an agent to monitor or intervene in an already-running interactive CLI session. It is the right invocation when a plain shell command is not enough because the target process expects prompts, confirmations, navigation, or iterative input over time. In practice that means checking whether a coding agent is waiting for approval, reading the tail of a pane for status, or sending follow-up instructions without attaching manually. The scope boundary keeps this from collapsing into a generic tmux or CLI listing. It is not a terminal multiplexer review, not a general process manager, and not a replacement for normal shell execution. The skill is specifically about controlling live tmux-backed sessions where interaction and screen scraping are the job. One-off commands should still use direct execution tools, and starting brand-new background processes belongs elsewhere. Integration points include tmux session names, pane targeting, capture-pane output, send-keys flows, and agent orchestration patterns that rely on persistent interactive sessions. It fits naturally into runbooks, coding-agent supervision, and diagnostics workflows.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/remote-control-tmux-sessions-for-interactive-cli-agents/)
