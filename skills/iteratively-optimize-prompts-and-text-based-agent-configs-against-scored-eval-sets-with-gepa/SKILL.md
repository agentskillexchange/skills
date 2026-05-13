---
title: "Iteratively optimize prompts and text-based agent configs against scored eval sets with GEPA"
slug: "iteratively-optimize-prompts-and-text-based-agent-configs-against-scored-eval-sets-with-gepa"
description: "Use reflective search to improve prompts or text-configured agent components against a real eval set instead of manual prompt tweaking."
github_stars: 3550
verification: "security_reviewed"
source: "https://github.com/gepa-ai/gepa"
author: "GEPA AI"
publisher_type: "organization"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "gepa-ai/gepa"
  github_stars: 3550
  npm_package: "gepa"
  npm_weekly_downloads: 4095897
---

# Iteratively optimize prompts and text-based agent configs against scored eval sets with GEPA

Use reflective search to improve prompts or text-configured agent components against a real eval set instead of manual prompt tweaking.

## Prerequisites

Python environment, GEPA package, train and validation examples with a scoring function, model provider credentials or local models, target prompt or text configuration to optimize

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install GEPA with pip install gepa, prepare a scored train and validation set plus a seed candidate, then run the documented optimize flow or DSPy integration to generate and compare improved candidates.
```

## Documentation

- https://gepa-ai.github.io/gepa/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/iteratively-optimize-prompts-and-text-based-agent-configs-against-scored-eval-sets-with-gepa/)
