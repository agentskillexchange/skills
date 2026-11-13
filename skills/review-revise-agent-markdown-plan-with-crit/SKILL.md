---
name: "Review and revise an agent-authored Markdown plan with Crit"
slug: "review-revise-agent-markdown-plan-with-crit"
description: "Open a local Markdown plan for line-level human comments, return the feedback to the agent, and repeat the revision loop until the operator approves."
github_stars: 1301
verification: "security_reviewed"
source: "https://github.com/tomasz-tomczyk/crit"
author: "tomasz-tomczyk"
publisher_type: "Community"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "tomasz-tomczyk/crit"
  github_stars: 1301
---

# Review and revise an agent-authored Markdown plan with Crit

Open a local Markdown plan for line-level human comments, return the feedback to the agent, and repeat the revision loop until the operator approves.

## Prerequisites

Crit binary; local Markdown plan; agent able to read files and run commands; local browser for the operator

## Installation

Install or set up from the source-backed instructions:

Install the reviewed Crit v0.23.2 binary from https://github.com/tomasz-tomczyk/crit/releases/tag/v0.23.2 for your operating system and place it on PATH. Run crit plan.md in the project. Use the upstream integration matching your agent, or manually return the review prompt to the agent after reviewing. No remote sharing or account is required for this local workflow.

- Source: https://github.com/tomasz-tomczyk/crit

## Documentation

- https://github.com/tomasz-tomczyk/crit/blob/4458cced170c23dde92070c12758f5942048359a/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/review-revise-agent-markdown-plan-with-crit/)
