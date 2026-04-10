---
name: Remote-control tmux sessions for interactive CLI agents
description: Lets an agent drive existing tmux sessions by sending keystrokes and
  scraping pane output, which is exactly what you need for interactive CLIs that cannot
  be handled as one-shot shell commands. Use it for session supervision and intervention,
  not for general terminal automation or starting new background jobs.
verification: security_reviewed
source: https://github.com/openclaw/skills/tree/main/skills/steipete/tmux
category:
- Runbooks &amp; Diagnostics
framework:
- OpenClaw
---
# Remote-control tmux sessions for interactive CLI agents

This entry is built around the tmux skill in the openclaw/skills repository. The agent behavior is precise: inspect existing tmux sessions, capture recent pane output, send text or control keys, and steer interactive terminal applications such as Claude Code, Codex, or other long-running TUIs. That makes the unit of value a concrete operator workflow, not a catalog card for tmux itself.
Use this when a user needs an agent to monitor or intervene in an already-running interactive CLI session. It is the right invocation when a plain shell command is not enough because the target process expects prompts, confirmations, navigation, or iterative input over time. In practice that means checking whether a coding agent is waiting for approval, reading the tail of a pane for status, or sending follow-up instructions without attaching manually.
The scope boundary keeps this from collapsing into a generic tmux or CLI listing. It is not a terminal multiplexer review, not a general process manager, and not a replacement for normal shell execution. The skill is specifically about controlling live tmux-backed sessions where interaction and screen scraping are the job. One-off commands should still use direct execution tools, and starting brand-new background processes belongs elsewhere.
Integration points include tmux session names, pane targeting, capture-pane output, send-keys flows, and agent orchestration patterns that rely on persistent interactive sessions. It fits naturally into runbooks, coding-agent supervision, and diagnostics workflows.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/remote-control-tmux-sessions-for-interactive-cli-agents/)
