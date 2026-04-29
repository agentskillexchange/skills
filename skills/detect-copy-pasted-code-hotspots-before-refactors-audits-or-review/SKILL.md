---
title: "Detect copy-pasted code hotspots before refactors, audits, or review"
description: "Use jscpd when an agent needs to scan a codebase for duplicated blocks and turn clone findings into a focused cleanup or review queue. The skill is about duplication detection and hotspot reporting, not general linting, testing, or automated refactoring by itself."
verification: "security_reviewed"
source: "https://www.npmjs.com/package/jscpd"
author: "Andrey Kucherenko"
publisher_type: "Individual Maintainer"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  npm_package: "jscpd"
  npm_weekly_downloads: 703581
---

# Detect copy-pasted code hotspots before refactors, audits, or review

Use jscpd when an agent needs to scan a codebase for duplicated blocks and turn clone findings into a focused cleanup or review queue. The skill is about duplication detection and hotspot reporting, not general linting, testing, or automated refactoring by itself.

## Prerequisites

Node.js and npm

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
npm install -g jscpd
```

## Documentation

- https://github.com/kucherenko/jscpd#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/detect-copy-pasted-code-hotspots-before-refactors-audits-or-review/)
