---
title: "Evaluate document parsers for agent ingestion with ParseBench"
description: "Use ParseBench to run repeatable document-parser evaluations before an agent relies on PDF, table, chart, or enterprise-document output for downstream decisions."
verification: "security_reviewed"
source: "https://github.com/run-llama/ParseBench"
author: "LlamaIndex"
publisher_type: "open_source"
category:
  - "Data Extraction & Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "run-llama/ParseBench"
  github_stars: 474
---

# Evaluate document parsers for agent ingestion with ParseBench

Use ParseBench to run repeatable document-parser evaluations before an agent relies on PDF, table, chart, or enterprise-document output for downstream decisions.

## Prerequisites

Python, uv, ParseBench runners, parser or model provider credentials for the selected pipeline

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
git clone https://github.com/run-llama/ParseBench.git && cd ParseBench && uv sync --extra runners
```

## Documentation

- https://github.com/run-llama/ParseBench

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/evaluate-document-parsers-for-agent-ingestion-with-parsebench/)
