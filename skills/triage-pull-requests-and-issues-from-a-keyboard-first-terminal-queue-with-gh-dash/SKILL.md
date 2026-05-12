---
title: "Triage pull requests and issues from a keyboard-first terminal queue with gh-dash"
slug: "triage-pull-requests-and-issues-from-a-keyboard-first-terminal-queue-with-gh-dash"
description: "Use gh-dash when an agent or operator needs assigned pull requests and issue queues in a keyboard-first terminal dashboard instead of bouncing across GitHub tabs."
verification: "security_reviewed"
source: "https://github.com/dlvhdr/gh-dash"
author: "Dolev Hadar"
publisher_type: "individual"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "dlvhdr/gh-dash"
  github_stars: 11340
---

# Triage pull requests and issues from a keyboard-first terminal queue with gh-dash

Use gh-dash when an agent or operator needs assigned pull requests and issue queues in a keyboard-first terminal dashboard instead of bouncing across GitHub tabs.

## Prerequisites

GitHub CLI authenticated against the target account, terminal access, and optionally a Nerd Font if you want the full dashboard visuals.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
<p>Install the GitHub CLI first, then run <code>gh extension install dlvhdr/gh-dash</code>. Launch the dashboard with <code>gh dash</code> and optionally add a Nerd Font plus a YAML config to define the PR and issue sections you want to triage.</p>
```

## Documentation

- https://www.gh-dash.dev/getting-started

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/triage-pull-requests-and-issues-from-a-keyboard-first-terminal-queue-with-gh-dash/)
