---
title: "Run queued background coding sessions across GitHub, Slack, Linear, and webhooks with background-agents"
description: "Dispatch long-running coding work to background agents, check progress later, and pull reviewed outputs back into the main repo flow instead of babysitting one foreground session."
verification: "security_reviewed"
source: "https://github.com/ColeMurray/background-agents"
author: "Cole Murray"
publisher_type: "individual"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "ColeMurray/background-agents"
  github_stars: 1591
---

# Run queued background coding sessions across GitHub, Slack, Linear, and webhooks with background-agents

Dispatch long-running coding work to background agents, check progress later, and pull reviewed outputs back into the main repo flow instead of babysitting one foreground session.

## Prerequisites

GitHub App or repo access, deployed background-agents stack, sandbox infrastructure, supported model provider credentials, target repositories, and one or more trigger surfaces such as web UI, Slack, GitHub, Linear, or webhooks

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Follow the upstream setup and deployment docs for the control plane, sandbox runtime, and integrations, then connect a repository and trigger a background coding session from the web UI, Slack, GitHub, Linear, or an authenticated webhook.
```

## Documentation

- https://backgroundagents.dev

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-queued-background-coding-sessions-across-github-slack-linear-and-webhooks-with-background-agents/)
