---
title: "Run security audits and variant analysis workflows in Claude Code with Trail of Bits Skills"
description: "Use curated Trail of Bits security skills inside Claude Code when the job is auditing, variant hunting, or fix verification rather than generic coding assistance."
verification: "listed"
source: "https://github.com/trailofbits/skills"
author: "Trail of Bits"
publisher_type: "company"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "trailofbits/skills"
  github_stars: 4663
---

# Run security audits and variant analysis workflows in Claude Code with Trail of Bits Skills

Use curated Trail of Bits security skills inside Claude Code when the job is auditing, variant hunting, or fix verification rather than generic coding assistance.

## Prerequisites

Claude Code with plugin marketplace support, the Trail of Bits skills repository or marketplace install, and whatever upstream tools a selected security skill requires such as Semgrep, CodeQL, SARIF tooling, Burp exports, or language-specific analyzers.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Add the marketplace with /plugin marketplace add trailofbits/skills, then install the needed skill from the plugin menu or by name. For Codex-native use, clone the repository and run the documented .codex install script so the sidecar skills tree becomes available locally.
```

## Documentation

- https://github.com/trailofbits/skills#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-security-audits-and-variant-analysis-workflows-in-claude-code-with-trail-of-bits-skills/)
