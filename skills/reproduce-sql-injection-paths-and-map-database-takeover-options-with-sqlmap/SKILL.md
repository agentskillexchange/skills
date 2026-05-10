---
title: "Reproduce SQL injection paths and map database takeover options with sqlmap"
slug: "reproduce-sql-injection-paths-and-map-database-takeover-options-with-sqlmap"
description: "Take a suspected injectable request, replay it on an authorized target, confirm the finding, and enumerate reachable database actions before manual follow-up."
github_stars: 37104
verification: "security_reviewed"
source: "https://github.com/sqlmapproject/sqlmap"
author: "sqlmapproject"
publisher_type: "open_source_project"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "sqlmapproject/sqlmap"
  github_stars: 37104
---

# Reproduce SQL injection paths and map database takeover options with sqlmap

Take a suspected injectable request, replay it on an authorized target, confirm the finding, and enumerate reachable database actions before manual follow-up.

## Prerequisites

Python, authorized target URL or captured HTTP request, operator approval for security testing

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Clone the upstream repository or use a packaged install, then run sqlmap.py against an authorized request or URL.
```

## Documentation

- http://sqlmap.org

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/reproduce-sql-injection-paths-and-map-database-takeover-options-with-sqlmap/)
