---
title: "Triage pull requests and issues from a keyboard-first terminal queue with gh-dash"
description: "Use gh-dash when an agent or operator needs assigned pull requests and issue queues in a keyboard-first terminal dashboard instead of bouncing across GitHub tabs."
verification: "security_reviewed"
source: "https://github.com/dlvhdr/gh-dash"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "dlvhdr/gh-dash"
  github_stars: 11340
---

# Triage pull requests and issues from a keyboard-first terminal queue with gh-dash

gh-dash gives an agent a bounded GitHub triage workflow inside the terminal. It organizes pull requests and issues into configurable sections, lets the user inspect diffs and comments, and keeps common queue-clearing actions close to the keyboard. That makes it useful when the job is reviewing incoming work, not authoring a whole new GitHub automation stack.

The boundary is narrow enough to be skill-shaped after one rewrite. Invoke it when an agent needs a terminal queue for PR and issue triage, review, or handoff, not when the user wants GitHub as a general platform listing or a full repository automation framework. The job-to-be-done is keyboard-first GitHub work-item triage.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/triage-pull-requests-and-issues-from-a-keyboard-first-terminal-queue-with-gh-dash/)
