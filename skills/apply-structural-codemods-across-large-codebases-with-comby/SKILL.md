---
title: "Apply structural codemods across large codebases with Comby"
description: "Rewrite recurring code patterns with syntax-aware matching so agents can run migration codemods more safely than plain regex search and replace."
verification: "listed"
source: "https://github.com/comby-tools/comby"
author: "comby-tools"
publisher_type: "organization"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "comby-tools/comby"
  github_stars: 2626
---

# Apply structural codemods across large codebases with Comby

Rewrite recurring code patterns with syntax-aware matching so agents can run migration codemods more safely than plain regex search and replace.

## Prerequisites

Comby CLI

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Comby from the release binaries or package manager for your platform, then run a match and rewrite pair such as `comby 'old(:[x])' 'new(:[x])' -matcher .python -i`.
```

## Documentation

- https://comby.dev/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apply-structural-codemods-across-large-codebases-with-comby/)
