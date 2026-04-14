---
title: "Remote-control tmux sessions for interactive CLI agents"
description: "Lets an agent drive existing tmux sessions by sending keystrokes and scraping pane output, which is exactly what you need for interactive CLIs that cannot be handled as one-shot shell commands. Use it for session supervision and intervention, not for general terminal automation or starting new background jobs."
verification: security_reviewed
source: "https://github.com/openclaw/skills/tree/main/skills/steipete/tmux"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "openclaw/skills"
  github_stars: 4086
---

# Remote-control tmux sessions for interactive CLI agents

This entry is built around the tmux skill in the openclaw/skills repository. The agent behavior is precise: inspect existing tmux sessions, capture recent pane output, send text or control keys, and steer interactive terminal applications such as Claude Code, Codex, or other long-running TUIs. That makes the unit of value a concrete operator workflow, not a catalog card for tmux itself.

Use this when a user needs an agent to monitor or intervene in an already-running interactive CLI session. It is the right invocation when a plain shell command is not enough because the target process expects prompts, confirmations, navigation, or iterative input over time. In practice that means checking whether a coding agent is waiting for approval, reading the tail of a pane for status, or sending follow-up instructions without attaching manually.

The scope boundary keeps this from collapsing into a generic tmux or CLI listing. It is not a terminal multiplexer review, not a general process manager, and not a replacement for normal shell execution. The skill is specifically about controlling live tmux-backed sessions where interaction and screen scraping are the job. One-off commands should still use direct execution tools, and starting brand-new background processes belongs elsewhere.

Integration points include tmux session names, pane targeting, capture-pane output, send-keys flows, and agent orchestration patterns that rely on persistent interactive sessions. It fits naturally into runbooks, coding-agent supervision, and diagnostics workflows.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/remote-control-tmux-sessions-for-interactive-cli-agents/)
