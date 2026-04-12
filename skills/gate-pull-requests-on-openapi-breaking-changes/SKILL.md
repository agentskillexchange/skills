---
title: "Gate pull requests on OpenAPI breaking changes"
description: "Use oasdiff when an agent needs to compare old and new OpenAPI specs and decide whether a proposed change is safe to merge. The skill turns spec drift into a concrete breaking-change report that can block CI or annotate review workflows."
verification: security_reviewed
source: "https://github.com/oasdiff/oasdiff"
---

# Gate pull requests on OpenAPI breaking changes

Use oasdiff when an agent needs to compare old and new OpenAPI specs and decide whether a proposed change is safe to merge. The skill turns spec drift into a concrete breaking-change report that can block CI or annotate review workflows.

## Installation

Choose the path that fits your setup:

1. Clone this repository and use the skill locally.
2. Copy the skill folder into your local skills directory.
3. Add the skill as a Git submodule in your skills workspace.
4. Vendor the files into an internal skill catalog for your team.
5. Reference the upstream source and recreate the skill in your own agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gate-pull-requests-on-openapi-breaking-changes/)
