---
name: "Assemble PR verification evidence with Roam Guard"
slug: "assemble-pr-verification-evidence-with-roam-guard"
description: "Collect a branch’s Roam analysis evidence into a strict local PR verdict, with explicit required checks, missing evidence and reviewer handoff."
github_stars: 516
verification: "security_reviewed"
source: "https://github.com/Cranot/roam-code/tree/2a12e418b10866ae26ee16d34d283f4aa394a745"
author: "Cranot"
publisher_type: "community"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "Cranot/roam-code"
  github_stars: 516
---

# Assemble PR verification evidence with Roam Guard

Collect a branch’s Roam analysis evidence into a strict local PR verdict, with explicit required checks, missing evidence and reviewer handoff.

## Prerequisites

Python 3.11+, Git 2.24+, uv, roam-code 14.2.3, project test tools

## Installation

Install or set up from the source-backed instructions:

Install Python 3.11+ and Git 2.24+. In an isolated tool environment run: uv tool install "roam-code==14.2.3". Select the intended Git checkout, then run roam index to build its local index. First use may download a parser bundle. Review the pinned adoption guide before initializing a branch-specific evidence bundle. MCP extras, agent hooks, CI files and GitHub credentials are unnecessary for this local CLI workflow.

- Source: https://github.com/Cranot/roam-code/tree/2a12e418b10866ae26ee16d34d283f4aa394a745

## Documentation

- https://github.com/Cranot/roam-code/blob/2a12e418b10866ae26ee16d34d283f4aa394a745/templates/examples/roam-guard-pr.README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/assemble-pr-verification-evidence-with-roam-guard/)
