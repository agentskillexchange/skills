---
title: "Track coding-agent quota burn and remaining headroom across providers with onWatch"
description: "Monitor quota, spend, resets, and alerts across multiple coding-agent providers from one local dashboard before a long run hits throttling or budget limits."
verification: "listed"
source: "https://github.com/onllm-dev/onWatch"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "onllm-dev/onWatch"
  github_stars: 580
---

# Track coding-agent quota burn and remaining headroom across providers with onWatch

Use onWatch when an operator needs a single preflight and in-run view of quota burn across coding-agent providers, not when they are simply using one provider dashboard normally. The invoke moment is concrete: before or during a long coding-agent run, poll provider usage endpoints, store history, surface remaining headroom, and alert before throttling or overage hits. That scope boundary, cross-provider quota and usage monitoring for coding-agent operations, makes this publishable as a skill instead of a generic LLM product or dashboard listing.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/track-coding-agent-quota-burn-and-remaining-headroom-across-providers-with-onwatch/)
