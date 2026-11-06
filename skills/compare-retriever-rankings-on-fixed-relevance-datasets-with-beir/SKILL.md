---
name: "Compare retriever rankings on fixed relevance datasets with BEIR"
slug: "compare-retriever-rankings-on-fixed-relevance-datasets-with-beir"
description: "Compare baseline and candidate retrievers on the same labeled dataset, then hand off ranking metrics, saved runs and query-level regressions before a RAG retrieval change."
verification: "security_reviewed"
source: "https://github.com/beir-cellar/beir/blob/ef83d29307061c65d04b035b4f4e7c18bd8374af/README.md"
author: "BEIR contributors (beir-cellar)"
publisher_type: "community"
category: "Security & Verification"
framework: "Multi-Framework"
---

# Compare retriever rankings on fixed relevance datasets with BEIR

Compare baseline and candidate retrievers on the same labeled dataset, then hand off ranking metrics, saved runs and query-level regressions before a RAG retrieval change.

## Prerequisites

Python 3.9+, pip, BEIR, selected dataset and retriever dependencies; compute and disk space appropriate to the chosen model and corpus

## Installation

Install or set up from the source-backed instructions:

Create an isolated environment with python3 -m venv .venv, activate it, then run python -m pip install beir==2.2.0. Select a documented dataset and retriever from the upstream README, load a fixed split with GenericDataLoader, retrieve via EvaluateRetrieval, and export metrics and run files. Install only the dependencies required by the selected retriever; model and dataset downloads are separate.

- Source: https://github.com/beir-cellar/beir/blob/ef83d29307061c65d04b035b4f4e7c18bd8374af/README.md

## Documentation

- https://github.com/beir-cellar/beir/blob/ef83d29307061c65d04b035b4f4e7c18bd8374af/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/compare-retriever-rankings-on-fixed-relevance-datasets-with-beir/)
