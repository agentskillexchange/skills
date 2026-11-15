---
name: "Run client delivery fieldwork with FDEOps"
slug: "run-client-delivery-fieldwork-with-fdeops"
description: "Use FDEOps to guide agent-assisted client work from discovery through build, QA, readout, and handoff while preserving local evidence and decisions."
github_stars: 536
verification: "security_reviewed"
source: "https://github.com/suboss87/FDEOps"
author: "suboss87"
publisher_type: "individual"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "suboss87/FDEOps"
  github_stars: 536
  npm_package: "fdeops"
  npm_weekly_downloads: 2274
---

# Run client delivery fieldwork with FDEOps

Use FDEOps to guide agent-assisted client work from discovery through build, QA, readout, and handoff while preserving local evidence and decisions.

## Prerequisites

Node.js 18+; Git; FDEOps CLI or skill pack; supported skill host such as Claude Code, Cursor, Codex, or another agent; local client engagement folder

## Installation

Install or set up from the source-backed instructions:

Run npx fdeops scan to inspect a checkout, then install the main skill with npx skills add suboss87/fdeops --skill fde. For a single task, install a narrower skill such as npx skills add suboss87/fdeops --skill fde-integrate. For Codex/offline setup, run npx fdeops resume --init client01 from the client workspace when needed.

- Source: https://github.com/suboss87/FDEOps

## Documentation

- https://github.com/suboss87/FDEOps/tree/main/docs

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-client-delivery-fieldwork-with-fdeops/)
