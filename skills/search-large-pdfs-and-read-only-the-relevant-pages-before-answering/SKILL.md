---
title: "Search large PDFs and read only the relevant pages before answering"
description: "This skill gives an agent a bounded PDF-reading workflow: inspect document metadata first, run keyword or semantic search to find the right pages, then read those pages in manageable chunks with extracted text, tables, images, and table-of-contents data. It is especially useful for annual reports, technical manuals, contracts, and other long PDFs where loading the full document would waste context or hide the relevant evidence. The scope boundary is clear: this is not a generic document platform listing and not just a raw parser card. The job-to-be-done is targeted PDF retrieval and page-scoped reading for downstream reasoning. Invoke it when the agent needs to navigate, search, and cite specific PDF sections efficiently, not when you want a broad document ETL stack or a whole knowledge-base platform."
source: "https://github.com/jztan/pdf-mcp"
verification: "security_reviewed"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "jztan/pdf-mcp"
  github_stars: 17
---

# Search large PDFs and read only the relevant pages before answering

This skill gives an agent a bounded PDF-reading workflow: inspect document metadata first, run keyword or semantic search to find the right pages, then read those pages in manageable chunks with extracted text, tables, images, and table-of-contents data. It is especially useful for annual reports, technical manuals, contracts, and other long PDFs where loading the full document would waste context or hide the relevant evidence. The scope boundary is clear: this is not a generic document platform listing and not just a raw parser card. The job-to-be-done is targeted PDF retrieval and page-scoped reading for downstream reasoning. Invoke it when the agent needs to navigate, search, and cite specific PDF sections efficiently, not when you want a broad document ETL stack or a whole knowledge-base platform.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/search-large-pdfs-and-read-only-the-relevant-pages-before-answering/)
