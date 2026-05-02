---
title: "PubMed Literature Mining Agent"
description: "Queries the NCBI E-utilities API (esearch, efetch, elink) to retrieve PubMed biomedical literature, extracting MeSH terms, citation networks, and full-text links from PubMed Central via the PMC OAI-PMH service."
verification: "security_reviewed"
source: "https://pubmed.ncbi.nlm.nih.gov/"
category:
  - "Research & Scraping"
framework:
  - "Gemini"
---

# PubMed Literature Mining Agent

The PubMed Literature Mining Agent automates biomedical literature research by interfacing with NCBI E-utilities APIs for comprehensive publication discovery and analysis. The esearch endpoint handles complex Boolean queries across PubMed’s 35+ million citations, supporting MeSH term expansion, date range filtering, and publication type restrictions. Retrieved article metadata is fetched via efetch in XML format, extracting structured fields including author affiliations, grant funding sources, and conflict of interest declarations. Citation network analysis uses elink to map forward and backward citations, identifying seminal papers and emerging research trends within specific domains. Full-text access is resolved through PubMed Central’s OAI-PMH service for open access articles, enabling paragraph-level text extraction for systematic review workflows. The agent constructs PRISMA-compliant search documentation, recording exact queries, database dates, and result counts for reproducible literature reviews. MeSH term analysis identifies concept relationships and suggests query refinements based on the MeSH tree hierarchy. Batch processing handles large result sets with proper API rate limiting and NCBI API key authentication for elevated request quotas.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/pubmed-literature-mining-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/pubmed-literature-mining-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/pubmed-literature-mining-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pubmed-literature-mining-agent/)
