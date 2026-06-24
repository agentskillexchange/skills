---
name: "Generate validated analytics SQL with SQLCoder"
slug: "generate-validated-analytics-sql-with-sqlcoder"
description: "Use SQLCoder when an analytics agent needs to turn natural-language questions plus schema context into SQL drafts that can be reviewed, validated, and run inside a controlled data workflow."
github_stars: 4035
verification: "security_reviewed"
source: "https://github.com/defog-ai/sqlcoder"
author: "Defog"
publisher_type: "company"
category: "Data Extraction & Transformation"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "defog-ai/sqlcoder"
  github_stars: 4035
---

# Generate validated analytics SQL with SQLCoder

Use SQLCoder when an analytics agent needs to turn natural-language questions plus schema context into SQL drafts that can be reviewed, validated, and run inside a controlled data workflow.

## Prerequisites

Python environment, SQLCoder package or Hugging Face model weights, schema metadata for the target database, and a controlled database execution or review path.

## Installation

Use the upstream install or setup path that matches your environment:
- pip install "sqlcoder[transformers]"
- pip install "sqlcoder[llama-cpp]"

Requirements and caveats from upstream:
- python inference.py -q "Question about the sample database goes here"

Basic usage or getting-started notes:
- If running on a non-apple silicon computer without GPU access, please run this on Linux/Intel Mac
- And run this on Windows
- In your terminal, run

- Source: https://github.com/defog-ai/sqlcoder
- Extracted from upstream docs: https://raw.githubusercontent.com/defog-ai/sqlcoder/HEAD/README.md

## Documentation

- https://github.com/defog-ai/sqlcoder

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-validated-analytics-sql-with-sqlcoder/)
