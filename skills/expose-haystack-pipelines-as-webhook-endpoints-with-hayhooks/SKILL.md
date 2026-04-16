---
title: "Expose Haystack pipelines as webhook endpoints with Hayhooks"
description: "Turn an existing Haystack pipeline into an HTTP or MCP endpoint without building and maintaining a custom wrapper service."
verification: "listed"
source: "https://github.com/deepset-ai/hayhooks"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "deepset-ai/hayhooks"
  github_stars: 138
---

# Expose Haystack pipelines as webhook endpoints with Hayhooks

Use Hayhooks when an agent already has a Haystack pipeline and needs to serve it through HTTP, webhook-style, OpenAI-compatible, or MCP endpoints for other systems to call. The user is not invoking a generic AI platform here. The workflow is narrow: wrap a pipeline, deploy it, and expose a documented endpoint surface for handoffs. That scope boundary, serving existing Haystack pipelines as callable endpoints, keeps it distinct from a plain library or framework listing.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/expose-haystack-pipelines-as-webhook-endpoints-with-hayhooks/)
