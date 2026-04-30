---
title: "Regression-test prompts, agents, and RAG outputs before shipping changes"
description: "Use promptfoo when an agent needs to evaluate prompt, agent, or RAG behavior against saved assertions before a change goes live. The value here is the repeatable evaluation workflow, not a generic AI tooling catalog entry."
verification: "security_reviewed"
source: "https://github.com/promptfoo/promptfoo"
author: "promptfoo"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "promptfoo/promptfoo"
  github_stars: 20007
---

# Regression-test prompts, agents, and RAG outputs before shipping changes

Use promptfoo when an agent needs to evaluate prompt, agent, or RAG behavior against saved assertions before a change goes live. The value here is the repeatable evaluation workflow, not a generic AI tooling catalog entry.

## Prerequisites

Node.js, CI pipeline, model provider credentials

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install promptfoo, define evaluation cases and assertions in config files, then run local or CI evaluations against prompts, agents, or RAG flows before merging changes.
```

## Documentation

- https://www.promptfoo.dev/docs/intro/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/regression-test-prompts-agents-and-rag-outputs-before-shipping-changes/)
