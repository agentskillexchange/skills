---
title: "Track coding-agent quota burn and remaining headroom across providers with onWatch"
description: "Monitor quota, spend, resets, and alerts across multiple coding-agent providers from one local dashboard before a long run hits throttling or budget limits."
verification: "listed"
source: "https://github.com/onllm-dev/onWatch"
author: "onllm-dev"
publisher_type: "organization"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "onllm-dev/onWatch"
  github_stars: 580
---

# Track coding-agent quota burn and remaining headroom across providers with onWatch

Monitor quota, spend, resets, and alerts across multiple coding-agent providers from one local dashboard before a long run hits throttling or budget limits.

## Prerequisites

onWatch binary or Homebrew install, local shell access, provider credentials for one or more supported services, and optional browser access for the local dashboard

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install onWatch with the upstream curl installer or Homebrew, run onwatch setup to configure provider credentials, then start onwatch before or during long coding-agent runs to monitor quota headroom and alerts.
```

## Documentation

- https://onwatch.onllm.dev

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/track-coding-agent-quota-burn-and-remaining-headroom-across-providers-with-onwatch/)
