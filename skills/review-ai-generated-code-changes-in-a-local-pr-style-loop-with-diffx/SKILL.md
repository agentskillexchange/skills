---
title: "Review AI-generated code changes in a local PR-style loop with DiffX"
slug: "review-ai-generated-code-changes-in-a-local-pr-style-loop-with-diffx"
description: "Use DiffX to review local git changes in a PR-style browser UI, leave inline comments, and hand structured feedback back to a coding agent for repair."
github_stars: 127
verification: "security_reviewed"
source: "https://github.com/wong2/diffx"
author: "wong2"
publisher_type: "individual"
category: "Code Quality & Review"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "wong2/diffx"
  github_stars: 127
---

# Review AI-generated code changes in a local PR-style loop with DiffX

Use DiffX to review local git changes in a PR-style browser UI, leave inline comments, and hand structured feedback back to a coding agent for repair.

## Prerequisites

git, diffx CLI, browser

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `npm install -g diffx-cli`. In any git repository run `diffx` to start the local review server and open the browser UI. You can also pass custom git diff arguments, for example `diffx -- HEAD~3` or `diffx -- --cached -- src/`.
```

## Documentation

- https://github.com/wong2/diffx

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/review-ai-generated-code-changes-in-a-local-pr-style-loop-with-diffx/)
