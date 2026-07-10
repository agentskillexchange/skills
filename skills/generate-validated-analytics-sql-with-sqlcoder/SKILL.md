---
title: "Generate validated analytics SQL with SQLCoder"
description: "Use SQLCoder when an analytics agent needs to turn natural-language questions plus schema context into SQL drafts that can be reviewed, validated, and run inside a controlled data workflow."
verification: "security_reviewed"
source: "https://github.com/defog-ai/sqlcoder"
author: "Defog"
publisher_type: "company"
category:
  - "Data Extraction & Transformation"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "defog-ai/sqlcoder"
  github_stars: 4035
---

# Generate validated analytics SQL with SQLCoder

Use SQLCoder when an analytics agent needs to turn natural-language questions plus schema context into SQL drafts that can be reviewed, validated, and run inside a controlled data workflow.

## Prerequisites

Python environment, SQLCoder package or Hugging Face model weights, schema metadata for the target database, and a controlled database execution or review path.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install SQLCoder in a Python environment with the hardware-specific extra from the README, for example sqlcoder[transformers] on a supported NVIDIA GPU or sqlcoder[llama-cpp] for llama.cpp backends. Launch SQLCoder or call the inference script with schema metadata, then validate generated SQL before allowing the agent to execute it.
```

## Documentation

- https://github.com/defog-ai/sqlcoder

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-validated-analytics-sql-with-sqlcoder/)
