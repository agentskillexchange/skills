---
title: "Test documentation sites across mobile, tablet, and desktop with GitHub Agentic Workflows"
slug: "test-documentation-sites-across-mobile-tablet-and-desktop-with-github-agentic-workflows"
description: "Run a repeatable docs-site check that builds locally, opens the site across device sizes, and reports layout, accessibility, and interaction issues."
verification: "security_reviewed"
source: "https://github.com/github/gh-aw/blob/v0.45.5/.github/workflows/daily-multi-device-docs-tester.md"
author: "GitHub"
publisher_type: "organization"
category: "Templates & Workflows"
framework: "Multi-Framework"
---

# Test documentation sites across mobile, tablet, and desktop with GitHub Agentic Workflows

Run a repeatable docs-site check that builds locally, opens the site across device sizes, and reports layout, accessibility, and interaction issues.

## Prerequisites

GitHub repository with docs build scripts, GitHub Actions, gh-aw, Playwright MCP tooling available through the workflow runtime

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install and configure gh-aw in the target repository, add the daily-multi-device-docs-tester workflow, compile the workflow with gh aw compile, then run it on schedule or via workflow_dispatch against the repository docs site.
```

## Documentation

- https://raw.githubusercontent.com/github/gh-aw/v0.45.5/.github/workflows/daily-multi-device-docs-tester.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/test-documentation-sites-across-mobile-tablet-and-desktop-with-github-agentic-workflows/)
