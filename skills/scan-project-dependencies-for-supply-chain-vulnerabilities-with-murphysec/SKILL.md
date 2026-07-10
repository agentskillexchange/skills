---
title: "Scan project dependencies for supply-chain vulnerabilities with MurphySec"
description: "Run MurphySec CLI against a project before release or dependency approval to detect vulnerable direct and transitive dependencies."
verification: "security_reviewed"
source: "https://github.com/murphysecurity/murphysec"
author: "MurphySecurity"
publisher_type: "Open-source vendor"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "murphysecurity/murphysec"
  github_stars: 1746
---

# Scan project dependencies for supply-chain vulnerabilities with MurphySec

Run MurphySec CLI against a project before release or dependency approval to detect vulnerable direct and transitive dependencies.

## Prerequisites

MurphySec CLI; MurphySec account access token for authentication

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Download a release from https://github.com/murphysecurity/murphysec/releases/latest or review and run the upstream installer for your OS, authenticate with `murphysec auth login` or `--token`, then scan with `murphysec scan [project-path] --json`.
```

## Documentation

- https://github.com/murphysecurity/murphysec

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-project-dependencies-for-supply-chain-vulnerabilities-with-murphysec/)
