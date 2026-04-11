---
title: "Gate pull requests on OpenAPI breaking changes"
description: "Use oasdiff when an agent needs to compare old and new OpenAPI specs and decide whether a proposed change is safe to merge. The skill turns spec drift into a concrete breaking-change report that can block CI or annotate review workflows."
verification: "security_reviewed"
source: "https://github.com/oasdiff/oasdiff"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "oasdiff/oasdiff"
  github_stars: 1145
---

# Gate pull requests on OpenAPI breaking changes

Use oasdiff when an agent needs to compare old and new OpenAPI specs and decide whether a proposed change is safe to merge. The skill turns spec drift into a concrete breaking-change report that can block CI or annotate review workflows.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gate-pull-requests-on-openapi-breaking-changes/)
