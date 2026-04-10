---
title: "PubMed Literature Mining Agent"
description: "Queries the NCBI E-utilities API (esearch, efetch, elink) to retrieve PubMed biomedical literature, extracting MeSH terms, citation networks, and full-text links from PubMed Central via the PMC OAI-PMH service."
slug: "pubmed-literature-mining-agent"
category:
  - "Research &amp; Scraping"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://pubmed.ncbi.nlm.nih.gov/"
---

# PubMed Literature Mining Agent

Queries the NCBI E-utilities API (esearch, efetch, elink) to retrieve PubMed biomedical literature, extracting MeSH terms, citation networks, and full-text links from PubMed Central via the PMC OAI-PMH service.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install pubmed-literature-mining-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The PubMed Literature Mining Agent automates biomedical literature research by interfacing with NCBI E-utilities APIs for comprehensive publication discovery and analysis. The esearch endpoint handles complex Boolean queries across PubMed’s 35+ million citations, supporting MeSH term expansion, date range filtering, and publication type restrictions. Retrieved article metadata is fetched via efetch in XML format, extracting structured fields including author affiliations, grant funding sources, and conflict of interest declarations. Citation network analysis uses elink to map forward and backward citations, identifying seminal papers and emerging research trends within specific domains. Full-text access is resolved through PubMed Central’s OAI-PMH service for open access articles, enabling paragraph-level text extraction for systematic review workflows. The agent constructs PRISMA-compliant search documentation, recording exact queries, database dates, and result counts for reproducible literature reviews. MeSH term analysis identifies concept relationships and suggests query refinements based on the MeSH tree hierarchy. Batch processing handles large result sets with proper API rate limiting and NCBI API key authentication for elevated request quotas.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pubmed-literature-mining-agent/)
