---
title: PubMed Literature Mining Agent
description: The PubMed Literature Mining Agent automates biomedical literature research
  by interfacing with NCBI E-utilities APIs for comprehensive publication discovery
  and analysis. The esearch endpoint handles complex Boolean queries across PubMed’s
  35+ million citations, supporting MeSH term expansion, date range filtering, and
  publication type restrictions. Retrieved article metadata is fetched via efetch
  in XML format, extracting structured fields including author affiliations, grant
  funding sources, and conflict of interest declarations. Citation network analysis
  uses elink to map forward and backward citations, identifying seminal papers and
  emerging research trends within specific domains. Full-text access is resolved through
  PubMed Central’s OAI-PMH service for open access articles, enabling paragraph-level
  text extraction for systematic review workflows. The agent constructs PRISMA-compliant
  search documentation, recording exact queries, database dates, and result counts
  for reproducible literature reviews. MeSH term analysis identifies concept relationships
  and suggests query refinements based on the MeSH tree hierarchy. Batch processing
  handles large result sets with proper API rate limiting and NCBI API key authentication
  for elevated request quotas.
verification: security_reviewed
source: https://pubmed.ncbi.nlm.nih.gov/
category:
- Research &amp; Scraping
framework:
- Gemini
---

# PubMed Literature Mining Agent

The PubMed Literature Mining Agent automates biomedical literature research by interfacing with NCBI E-utilities APIs for comprehensive publication discovery and analysis. The esearch endpoint handles complex Boolean queries across PubMed’s 35+ million citations, supporting MeSH term expansion, date range filtering, and publication type restrictions. Retrieved article metadata is fetched via efetch in XML format, extracting structured fields including author affiliations, grant funding sources, and conflict of interest declarations. Citation network analysis uses elink to map forward and backward citations, identifying seminal papers and emerging research trends within specific domains. Full-text access is resolved through PubMed Central’s OAI-PMH service for open access articles, enabling paragraph-level text extraction for systematic review workflows. The agent constructs PRISMA-compliant search documentation, recording exact queries, database dates, and result counts for reproducible literature reviews. MeSH term analysis identifies concept relationships and suggests query refinements based on the MeSH tree hierarchy. Batch processing handles large result sets with proper API rate limiting and NCBI API key authentication for elevated request quotas.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pubmed-literature-mining-agent/)
