---
name: "Keep agent retrieval current as documents change with Serviette"
slug: "keep-agent-retrieval-current-as-documents-change-with-serviette"
description: "Configure a watched document corpus, serve source-backed retrieval to agents, and verify that additions, edits, and deletions reach the index without manual re-ingestion."
github_stars: 58791
verification: "security_reviewed"
source: "https://github.com/pathwaycom/serviette"
author: "Pathway / Serviette contributors"
publisher_type: "community"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "pathwaycom/serviette"
  github_stars: 58791
---

# Keep agent retrieval current as documents change with Serviette

Configure a watched document corpus, serve source-backed retrieval to agents, and verify that additions, edits, and deletions reach the index without manual re-ingestion.

## Prerequisites

Python 3.10+; pip 23.1+; Serviette CLI; required Pathway license key; selected embedding backend and vector store; HTTP-capable agent

## Installation

Install or set up from the source-backed instructions:

Create an isolated Python environment, use pip 23.1+, and run python -m pip install 'serviette[local]'. Obtain a free Pathway license key through the upstream license page and set PATHWAY_LICENSE_KEY. Run serviette wizard, choose the document folder, local embeddings and DuckDB, and then serviette up --config config.yaml. Use the upstream CPU PyTorch wheel option if appropriate for the host. Configure optional model credentials only if generated answers or remote embeddings are needed. Query POST /api/v1/retrieve with query and k; test a controlled file edit and deletion before relying on freshness.

- Source: https://github.com/pathwaycom/serviette

## Documentation

- https://github.com/pathwaycom/serviette/blob/main/docs/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/keep-agent-retrieval-current-as-documents-change-with-serviette/)
