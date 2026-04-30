---
title: "Run reviewable multi-step codemod workflows with Codemod CLI"
description: "Use Codemod CLI when an agent needs to scaffold, test, and run a reviewable multi-step migration workflow with approval gates, rather than applying a one-off search-and-replace or browsing the hosted Codemod platform."
verification: "security_reviewed"
source: "https://github.com/codemod/codemod"
author: "Codemod"
publisher_type: "company"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "codemod/codemod"
  github_stars: 979
---

# Run reviewable multi-step codemod workflows with Codemod CLI

Use Codemod CLI when an agent needs to scaffold, test, and run a reviewable multi-step migration workflow with approval gates, rather than applying a one-off search-and-replace or browsing the hosted Codemod platform.

## Prerequisites

Node.js, npm or npx access, target repository, workflow YAML or codemod package

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Use `npx codemod` or the documented package install method, scaffold or select a codemod workflow, then run `npx codemod workflow run -w workflow.yaml` locally or in CI to execute the migration.
```

## Documentation

- https://docs.codemod.com/cli

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-reviewable-multi-step-codemod-workflows-with-codemod-cli/)
