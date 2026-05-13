---
title: "SAST Pipeline Scanner"
slug: "sast-pipeline-scanner"
description: "Runs static application security testing using Semgrep rules and CodeQL queries against pull request diffs. Supports SARIF output format and integrates with GitHub Advanced Security for findings management."
github_stars: 14922
verification: "security_reviewed"
source: "https://github.com/semgrep/semgrep"
author: "Semgrep"
category: "Security & Verification"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "semgrep/semgrep"
  github_stars: 14922
---

# SAST Pipeline Scanner

Runs static application security testing using Semgrep rules and CodeQL queries against pull request diffs. Supports SARIF output format and integrates with GitHub Advanced Security for findings management.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
python3 -m pip install semgrep
```

## Documentation

- https://semgrep.dev/docs/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sast-pipeline-scanner/)
