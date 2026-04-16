---
title: "Search large PDFs and read only the relevant pages before answering"
description: "Use pdf-mcp to inspect a PDF, search it, and load only the pages that matter so an agent can answer questions from long documents without brute-forcing the whole file into context."
verification: "security_reviewed"
source: "https://github.com/jztan/pdf-mcp"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "jztan/pdf-mcp"
  github_stars: 17
---

# Search large PDFs and read only the relevant pages before answering

This skill gives an agent a bounded PDF-reading workflow: inspect document metadata first, run keyword or semantic search to find the right pages, then read those pages in manageable chunks with extracted text, tables, images, and table-of-contents data. It is especially useful for annual reports, technical manuals, contracts, and other long PDFs where loading the full document would waste context or hide the relevant evidence.

The scope boundary is clear: this is not a generic document platform listing and not just a raw parser card. The job-to-be-done is targeted PDF retrieval and page-scoped reading for downstream reasoning. Invoke it when the agent needs to navigate, search, and cite specific PDF sections efficiently, not when you want a broad document ETL stack or a whole knowledge-base platform.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/search-large-pdfs-and-read-only-the-relevant-pages-before-answering/)
