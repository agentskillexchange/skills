---
name: "PubMed Literature Mining Agent"
description: "Queries the NCBI E-utilities API (esearch, efetch, elink) to retrieve PubMed biomedical literature, extracting MeSH terms, citation networks, and full-text links from PubMed Central via the PMC OAI-PMH service."
category: "Research & Scraping"
framework: "Gemini"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/pubmed-literature-mining-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "prisma"  # from ase_tool_match
  github_stars: 45585  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 9355280  # from ase_npm_downloads
  github_repo: "prisma/prisma"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# PubMed Literature Mining Agent

Queries the NCBI E-utilities API (esearch, efetch, elink) to retrieve PubMed biomedical literature, extracting MeSH terms, citation networks, and full-text links from PubMed Central via the PMC OAI-PMH service.

## Overview

The PubMed Literature Mining Agent automates biomedical literature research by interfacing with NCBI E-utilities APIs for comprehensive publication discovery and analysis. The esearch endpoint handles complex Boolean queries across PubMed’s 35+ million citations, supporting MeSH term expansion, date range filtering, and publication type restrictions. Retrieved article metadata is fetched via efetch in XML format, extracting structured fields including author affiliations, grant funding sources, and conflict of interest declarations. Citation network analysis uses elink to map forward and backward citations, identifying seminal papers and emerging research trends within specific domains. Full-text access is resolved through PubMed Central’s OAI-PMH service for open access articles, enabling paragraph-level text extraction for systematic review workflows. The agent constructs PRISMA-compliant search documentation, recording exact queries, database dates, and result counts for reproducible literature reviews. MeSH term analysis identifies concept relationships and suggests query refinements based on the MeSH tree hierarchy. Batch processing handles large result sets with proper API rate limiting and NCBI API key authentication for elevated request quotas.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pubmed-literature-mining-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pubmed-literature-mining-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pubmed-literature-mining-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pubmed-literature-mining-agent -a codex
```

### OpenClaw

```bash
clawhub install pubmed-literature-mining-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/pubmed-literature-mining-agent/
