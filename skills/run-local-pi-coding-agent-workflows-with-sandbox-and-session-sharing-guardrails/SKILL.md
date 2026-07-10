---
title: "Run local Pi coding-agent workflows with sandbox and session-sharing guardrails"
description: "Use Pi when an operator needs a local coding-agent CLI with explicit sandboxing, provider setup, and reviewable session artifacts."
verification: "listed"
source: "https://github.com/earendil-works/pi"
author: "Earendil Works"
publisher_type: "organization"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "earendil-works/pi"
  github_stars: 63139
  npm_package: "@earendil-works/pi-coding-agent"
  npm_weekly_downloads: 5666680
---

# Run local Pi coding-agent workflows with sandbox and session-sharing guardrails

Use Pi when an operator needs a local coding-agent CLI with explicit sandboxing, provider setup, and reviewable session artifacts.

## Prerequisites

Pi coding-agent CLI, configured LLM provider credentials, target repository, optional Docker/OpenShell/Gondolin sandbox

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the @earendil-works/pi-coding-agent package from npm, configure the intended model provider, run Pi from the target repository, and apply the documented containerization or sandbox pattern before allowing broad filesystem or shell access.
```

## Documentation

- https://pi.dev/docs/latest

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-local-pi-coding-agent-workflows-with-sandbox-and-session-sharing-guardrails/)
