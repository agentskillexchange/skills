---
name: "MinerU PDF-to-Markdown Document Parser"
slug: "mineru-pdf-to-markdown-document-parser"
description: "Transforms complex PDFs into LLM-ready markdown and JSON using MinerU, a high-accuracy document intelligence pipeline. Extracts text, tables, formulas, and images from scientific papers, reports, and scanned documents with layout-aware parsing."
github_stars: 57814
verification: "security_reviewed"
source: "https://github.com/opendatalab/MinerU"
category: "Data Extraction & Transformation"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "opendatalab/MinerU"
  github_stars: 57814
---

# MinerU PDF-to-Markdown Document Parser

Transforms complex PDFs into LLM-ready markdown and JSON using MinerU, a high-accuracy document intelligence pipeline. Extracts text, tables, formulas, and images from scientific papers, reports, and scanned documents with layout-aware parsing.

## Installation

Use the upstream install or setup path that matches your environment:
- pip install --upgrade pip
- pip install uv
- uv pip install -U "mineru[all]"
- git clone https://github.com/opendatalab/MinerU.git

Requirements and caveats from upstream:
- [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mineru)](https://pypi.org/project/mineru/)
- | Development | Python / Go / TypeScript SDK · CLI · REST API · Docker |
- The official online version has the same functionality as the client, with a beautiful interface and rich features, requires login to use

Basic usage or getting-started notes:
- While maintaining high accuracy, it keeps resource usage extremely low and continues to support inference in pure CPU environments.
- Optimized the parsing pipeline with a sliding-window mechanism, significantly reducing peak memory usage in long-document scenarios, so documents with tens of thousands of pages no longer need to be split manually.
- This update is not just a set of feature enhancements, but a key leap forward in MinerU's overall system capabilities. We specifically addressed the peak memory usage issue in long-document parsing. Through optimizati...

- Source: https://github.com/opendatalab/MinerU
- Extracted from upstream docs: https://raw.githubusercontent.com/opendatalab/MinerU/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mineru-pdf-to-markdown-document-parser/)
