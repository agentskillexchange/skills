---
title: "Scan LLM systems for jailbreaks, prompt injections, and unsafe behaviors with garak"
description: "Probe a model or agent stack with adversarial test suites so safety failures show up before deployment or review."
verification: "listed"
source: "https://github.com/NVIDIA/garak"
author: "NVIDIA"
publisher_type: "organization"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "NVIDIA/garak"
  github_stars: 7549
---

# Scan LLM systems for jailbreaks, prompt injections, and unsafe behaviors with garak

Probe a model or agent stack with adversarial test suites so safety failures show up before deployment or review.

## Prerequisites

Python 3.10+, target LLM or API credentials, command line access

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `python -m pip install -U garak`, configure access to the target model or provider, then run garak with the generator and probe options that match the system you want to assess.
```

## Documentation

- https://garak.ai

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-llm-systems-for-jailbreaks-prompt-injections-and-unsafe-behaviors-with-garak/)
