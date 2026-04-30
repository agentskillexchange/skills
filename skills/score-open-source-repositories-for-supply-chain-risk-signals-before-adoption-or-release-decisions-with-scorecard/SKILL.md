---
title: "Score open source repositories for supply-chain risk signals before adoption or release decisions with Scorecard"
description: "Check a repository against OpenSSF security heuristics before you trust it as a dependency, approve it for use, or ship from it."
verification: "listed"
source: "https://github.com/ossf/scorecard"
author: "OpenSSF"
publisher_type: "organization"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "ossf/scorecard"
  github_stars: 5376
---

# Score open source repositories for supply-chain risk signals before adoption or release decisions with Scorecard

Check a repository against OpenSSF security heuristics before you trust it as a dependency, approve it for use, or ship from it.

## Prerequisites

Scorecard CLI or GitHub Action, network access to the target repository host, and optional GitHub authentication for higher API limits.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Scorecard from the upstream release, package, or action path documented at scorecard.dev, then run it against the target repository URL or dependency list and review the reported checks before adoption or release work proceeds.
```

## Documentation

- https://scorecard.dev

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/score-open-source-repositories-for-supply-chain-risk-signals-before-adoption-or-release-decisions-with-scorecard/)
