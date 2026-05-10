---
title: "Wrap local coding agents in deny-by-default least-privilege sandboxes with Greywall"
slug: "wrap-local-coding-agents-in-deny-by-default-least-privilege-sandboxes-with-greywall"
description: "Run Claude Code, Codex, Cursor, or similar local agent CLIs inside a host-local sandbox that learns required access and blocks everything else by default."
github_stars: 158
verification: "security_reviewed"
source: "https://github.com/GreyhavenHQ/greywall"
author: "GreyhavenHQ"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "GreyhavenHQ/greywall"
  github_stars: 158
---

# Wrap local coding agents in deny-by-default least-privilege sandboxes with Greywall

Run Claude Code, Codex, Cursor, or similar local agent CLIs inside a host-local sandbox that learns required access and blocks everything else by default.

## Prerequisites

Greywall CLI, local shell access, a supported local coding agent such as Claude Code, Codex, Cursor, Aider, Gemini CLI, or OpenCode, Linux or macOS host

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Greywall with the documented Homebrew, install script, or Go flow, verify platform dependencies with greywall check, then launch the target agent through Greywall and optionally use learning mode to generate a least-privilege profile.
```

## Documentation

- https://docs.greywall.io/greywall/platform-support

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wrap-local-coding-agents-in-deny-by-default-least-privilege-sandboxes-with-greywall/)
