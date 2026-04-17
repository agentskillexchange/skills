---
title: "Search large PDFs and read only the relevant pages before answering"
description: "This skill gives an agent a bounded PDF-reading workflow: inspect document metadata first, run keyword or semantic search to find the right pages, then read those pages in manageable chunks with extracted text, tables, images, and table-of-contents data. It is especially useful for annual reports, technical manuals, contracts, and other long PDFs where loading the full document would waste context or hide the relevant evidence.\nThe scope boundary is clear: this is not a generic document platform listing and not just a raw parser card. The job-to-be-done is targeted PDF retrieval and page-scoped reading for downstream reasoning. Invoke it when the agent needs to navigate, search, and cite specific PDF sections efficiently, not when you want a broad document ETL stack or a whole knowledge-base platform."
verification: security_reviewed
source: "https://github.com/jztan/pdf-mcp"
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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/search-large-pdfs-and-read-only-the-relevant-pages-before-answering
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/search-large-pdfs-and-read-only-the-relevant-pages-before-answering` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/search-large-pdfs-and-read-only-the-relevant-pages-before-answering/)
