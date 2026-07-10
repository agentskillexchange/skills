---
title: "Prove whether a prompt or model variant really won before shipping with promptstats"
description: "Run statistically sound comparisons on eval results so prompt and model changes are judged by confidence bounds, not bar-chart vibes."
verification: "security_reviewed"
source: "https://github.com/ianarawjo/promptstats"
author: "Ian Arawjo"
publisher_type: "individual"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "ianarawjo/promptstats"
  github_stars: 97
  npm_package: "promptstats"
  npm_weekly_downloads: 678
---

# Prove whether a prompt or model variant really won before shipping with promptstats

Run statistically sound comparisons on eval results so prompt and model changes are judged by confidence bounds, not bar-chart vibes.

## Prerequisites

Python environment, promptstats package, eval result tables or per-input score arrays, prompt or model experiment outputs to compare

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install promptstats from the upstream Python package instructions, format your eval results into the documented input shape, then run the analysis methods and review the generated statistical report before making rollout decisions.
```

## Documentation

- https://statsforevals.com

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prove-whether-a-prompt-or-model-variant-really-won-before-shipping-with-promptstats/)
