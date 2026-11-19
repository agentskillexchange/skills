---
name: "Review Master CSS output regressions through MCP snapshots"
slug: "review-master-css-output-regressions-through-mcp-snapshots"
description: "Capture project CSS snapshots, trace missing classes, compare generated output, and propose scoped fixes with evidence from the installed Master CSS compiler."
github_stars: 1957
verification: "security_reviewed"
source: "https://github.com/master-co/css"
author: "Aoyue Design LLC."
publisher_type: "organization"
category: "Code Quality & Review"
framework: "MCP"
tool_ecosystem:
  github_repo: "master-co/css"
  github_stars: 1957
  npm_package: "@master/css-mcp"
  npm_weekly_downloads: 2286
---

# Review Master CSS output regressions through MCP snapshots

Capture project CSS snapshots, trace missing classes, compare generated output, and propose scoped fixes with evidence from the installed Master CSS compiler.

## Prerequisites

Node.js 24+, @master/css-mcp 2.1.4, MCP client supporting stdio, authorized Master CSS project and lockfile

## Installation

Install or set up from the source-backed instructions:

Use Node.js 24+. In the authorized Master CSS project, install npm install -D --save-exact @master/css-mcp@2.1.4 and retain the lockfile. Configure the MCP client's stdio command as the absolute project-local node_modules/.bin/master-css-mcp executable, with args ["--root", "/absolute/path/to/project"]. Upstream also supports npx -y @master/css-mcp@2.1.4 --root /absolute/path/to/project. Inspect workspace package and compiler versions before using project tools.

- Source: https://github.com/master-co/css

## Documentation

- https://github.com/master-co/css/blob/main/packages/mcp/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/review-master-css-output-regressions-through-mcp-snapshots/)
