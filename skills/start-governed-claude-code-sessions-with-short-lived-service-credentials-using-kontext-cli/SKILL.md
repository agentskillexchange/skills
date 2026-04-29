---
title: "Start governed Claude Code sessions with short-lived service credentials using Kontext CLI"
description: "Inject short-lived, scoped service credentials into Claude Code sessions so agents can reach approved systems without exposing raw secrets."
verification: "listed"
source: "https://github.com/kontext-security/kontext-cli"
author: "kontext-security"
publisher_type: "organization"
category:
  - "Security & Verification"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "kontext-security/kontext-cli"
  github_stars: 143
---

# Start governed Claude Code sessions with short-lived service credentials using Kontext CLI

Inject short-lived, scoped service credentials into Claude Code sessions so agents can reach approved systems without exposing raw secrets.

## Prerequisites

Claude Code, supported service accounts, browser login for first-run auth

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `brew install kontext-security/tap/kontext`, then run `kontext start --agent claude` from your project to authenticate, connect providers, inject short-lived credentials, and launch Claude Code.
```

## Documentation

- https://github.com/kontext-security/kontext-cli

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/start-governed-claude-code-sessions-with-short-lived-service-credentials-using-kontext-cli/)
