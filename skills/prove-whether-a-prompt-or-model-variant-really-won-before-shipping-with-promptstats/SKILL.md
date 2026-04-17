---
title: "Prove whether a prompt or model variant really won before shipping with promptstats"
description: "Use promptstats when the job is to analyze eval results and decide whether one prompt or model variant truly outperformed another, not when a user simply wants a generic benchmark dashboard. The operator workflow is crisp: feed in benchmark data, run the statistical analysis, inspect confidence bounds and pairwise comparisons, and decide whether the observed lift is real enough to act on. That scope boundary, statistical adjudication of prompt and model experiments, gives it a clear skill shape instead of reducing it to a plain library listing."
verification: listed
source: "https://github.com/ianarawjo/promptstats"
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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prove-whether-a-prompt-or-model-variant-really-won-before-shipping-with-promptstats
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/prove-whether-a-prompt-or-model-variant-really-won-before-shipping-with-promptstats` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prove-whether-a-prompt-or-model-variant-really-won-before-shipping-with-promptstats/)
