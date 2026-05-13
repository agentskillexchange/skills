---
title: "Filter prompts and model outputs for injection, secrets, toxicity, and policy risks with LLM Guard"
slug: "filter-prompts-and-model-outputs-for-injection-secrets-toxicity-and-policy-risks-with-llm-guard"
description: "Screen prompts and responses with input and output scanners before an LLM interaction reaches production users or downstream systems."
github_stars: 2831
verification: "security_reviewed"
source: "https://github.com/protectai/llm-guard"
author: "Protect AI"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "protectai/llm-guard"
  github_stars: 2831
---

# Filter prompts and model outputs for injection, secrets, toxicity, and policy risks with LLM Guard

Screen prompts and responses with input and output scanners before an LLM interaction reaches production users or downstream systems.

## Prerequisites

Python 3.9+, application or agent code that can wrap LLM input and output handling

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `pip install llm-guard`, choose the input and output scanners that match your risk profile, and wrap those checks around prompt submission and response handling in your LLM workflow.
```

## Documentation

- https://protectai.github.io/llm-guard/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/filter-prompts-and-model-outputs-for-injection-secrets-toxicity-and-policy-risks-with-llm-guard/)
