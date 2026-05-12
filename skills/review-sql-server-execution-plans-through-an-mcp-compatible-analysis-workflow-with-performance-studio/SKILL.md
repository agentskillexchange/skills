---
title: "Review SQL Server execution plans through an MCP-compatible analysis workflow with Performance Studio"
slug: "review-sql-server-execution-plans-through-an-mcp-compatible-analysis-workflow-with-performance-studio"
description: "Use Performance Studio when an MCP-compatible agent needs to parse SQL Server .sqlplan files, surface performance warnings, inspect missing-index suggestions, and turn execution-plan evidence into a reviewable tuning workflow."
verification: "security_reviewed"
source: "https://github.com/erikdarlingdata/PerformanceStudio"
author: "Erik Darling Data"
publisher_type: "company"
category: "Runbooks & Diagnostics"
framework: "MCP"
tool_ecosystem:
  github_repo: "erikdarlingdata/PerformanceStudio"
  github_stars: 175
---

# Review SQL Server execution plans through an MCP-compatible analysis workflow with Performance Studio

Use Performance Studio when an MCP-compatible agent needs to parse SQL Server .sqlplan files, surface performance warnings, inspect missing-index suggestions, and turn execution-plan evidence into a reviewable tuning workflow.

## Prerequisites

Performance Studio via its built-in MCP server or CLI, plus SQL Server execution plan files or a reachable SQL Server environment.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Clone the repository or download a release from GitHub, then follow the README to run Performance Studio and enable its built-in MCP server or CLI workflow for execution-plan analysis.
```

## Documentation

- https://github.com/erikdarlingdata/PerformanceStudio

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/review-sql-server-execution-plans-through-an-mcp-compatible-analysis-workflow-with-performance-studio/)
