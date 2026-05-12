---
title: "Search large PDFs and read only the relevant pages before answering"
slug: "search-large-pdfs-and-read-only-the-relevant-pages-before-answering"
description: "Use pdf-mcp to inspect a PDF, search it, and load only the pages that matter so an agent can answer questions from long documents without brute-forcing the whole file into context."
verification: "security_reviewed"
source: "https://github.com/jztan/pdf-mcp"
author: "jztan"
publisher_type: "individual"
category: "Data Extraction & Transformation"
framework: "MCP"
tool_ecosystem:
  github_repo: "jztan/pdf-mcp"
  github_stars: 17
---

# Search large PDFs and read only the relevant pages before answering

Use pdf-mcp to inspect a PDF, search it, and load only the pages that matter so an agent can answer questions from long documents without brute-forcing the whole file into context.

## Prerequisites

Python 3.10+; an MCP-compatible client; local PDFs or accessible PDF URLs; optional extra dependencies for semantic search.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
<p>Install with <code>pip install pdf-mcp</code>, or use <code>pip install 'pdf-mcp[semantic]'</code> to enable local embedding-based semantic search. Then add it to your MCP client with a command such as <code>claude mcp add pdf-mcp -- pdf-mcp</code>, and use the info, search, TOC, and page-read tools to inspect the document before loading content into the model.</p>
```

## Documentation

- https://github.com/jztan/pdf-mcp

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/search-large-pdfs-and-read-only-the-relevant-pages-before-answering/)
