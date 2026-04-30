---
title: "Expose Haystack pipelines as webhook endpoints with Hayhooks"
description: "Turn an existing Haystack pipeline into an HTTP or MCP endpoint without building and maintaining a custom wrapper service."
verification: "listed"
source: "https://github.com/deepset-ai/hayhooks"
author: "deepset"
publisher_type: "organization"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "deepset-ai/hayhooks"
  github_stars: 138
---

# Expose Haystack pipelines as webhook endpoints with Hayhooks

Turn an existing Haystack pipeline into an HTTP or MCP endpoint without building and maintaining a custom wrapper service.

## Prerequisites

Python environment, Haystack pipeline definitions, hayhooks package, network access for HTTP serving, optional MCP clients

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install hayhooks in a Python environment, prepare the pipeline wrapper and pipeline definition files described upstream, then run the Hayhooks server and deploy the target pipeline as an endpoint.
```

## Documentation

- https://docs.haystack.deepset.ai/docs/hayhooks

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/expose-haystack-pipelines-as-webhook-endpoints-with-hayhooks/)
