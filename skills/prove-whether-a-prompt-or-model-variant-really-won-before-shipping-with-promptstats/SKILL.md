---
name: "Prove whether a prompt or model variant really won before shipping with promptstats"
slug: "prove-whether-a-prompt-or-model-variant-really-won-before-shipping-with-promptstats"
description: "Run statistically sound comparisons on eval results so prompt and model changes are judged by confidence bounds, not bar-chart vibes."
github_stars: 97
verification: "security_reviewed"
source: "https://github.com/ianarawjo/promptstats"
author: "Ian Arawjo"
publisher_type: "individual"
category: "Code Quality & Review"
framework: "Multi-Framework"
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

Use the upstream install or setup path that matches your environment:
- pip install evalstats
- pip install "evalstats[xlsx]"
- pip install "evalstats[all]"
- pip install "evalstats[lmm]"

Requirements and caveats from upstream:
- If you set method="lmm", analyze() switches to a mixed-effects path (score ~ template + (1|input)) with Wald CIs and parametric rank distributions. By default this uses statsmodels (pure Python, no additional setup re...
- ## Python API
- evalstats main use case is as a Python API, which provides a similar entry point, the analyze() function. Simply pass your benchmark data in the correct format, and pass it to analyze to get a battery of results:

Basic usage or getting-started notes:
- What statistics test should I run in X situation?
- as well as example code (which will, obviously, tend to use evalstats, but
- Running estats.analyze() and then estats.print_analysis_summary(analysis) prints a full statistical report to the terminal, including confidence interval line plots, pairwise comparisons between prompt templates, and...

- Source: https://github.com/ianarawjo/promptstats
- Extracted from upstream docs: https://raw.githubusercontent.com/ianarawjo/promptstats/HEAD/README.md

## Documentation

- https://statsforevals.com

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prove-whether-a-prompt-or-model-variant-really-won-before-shipping-with-promptstats/)
