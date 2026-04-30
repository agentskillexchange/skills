---
title: "Preflight agent specs for prompt-injection risk across prompt, tool, and architecture layers with Prompt Hardener"
description: "Describe an agent in `agent_spec.yaml`, run deterministic prompt-injection analysis, generate mitigations, and validate defenses before rollout."
verification: "listed"
source: "https://github.com/cybozu/prompt-hardener"
author: "Cybozu"
publisher_type: "organization"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "cybozu/prompt-hardener"
  github_stars: 50
---

# Preflight agent specs for prompt-injection risk across prompt, tool, and architecture layers with Prompt Hardener

Describe an agent in `agent_spec.yaml`, run deterministic prompt-injection analysis, generate mitigations, and validate defenses before rollout.

## Prerequisites

Python 3, pipx or uv optional

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install from the published wheel with `pipx install https://github.com/cybozu/prompt-hardener/releases/download/v0.6.0/prompt_hardener-0.6.0-py3-none-any.whl` or use `uv tool install ...`, copy or write `agent_spec.yaml`, then run `prompt-hardener validate agent_spec.yaml` and `prompt-hardener analyze agent_spec.yaml`.
```

## Documentation

- https://github.com/cybozu/prompt-hardener

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/preflight-agent-specs-for-prompt-injection-risk-across-prompt-tool-and-architecture-layers-with-prompt-hardener/)
