---
name: "Turn documents into validated knowledge graphs with Docling Graph"
slug: "turn-documents-into-validated-knowledge-graphs-with-docling-graph"
description: "Convert documents into schema-enforced entities and graph relationships when the job is exact knowledge extraction rather than generic document parsing."
github_stars: 134
verification: "listed"
source: "https://github.com/docling-project/docling-graph"
author: "docling-project"
publisher_type: "organization"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "docling-project/docling-graph"
  github_stars: 134
---

# Turn documents into validated knowledge graphs with Docling Graph

Convert documents into schema-enforced entities and graph relationships when the job is exact knowledge extraction rather than generic document parsing.

## Prerequisites

Python 3.10+, docling-graph package, source documents supported by Docling, optional model provider credentials for remote LLM extraction

## Installation

Use the upstream install or setup path that matches your environment:
- pip install docling-graph
- git clone https://github.com/docling-project/docling-graph
- uv sync --extra dev
- uv run pre-commit run --all-files

Requirements and caveats from upstream:
- [![Python 3.10 | 3.11 | 3.12](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/downloads/)
- Python 3.10 or higher
- # Convert document from URL (each line except the last must end with \)

Basic usage or getting-started notes:
- **✍🏻 Input formats:** [Docling](https://docling-project.github.io/docling/usage/supported_formats/)’s supported inputs: PDF, images, markdown, Office, HTML, and more.
- **📐 Structured extraction:** LLM output is schema-enforced by default; see [CLI](docs/usage/cli/convert-command.md#structured-output-mode) and [API](docs/usage/api/llm-model-config.md) to disable.
- **🐛 Trace capture:** [Debug exports](docs/usage/advanced/trace-data-debugging.md) for extraction and fallback diagnostics.

- Source: https://github.com/docling-project/docling-graph
- Extracted from upstream docs: https://raw.githubusercontent.com/docling-project/docling-graph/HEAD/README.md

## Documentation

- https://docling-project.github.io/docling-graph/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/turn-documents-into-validated-knowledge-graphs-with-docling-graph/)
