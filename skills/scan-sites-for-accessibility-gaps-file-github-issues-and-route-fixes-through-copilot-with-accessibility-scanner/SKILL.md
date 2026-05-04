---
title: "Scan sites for accessibility gaps, file GitHub issues, and route fixes through Copilot with Accessibility Scanner"
description: "Run accessibility scans against target URLs, open trackable issues, and optionally hand remediation suggestions to Copilot instead of treating accessibility review as a manual audit chore."
verification: "listed"
source: "https://github.com/github/accessibility-scanner"
author: "GitHub"
publisher_type: "organization"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "github/accessibility-scanner"
  github_stars: 266
---

# Scan sites for accessibility gaps, file GitHub issues, and route fixes through Copilot with Accessibility Scanner

Run accessibility scans against target URLs, open trackable issues, and optionally hand remediation suggestions to Copilot instead of treating accessibility review as a manual audit chore.

## Prerequisites

GitHub repository with Actions and Issues enabled, repository secret for a fine-grained PAT, list of target URLs, optional GitHub Copilot access for automated fix assignment

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Add the documented GitHub Actions workflow to the target repository, configure the required token secret and scan inputs, then run the action manually or on the chosen trigger to create issues from accessibility findings.
```

## Documentation

- https://github.com/github/accessibility-scanner

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-sites-for-accessibility-gaps-file-github-issues-and-route-fixes-through-copilot-with-accessibility-scanner/)
