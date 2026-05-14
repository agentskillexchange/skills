---
title: "Generate and iterate on a local codebase from a natural-language spec with gpt-engineer"
slug: "generate-and-iterate-on-a-local-codebase-from-a-natural-language-spec-with-gpt-engineer"
description: "Use gpt-engineer when an agent/operator needs to turn a prompt file into a local project scaffold, inspect the generated code, and run a supervised improvement loop before adopting the result."
github_stars: 55220
verification: "security_reviewed"
source: "https://github.com/AntonOsika/gpt-engineer"
author: "AntonOsika / gpt-engineer community"
publisher_type: "open_source"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "AntonOsika/gpt-engineer"
  github_stars: 55220
---

# Generate and iterate on a local codebase from a natural-language spec with gpt-engineer

Use gpt-engineer when an agent/operator needs to turn a prompt file into a local project scaffold, inspect the generated code, and run a supervised improvement loop before adopting the result.

## Prerequisites

Python, pip, OpenAI-compatible or supported model API key, gpte CLI

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `python -m pip install gpt-engineer`; set an API key such as `OPENAI_API_KEY`; create a project folder with a `prompt` file; run `gpte <project_dir>` or `gpte <project_dir> -i` for improvement mode.
```

## Documentation

- https://gpt-engineer.readthedocs.io/en/latest/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-and-iterate-on-a-local-codebase-from-a-natural-language-spec-with-gpt-engineer/)
