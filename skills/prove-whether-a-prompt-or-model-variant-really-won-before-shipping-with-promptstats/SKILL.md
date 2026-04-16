---
title: "Prove whether a prompt or model variant really won before shipping with promptstats"
description: "Run statistically sound comparisons on eval results so prompt and model changes are judged by confidence bounds, not bar-chart vibes."
verification: "listed"
source: "https://github.com/ianarawjo/promptstats"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "ianarawjo/promptstats"
  github_stars: 97
  ase_npm_package: "promptstats"
  npm_weekly_downloads: 678
---

# Prove whether a prompt or model variant really won before shipping with promptstats

Use promptstats when the job is to analyze eval results and decide whether one prompt or model variant truly outperformed another, not when a user simply wants a generic benchmark dashboard. The operator workflow is crisp: feed in benchmark data, run the statistical analysis, inspect confidence bounds and pairwise comparisons, and decide whether the observed lift is real enough to act on. That scope boundary, statistical adjudication of prompt and model experiments, gives it a clear skill shape instead of reducing it to a plain library listing.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prove-whether-a-prompt-or-model-variant-really-won-before-shipping-with-promptstats/)
