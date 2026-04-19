---
title: "PubMed Literature Mining Agent"
description: "The PubMed Literature Mining Agent automates biomedical literature research by interfacing with NCBI E-utilities APIs for comprehensive publication discovery and analysis. The esearch endpoint handles complex Boolean queries across PubMed&#8217;s 35+ million citations, supporting MeSH term expansion, date range filtering, and publication type restrictions. Retrieved article metadata is fetched via efetch in XML format, extracting structured fields including author affiliations, grant funding sources, and conflict of interest declarations. Citation network analysis uses elink to map forward and backward citations, identifying seminal papers and emerging research trends within specific domains. Full-text access is resolved through PubMed Central&#8217;s OAI-PMH service for open access articles, enabling paragraph-level text extraction for systematic review workflows. The agent constructs PRISMA-compliant search documentation, recording exact queries, database dates, and result counts for reproducible literature reviews. MeSH term analysis identifies concept relationships and suggests query refinements based on the MeSH tree hierarchy. Batch processing handles large result sets with proper API rate limiting and NCBI API key authentication for elevated request quotas."
source: "https://pubmed.ncbi.nlm.nih.gov/"
verification: "security_reviewed"
category:
  - "Research &amp; Scraping"
framework:
  - "Gemini"
---

# PubMed Literature Mining Agent

The PubMed Literature Mining Agent automates biomedical literature research by interfacing with NCBI E-utilities APIs for comprehensive publication discovery and analysis. The esearch endpoint handles complex Boolean queries across PubMed&#8217;s 35+ million citations, supporting MeSH term expansion, date range filtering, and publication type restrictions. Retrieved article metadata is fetched via efetch in XML format, extracting structured fields including author affiliations, grant funding sources, and conflict of interest declarations. Citation network analysis uses elink to map forward and backward citations, identifying seminal papers and emerging research trends within specific domains. Full-text access is resolved through PubMed Central&#8217;s OAI-PMH service for open access articles, enabling paragraph-level text extraction for systematic review workflows. The agent constructs PRISMA-compliant search documentation, recording exact queries, database dates, and result counts for reproducible literature reviews. MeSH term analysis identifies concept relationships and suggests query refinements based on the MeSH tree hierarchy. Batch processing handles large result sets with proper API rate limiting and NCBI API key authentication for elevated request quotas.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pubmed-literature-mining-agent/)
