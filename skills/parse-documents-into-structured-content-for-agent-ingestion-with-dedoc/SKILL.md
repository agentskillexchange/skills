---
title: "Parse documents into structured content for agent ingestion with Dedoc"
description: "Extract document text, tables, logical structure, and metadata into normalized output before RAG, review, or workflow automation."
verification: "security_reviewed"
source: "https://github.com/ispras/dedoc"
author: "ISP RAS"
publisher_type: "organization"
category:
  - "Data Extraction & Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "ispras/dedoc"
  github_stars: 712
---

# Parse documents into structured content for agent ingestion with Dedoc

Extract document text, tables, logical structure, and metadata into normalized output before RAG, review, or workflow automation.

## Prerequisites

Dedoc Docker service or Python library, source documents

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Run the published Docker image with `docker run -p 1231:1231 --rm dedocproject/dedoc python3 /dedoc_root/dedoc/main.py`, or install the Python package from the upstream project and call Dedoc from the parsing workflow.
```

## Documentation

- https://dedoc.readthedocs.io/en/latest/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parse-documents-into-structured-content-for-agent-ingestion-with-dedoc/)
