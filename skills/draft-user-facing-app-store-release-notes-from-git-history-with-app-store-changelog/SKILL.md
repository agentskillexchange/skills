---
title: "Draft user-facing App Store release notes from git history with App Store Changelog"
description: "Turn commits since the last tag into concise App Store What’s New bullets instead of hand-sifting raw git history."
verification: "security_reviewed"
source: "https://github.com/Dimillian/Skills/tree/main/app-store-changelog"
author: "Dimillian"
publisher_type: "individual"
category:
  - "Templates & Workflows"
framework:
  - "Codex"
---

# Draft user-facing App Store release notes from git history with App Store Changelog

Turn commits since the last tag into concise App Store What’s New bullets instead of hand-sifting raw git history.

## Prerequisites

Codex skills directory, a Git repository with tags or refs, shell access to run the included collection script

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Place the app-store-changelog folder under $CODEX_HOME/skills, then run the documented collect_release_changes.sh flow from the target repository and draft the final App Store bullets from the gathered git range.
```

## Documentation

- https://raw.githubusercontent.com/Dimillian/Skills/main/app-store-changelog/SKILL.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/draft-user-facing-app-store-release-notes-from-git-history-with-app-store-changelog/)
