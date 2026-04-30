---
title: "Drive dependency and config bumps through declarative Updatecli pipelines"
description: "Use Updatecli when an agent needs to detect upstream releases, validate conditions, patch versioned files, and open reviewable update actions from one policy run instead of hand-editing manifests or relying on a single ecosystem bot."
verification: "security_reviewed"
source: "https://github.com/updatecli/updatecli"
author: "Updatecli contributors"
publisher_type: "open_source_project"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "updatecli/updatecli"
  github_stars: 894
---

# Drive dependency and config bumps through declarative Updatecli pipelines

Use Updatecli when an agent needs to detect upstream releases, validate conditions, patch versioned files, and open reviewable update actions from one policy run instead of hand-editing manifests or relying on a single ecosystem bot.

## Prerequisites

Updatecli binary, YAML policy file, access to the repositories or files you want to update

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Updatecli from the documented release or package method, write an updatecli YAML policy, then run `updatecli apply --config updatecli.yaml` against the target repository or workspace.
```

## Documentation

- https://www.updatecli.io

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/drive-dependency-and-config-bumps-through-declarative-updatecli-pipelines/)
